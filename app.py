from flask import Flask

from api_view.account_view import auth_view
from api_view.post_views import post_views

app = Flask('FacebookCloneApp')

app.register_blueprint(auth_view)
app.register_blueprint(post_views)

app.run(port=8080)
