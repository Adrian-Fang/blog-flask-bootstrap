from flask import render_template, request, flash, redirect, g, url_for
from werkzeug.exceptions import abort
from app.routes.auth import login_required
from app.extension import db
from app.models.post import Post


class BlogController:
    def index():
        posts = Post.query.all()
        return render_template("blog/index.html", posts=posts)

    @login_required
    def create():
        if request.method == "POST":
            title = request.form["title"]
            body = request.form["body"]
            error = None

            if not title:
                error = "Title is required."

            if error is not None:
                flash(error)
            else:
                new_post = Post(title=title, body=body)
                db.session.add(new_post)
                db.session.commit()
                return redirect(url_for("blog.index"))
        return render_template("blog/create.html")

    @login_required
    def delete(id):
        post = db.get_or_404(Post, id)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for("blog.index"))

    @login_required
    def update(id):
        post = db.get_or_404(Post, id)
        if request.method == "POST":
            title = request.form["title"]
            body = request.form["body"]
            error = None

            if not title:
                error = "Title is required."

            if error is not None:
                flash(error)
            else:
                db.session.execute(
                    "UPDATE post SET title = ?, body = ?" "WHERE id = ?",
                    (title, body, id),
                )
                db.session.commit()
                return redirect(url_for("blog.index"))
        return render_template("blog/update.html", post=post)


def get_post(id, check_author=True):
    post = db.get_or_404(Post, id)

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post