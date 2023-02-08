from api_view.utils import user_request
from service.post_service import list_posts_for_user, create_post, list_posts_for_other
from flask import Blueprint, jsonify, request
import json

post_views = Blueprint('posts', __name__)


@post_views.route('/posts/list/my')
@user_request
def list_my_posts(user):
    print(user)
    r_data = []
    for post in list_posts_for_user(user.id):
        r_data.append(
            dict(
                title=post.title,
                message=post.message
            )
        )
    return jsonify(r_data), 200


@post_views.route('/posts/list/other')
@user_request
def list_other_posts(user):
    r_data = []
    for post in list_posts_for_other(user.id):
        r_data.append(
            dict(
                title=post.title,
                message=post.message
            )
        )
    return jsonify(r_data), 200


@post_views.route('/posts/comments/<post_id>')
@user_request
def get_comments_for_post(user, post_id):
    # Post id is part of the URL
    # For example accessing localhost:8080/posts/comments/1/ will return comments for post_id 1
    # TODO: Implement
    pass


@post_views.route('/posts/comments/<post_id>/add/', methods=['POST'])
@user_request
def add_comment_on_post(user, post_id):
    # Post id is part of the URL
    # For example sending request to localhost:8080/posts/comments/1/add/
    # will add the comment to post with id 1
    # TODO: Implement
    pass


@post_views.route('/posts/add')
@user_request
def add_post(user):
    req_data = json.loads(request.data)
    title = req_data.get('title')
    message = req_data.get('message')
    post = create_post(title, message, user)
    return 200
