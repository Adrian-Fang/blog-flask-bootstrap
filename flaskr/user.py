from flask import Blueprint
from flaskr.controllers.user import UserController

userRouter = Blueprint("user", __name__)


userRouter.route("/user")(UserController.userHome)
