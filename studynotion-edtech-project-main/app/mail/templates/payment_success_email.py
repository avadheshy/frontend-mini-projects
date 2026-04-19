def payment_success_email(name: str, amount: float, order_id: str, payment_id: str) -> str:
    return f"""<!DOCTYPE html>
<html>

<head>
  <meta charset=\"UTF-8\">
  <title>Payment Success</title>
</head>

<body>
  <p>Hello {name},</p>
  <p>Your payment of {amount} was successful.</p>
  <p>Order ID: {order_id}</p>
  <p>Payment ID: {payment_id}</p>
</body>

</html>"""
