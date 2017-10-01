from flask import current_app
from mailjet_rest import Client

from utils.email_providers.base import BaseEmailProvider


class MailjetProvider(BaseEmailProvider):
    def __init__(self):
        self.provider = Client(
            auth=(current_app.config['MAILJET_PUBLIC_KEY'], current_app.config['MAILJET_SECRET_KEY']),
            version='v3')

    def send_email(self, from_name, from_email, subject, text, recipients_list):
        email = {
            'FromName': from_name,
            'FromEmail': from_email,
            'Subject': subject,
            'Text-Part': text,
            'Recipients': recipients_list
            # 'Recipients': [{'Email': 'your email here'}]
        }
        return self.provider.send.create(email)
