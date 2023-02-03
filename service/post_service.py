from db.database import Session
from models.models import Post, User, Comment


def create_post(title, message, user):
    session = Session()
    post = Post(title=title, message=message, created_by_id=user.id)
    session.add(post)
    session.commit()
    return post


def list_posts():
    session = Session()
    return session.query(Post).all()


def list_posts_for_user(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).one()
    return user.posts


def list_posts_for_other(user_id):
    session = Session()
    posts = session.query(Post).filter(Post.created_by_id != user_id).all()
    return posts


def create_post_by_user(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).one()
    new_post = Post(title='Adding extra post', message='Post message')
    user.posts.append(new_post)
    session.commit()


def list_comments_on_post(post_id):
    session = Session()
    comments = session.query(Comment).join(Post).filter((Post.id == post_id)).all()
    return comments


def comments_on_post_by_user(post_id, user_id):
    session = Session()
    comments = session.query(Comment).join(Post).join(User).filter((Post.id == post_id) & (User.id == user_id)).all()
    return comments


def add_comment_on_post(post_id, by_user_id, message):
    with Session() as session:
        comment = Comment(
            post_id=post_id,
            message=message,
            user_id=by_user_id
        )
        session.add(comment)
        session.commit()
