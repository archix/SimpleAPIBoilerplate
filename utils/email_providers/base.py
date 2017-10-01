class BaseEmailProvider:

    provider = None

    def send_email(self, *args, **kwargs):
        raise NotImplementedError('Required method')
