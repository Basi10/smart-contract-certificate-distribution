import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

def send_email(receiver_email, created_asset_id):
    sender_email = "basilelbirru@gmail.com"
    receiver_email = receiver_email
    subject = "Certificate of Completion"
    body = "This is your certificate of completion. In order to recieve it you have to optin on our website using the following key: " + str(created_asset_id)
    load_dotenv()
    email_username = "basilelbirru@gmail.com"
    email_password = os.getenv("EMAIL_PASSWORD")
    print(email_password)
    message = MIMEMultipart()
    message["From"] = sender_email  
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Establish a connection with the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(email_username, email_password)  # Log in to your Gmail account
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email