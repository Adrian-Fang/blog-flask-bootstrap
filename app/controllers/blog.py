from flask import render_template, request, flash, redirect, g, url_for
from werkzeug.exceptions import abort
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.routes.auth import login_required
from app.extension import db
from app.models import Post


class BlogController:
    def index(self):
        posts = db.session.scalars(select(Post))
        return render_template("blog/index.html", posts=posts)

    @login_required
    def create(self):
        if request.method == "POST":
            title = request.form["title"]
            body = request.form["body"]
            error = None

            if not title:
                error = "Title is required."

            if error is not None:
                flash(error)
            else:
                try:
                    new_post = Post(title=title, body=body, user_id=g.user.id)
                    db.session.add(new_post)
                    db.session.commit()
                except IntegrityError:
                    abort(400, message="A blog with the same name already exists.")
                except SQLAlchemyError:
                    abort(500, message="An error occurred while creating new post.")

                return redirect(url_for("blog.index"))
        return render_template("blog/create.html")

    @login_required
    def delete(self, post_id: id):
        try:
            post = db.get_or_404(Post, post_id)
            db.session.delete(post)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message=f"An error occurred while deleting post {post_id}.")

        return redirect(url_for("blog.index"))

    @login_required
    def update(self, post_id: id):
        post = db.get_or_404(Post, post_id)
        if request.method == "POST":
            title = request.form["title"]
            body = request.form["body"]
            error = None

            if not title:
                error = "Title is required."

            if error is not None:
                flash(error)
            else:
                try:
                    db.session.execute(
                        db.update(Post),
                        [{"id": post.id, "title": title, "body": body}],
                    )
                    db.session.commit()
                except SQLAlchemyError:
                    abort(500, message=f"Updating post <{post.title}> failed.")

                return redirect(url_for("blog.index"))
        return render_template("blog/update.html", post=post)


def get_post(post_id: id, check_author=True):
    post = db.get_or_404(Post, post_id)

    if post is None:
        abort(404, f"Post id {post_id} doesn't exist.")

    if check_author and post["user_id"] != g.user["id"]:
        abort(403)

    return post
