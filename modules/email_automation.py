import smtplib
from email.mime.text import MIMEText

class EmailAutomation:

    def __init__(self, config):
        self.server = config["smtp_server"]
        self.port = config["smtp_port"]
        self.sender = config["sender_email"]
        self.password = config["password"]

    def send_email(self, receiver, subject, body):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = receiver

        with smtplib.SMTP(self.server, self.port) as server:
            server.starttls()
            server.login(self.sender, self.password)
            server.send_message(msg)
