from views.post_views import add_post, add_comment, list_other_posts, list_my_posts, list_my_comments, \
    list_post_comments, delete_post
from views.user_views import log_in, register


def not_logged_in():
    print('1: To log-in')
    print('2: To Register')
    option = input('Option')
    if option == '1':
        return log_in()
    elif option == '2':
        return register()


def menu(user):
    map = {
        '1': add_post,
        '2': add_comment,
        '3': list_other_posts,
        '4': list_my_posts,
        '5': list_my_comments,
        '6': list_post_comments,
        '7': delete_post,
    }
    print('1: Make Post')
    print('2: Make Comment')
    print('3: List other posts')
    print('4: List my posts')
    print('5: List my comments')  # Comments I have created
    print('6: List post comments')  # Comments for a post by post_id
    print('6: Delete post')  # Comments for a post by post_id
    while True:
        opt = input('Option: ')
        try:
            map[opt](user)  # executing option
        except KeyError as ex:
            print("Invalid option")
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    user = None
    while not user:
        try:
            user = not_logged_in()
        except Exception as ex:
            print(ex)
    while True:
        menu(user)
