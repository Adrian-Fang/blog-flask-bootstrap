# 本文件作用: 包含应用工厂；告诉 Python flaskr 文件夹应当视作为一个包
import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="development",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    from .auth import authRouter
    from .blog import blogRouter
    from .user import userRouter
    from .admin import adminRouter

    db.init_app(app)
    app.register_blueprint(authRouter)
    app.register_blueprint(blogRouter)
    app.register_blueprint(userRouter)
    app.register_blueprint(adminRouter)
    app.add_url_rule("/", endpoint="index")

    return app
