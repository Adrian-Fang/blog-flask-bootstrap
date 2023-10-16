import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash
from app.extension import db
from app.models import User

authRouter = Blueprint("auth", __name__, url_prefix="/auth")


@authRouter.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                hashed_password = generate_password_hash(password)
                db.session.add(User(username=username, password=hashed_password))
                db.session.commit()
            except IntegrityError:
                error = f"User ${username} is already registered."
            except SQLAlchemyError:
                error = "An error occurred while creating user."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@authRouter.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        user = db.session.execute(select(User).filter_by(username=username)).scalar()
        if user is None:
            error = "username not exists."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("blog.index"))

        flash(error)

    return render_template("auth/login.html")


@authRouter.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = db.session.execute(select(User).filter_by(id=user_id)).scalar()


@authRouter.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view
