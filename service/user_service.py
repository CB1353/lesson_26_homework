from sqlalchemy.exc import NoResultFound

from db.database import Session
from models.models import User


def create_user(username, firstname, last_name, password):
    my_user = User(
        user_name=username,
        first_name=firstname,
        last_name=last_name
    )
    my_user.set_password(password)
    session = Session()  # Create new session
    session.add(my_user)  # Add user to the session
    session.commit()  # Save changes to the database
    return my_user


def list_all_users():
    session = Session()
    all_users = session.query(User).all()
    print(all_users)
    users_count = session.query(User).count()
    print(users_count)
    # 1
    my_user = session.query(User).filter(User.user_name == 'mtricolici').one()
    print(my_user)


def login_user(username, password):
    session = Session()
    try:
        user = session.query(User).filter(User.user_name == username).one()
    except NoResultFound:
        raise Exception("User does not exist")
    if not user.password == user.hash_password_text(password):
        raise Exception("Password incorrect")
    return user  # Success
