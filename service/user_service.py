from uuid import uuid4

from sqlalchemy.exc import NoResultFound, MultipleResultsFound, IntegrityError

from db.database import Session
from models.models import User, Token


def create_user(username, firstname, last_name, password):
    my_user = User(
        user_name=username,
        first_name=firstname,
        last_name=last_name
    )
    my_user.set_password(password)
    try:
        session = Session()  # Create new session
        session.add(my_user)  # Add user to the session
        session.commit()  # Save changes to the database
    except IntegrityError:
        raise Exception('User already exists')
    return my_user


def list_all_users():
    with Session() as s:
        all_users = s.query(User).all()
        print('There are: ', s.query(User).count(), 'users total.')
        for user in all_users:
            print(user)


def get_user_by_username(username):
    with Session() as s:
        try:
            user = s.query(User).filter(User.user_name == username).one()
            print(user)
            return user
        except NoResultFound:
            print('User not found')
        except MultipleResultsFound:
            print('Multiple users with this username')


def login_user(username, password):
    session = Session()
    try:
        user = session.query(User).filter(
            User.user_name == username,
            User.password == User.hash_password_text(password)
        ).one()
    except NoResultFound:
        raise Exception("Credentials dont match any user in the system")
    uuid_str = str(uuid4())
    try:
        existing_toekn = session.query(Token).filter(
            Token.user_id == user.id
        ).one()
        return existing_toekn
    except NoResultFound:
        tkn = Token(
            token=uuid_str,
            user=user
        )
        session.add(
            tkn
        )
        session.commit()
        return tkn
