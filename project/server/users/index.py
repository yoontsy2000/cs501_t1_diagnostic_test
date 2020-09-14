# project/server/users/index

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class ViewUsers(MethodView):
    def get(self):
        users_list = User.query.all()
        ret = ""
        for user in users_list:
            ret += str(user.id) + ": " + user.email + "<br>"
        return ret

# define the API resources
users_view = ViewUsers.as_view('view_users')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)