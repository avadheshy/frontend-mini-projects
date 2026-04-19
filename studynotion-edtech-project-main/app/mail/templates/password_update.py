def password_updated(email: str, message: str) -> str:
    return f"""<!DOCTYPE html>
<html>

<head>
  <meta charset=\"UTF-8\">
  <title>Password Update</title>
</head>

<body>
  <p>Hello {email},</p>
  <p>{message}</p>
</body>

</html>"""
