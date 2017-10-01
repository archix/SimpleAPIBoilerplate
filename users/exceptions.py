from utils.exeptions import BadRequestMixin, UnauthorizedMixin, ForbiddenMixin


class UserException(Exception):
    """Basic exception for errors raised by users app"""
    msg = 'An error occurred'
    status_code = 500

    def __init__(self, msg=None, status_code=None):
        if msg:
            self.msg = msg
        if status_code:
            self.status_code = status_code


class UserBadRequestException(BadRequestMixin, UserException):
    """Raise BadRequest"""


class UserUnauthorized(UnauthorizedMixin, UserException):
    """Raise Unauthorized"""


class UserForbidden(ForbiddenMixin, UserException):
    """Raise Forbidden"""
