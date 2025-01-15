import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.Schema.Users import UserSchema
from app.Models.Users import User
from app.Models.db import db
from flask_jwt_extended import create_access_token

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegisterResource(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        if User.query.filter_by(username=user_data["username"]).first():
            abort(400, message="Username already exists.")

        user = User(id=str(uuid.uuid4()), **user_data)
        db.session.add(user)
        db.session.commit()
        return user

@blp.route("/login")
class UserLoginResource(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = User.query.filter_by(username=user_data["username"]).first()
        if not user or user.password != user_data["password"]:
            abort(401, message="Invalid credentials.")

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}
