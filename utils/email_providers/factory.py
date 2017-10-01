from utils.email_providers.mailjet.provider import MailjetProvider


class EmailProviderFactory:

    @classmethod
    def get_email_provider(cls, provider):
        if provider == 'mailjet':
            return MailjetProvider()
        return None
