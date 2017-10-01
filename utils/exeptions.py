class BadRequestMixin:

    def __init__(self, msg=None):
        if msg is None:
            self.msg = "Bad request"
        self.status_code = 400
        super(BadRequestMixin, self).__init__(msg, status_code=self.status_code)


class UnauthorizedMixin:

    def __init__(self, msg=None):
        if msg is None:
            msg = "Unauthorized"
        self.status_code = 401
        super(UnauthorizedMixin, self).__init__(msg, status_code=self.status_code)


class ForbiddenMixin:

    def __init__(self, msg=None):
        if msg is None:
            msg = "Forbidden"
        self.status_code = 403
        super(ForbiddenMixin, self).__init__(msg, status_code=self.status_code)
