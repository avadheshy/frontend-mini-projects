def contact_us_email(email: str, firstname: str, lastname: str, message: str, phone_no: str, countrycode: str) -> str:
    return f"""<!DOCTYPE html>
<html>

<head>
  <meta charset=\"UTF-8\">
  <title>Contact Form</title>
</head>

<body>
  <p>Hello {firstname} {lastname},</p>
  <p>We received your message:</p>
  <p>{message}</p>
  <p>Phone: {countrycode} {phone_no}</p>
  <p>Email: {email}</p>
</body>

</html>"""
