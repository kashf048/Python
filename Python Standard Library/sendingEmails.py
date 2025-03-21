# mimi -> Multipurpose Internet Mail Extension

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path(r"d:\Stack C\All Program\Python\Python Standard Library\template.html").read_text())

message = MIMEMultipart()
message["from"] = "kashfabbas048@gmail.com"
message["to"] = "starm142@gmail.com"
message["subject"] = "This is a test email from Python."
# body = template.substitute({ "name": "Kashf" })
body = template.substitute(name="Kashf")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path(r"d:\Stack C\All Program\Python\Python Standard Library\kashf.jpeg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smpt:
    smpt.ehlo()
    smpt.starttls()     # tls -> Transport Layer Security
    smpt.login("kashfabbas048@gmail.com", "todayskyisdarkblue1234")
    smpt.send_message(message)
    print("Email sent successfully!")









# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib

# # Load the HTML template
# template_path = Path(r"d:\Stack C\All Program\Python\Python Standard Library\template.html")
# if not template_path.exists():
#     raise FileNotFoundError(f"Template file not found: {template_path}")

# template = Template(template_path.read_text())

# # Create the email message
# message = MIMEMultipart()
# message["from"] = "kashfabbas048@gmail.com"
# message["to"] = "starm142@gmail.com"
# message["subject"] = "This is a test email from Python."

# # Substitute the template with the actual name
# body = template.substitute(name="Kashf")
# message.attach(MIMEText(body, "html"))

# # Attach the image
# image_path = Path(r"d:\Stack C\All Program\Python\Python Standard Library\kashf.jpeg")
# if not image_path.exists():
#     raise FileNotFoundError(f"Image file not found: {image_path}")

# message.attach(MIMEImage(image_path.read_bytes()))

# # Send the email
# try:
#     with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()  # Upgrade the connection to secure
#         print("Attempting to log in...")
#         smtp.login("kashfabbas048@gmail.com", "todayskyisdarkblue1234")  # Use your email and password here
#         print("Login successful. Sending email...")
#         smtp.send_message(message)
#         print("Email sent successfully!")
# except smtplib.SMTPAuthenticationError as e:
#     print(f"Error: Authentication failed. Details: {e}")
#     print("Please check your email and password. If you have 2FA enabled, use an App Password.")
# except smtplib.SMTPException as e:
#     print(f"Error: Unable to send email. Details: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")