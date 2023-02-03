from db.database import Session
from models.models import User, Post
from service.post_service import list_posts_for_other, list_posts_for_user, create_post, add_comment_on_post, \
    list_comments_on_post


def list_other_posts(user):
    print("Others posts: \n")
    posts = list_posts_for_other(user.id)
    for post in posts:
        print(post)
    print("\n")


def list_my_posts(user):
    print("My posts: \n")
    for post in list_posts_for_user(user.id):
        print(post)
    print("\n")


def add_post(user):
    title = input('Post title')
    message = input('Post message')
    post = create_post(title, message, user)
    print(f'Post {post.title} created succesfully')


def add_comment(user):
    list_my_posts(user)
    post_id = input('Post ID')
    message = input('Comment message')
    add_comment_on_post(post_id, user.id, message)
    print('Comment added successfully')


def list_my_comments(user):
    with Session() as session:
        user = session.query(User).filter(User.id == user.id).one()
        for comment in user.comments:
            print(comment)


def list_post_comments(user):
    list_my_posts(user)
    list_other_posts(user)
    post_id = input('Select Post ID:')
    comments = list_comments_on_post(post_id)
    for comment in comments:
        print(comment)


def delete_post(user):
    list_my_posts(user)
    list_other_posts(user)
    with Session() as session:
        post_id = input('Select post ID to delete')
        try:
            post = session.query(Post).filter((Post.id == post_id) & (User.id == user.id)).one()
            session.delete(post)
            session.commit()
        except Exception as ex:
            print(ex)
