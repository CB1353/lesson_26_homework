from functools import wraps

from flask import request
from sqlalchemy.exc import NoResultFound

from db.database import Session
from models.models import User, Token


def user_request(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.headers.get('Auth-Token')
        if not token:
            return 'User is not authenticated', 401
        session = Session()
        try:
            user = session.query(User).join(Token).filter(Token.token == token).one()
        except NoResultFound:
            return 'User is not authenticated', 401
        return func(user, *args, **kwargs)

    return wrapped
