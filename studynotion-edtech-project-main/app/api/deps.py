from fastapi import Depends, HTTPException, Request, status
from jose import JWTError

from app.core.security import decode_token
from app.db.mongodb import get_database


def get_db():
    return get_database()


def _get_token_from_request(request: Request) -> str | None:
    token = request.cookies.get("token")
    if token:
        return token
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.lower().startswith("bearer "):
        return auth_header.split(" ", 1)[1]
    return None


async def get_current_user(request: Request, db=Depends(get_db)):
    token = _get_token_from_request(request)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Missing")
    try:
        payload = decode_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token is invalid")

    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token is invalid")
    return payload


def require_role(role: str):
    async def _checker(user=Depends(get_current_user), db=Depends(get_db)):
        user_doc = await db.users.find_one({"email": user.get("email")})
        if not user_doc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        if user_doc.get("accountType") != role:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"This is a Protected Route for {role}s")
        return user

    return _checker
