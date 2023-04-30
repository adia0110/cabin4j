import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender_email = "aditya.2125csit1115@kiet.edu"
sender_password = "adinet001A@"
recipient_email = "sales@cabin4j.com"
subject = "“Challenges Completed"
name = "Aditya Agarwal"
email = "aditya.2125csit1115@kiet.edu"
mobile_no = "8979148886"
branch = "Computer Science and Information Technology"
year = "2nd"
department = "Engineering"
roll_no = "2100290110011"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

body = f"""Name: {name}
Email: {email}
Mobile No.: {mobile_no}
Branch: {branch}
Year: {year}
Department: {department}
Roll No.: {roll_no}
"""
msg.attach(MIMEText(body))

with open("image_1.jpeg", 'rb') as f:
    image_data = f.read()
image = MIMEImage(image_data, name="passport_photo.jpg")
msg.attach(image)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, recipient_email, msg.as_string())

print("Email sent successfully.")
