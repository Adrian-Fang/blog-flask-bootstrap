from flask import Blueprint
from flaskr.controllers.admin import AdminController

adminRouter = Blueprint("admin", __name__)

adminRouter.route("/admin")(AdminController.adminHome)
