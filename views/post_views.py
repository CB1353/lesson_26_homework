from service.post_service import PostService


def list_other_posts(user):
    pass


def list_my_posts(user):
    post_service = PostService()
    for p in post_service.list_posts_by_user_id(user.id):
        print(p)


def add_post(user):
    title = input('title:')
    message = input('message:')
    post_service = PostService()
    post_service.create_post(title, message, user)


def add_comment(user):
    # Note: Use post ID to identify what post to leave a comment on
    pass


def list_my_comments(user):
    pass


def list_post_comments(user):
    pass


def delete_post(user):
    # Note: Use post ID to identify what post to delete
    pass
