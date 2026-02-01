from email.message import EmailMessage
import json
import smtplib

import boto3


def send_email(sender_email, sender_app_password, recipient_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_app_password)
        server.send_message(msg)


if __name__ == "__main__":
    client = boto3.client('secretsmanager')
    sender_email = json.loads(client.get_secret_value(SecretId='personal_email').get(
        'SecretString'))['personal_email']
    sender_app_password = json.loads(client.get_secret_value(SecretId='gmail_app_password').get(
        'SecretString'))['gmail_app_password']
    send_email(sender_email, sender_app_password, sender_email, 'test', 'test')
