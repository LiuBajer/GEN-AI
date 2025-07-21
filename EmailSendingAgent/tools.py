from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("GMAIL_PASS")

def send_email(email_content, recipient, subject):
    msg = EmailMessage()
    msg['Subject'] = 'Test'
    msg['From'] = "gmail.com"
    msg['To'] = "gmail.com"
    msg.set_content('Hello this is test')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('gmail.com', password)
            smtp.send_message(msg)
        print('Email sent')
    except Exception as e:
        print(f"Failed to send email {e}")

send_email_definition = {
    "type": "function",
    "function": {
        "name": "send_email",
        "description": "sends email",
        "parameters": {
            "type": "object",
            "properties": {
                "email_content": {"type": "string", "description": "HTML markup of email message"},
                "recipient": {"type": "string", "description": "The recipient of the message"},
                "subject": {"type": "string", "description": "The title or subject of email message"},
            },
            "required": ["email_content", "recipient"]
        }
    }
}