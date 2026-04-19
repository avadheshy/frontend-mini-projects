# Studynotion EdTech Backend (FastAPI)

FastAPI backend ported from the original Express.js implementation.

## Quick start

1) Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Copy environment file and update values:

```bash
cp .env.example .env
```

3) Run the API server:

```bash
uvicorn app.main:app --reload
```

## API base

- `http://127.0.0.1:8000/api/v1`

## Routes (mirrors Express)

- `/auth` -> login/signup/otp/reset/change password
- `/profile` -> profile CRUD, display picture, enrolled courses, instructor dashboard
- `/course` -> courses, sections, subsections, categories, ratings, progress
- `/payment` -> capture/verify payment, success email
- `/reach` -> contact

## Environment

Key variables in `.env`:

- `MONGODB_URL` / `MONGODB_DB`
- `JWT_SECRET`
- Mail: `MAIL_HOST`, `MAIL_USER`, `MAIL_PASS`
- Cloudinary: `CLOUD_NAME`, `CLOUD_API_KEY`, `CLOUD_API_SECRET`, `CLOUD_FOLDER`
- Razorpay: `RAZORPAY_KEY`, `RAZORPAY_SECRET`
- `FRONTEND_RESET_URL`
