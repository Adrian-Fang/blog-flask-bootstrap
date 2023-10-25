from flask import Blueprint
from app.controllers.user import UserController

userRouter = Blueprint("user", __name__)


userRouter.route("/user")(UserController.user_home)
