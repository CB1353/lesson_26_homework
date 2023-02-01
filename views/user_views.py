from service.user_service import login_user, create_user


def register():
    try:
        user_name = input('Input username')
        first_name = input('Input first name')
        last_name = input('Input last name')
        password = input('Input password')
        return create_user(user_name, first_name, last_name, password)
    except Exception as ex:
        print(ex)
        print('Try again:')
        register()


def log_in():
    user_name = input('Input username')
    password = input('Input password')
    return login_user(user_name, password)
