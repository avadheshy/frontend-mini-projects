def course_enrollment_email(course_name: str, student_name: str) -> str:
    return f"""<!DOCTYPE html>
<html>

<head>
  <meta charset=\"UTF-8\">
  <title>Course Enrollment</title>
</head>

<body>
  <p>Hello {student_name},</p>
  <p>You have successfully enrolled in {course_name}.</p>
</body>

</html>"""
