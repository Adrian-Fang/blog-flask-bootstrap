from flask import Blueprint
from app.controllers.blog import BlogController

blogRouter = Blueprint("blog", __name__)

blogRouter.route("/")(BlogController.home)
blogRouter.route("/index")(BlogController.render_posts)
blogRouter.route("/create", methods=("GET", "POST"))(BlogController.create)
blogRouter.route("/<int:id>/update", methods=("GET", "POST"))(BlogController.update)
blogRouter.route("/<int:id>/delete", methods=("POST",))(BlogController.delete)
