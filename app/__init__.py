from flask import Flask
from config import Config
from app.extension import db
from app.routes import userRouter, adminRouter, blogRouter, authRouter


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    if config_class is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_object(config_class)

    # initialize Flask extensions here
    db.init_app(app)

    # import app.models

    with app.app_context():
        db.create_all()

    # Register blueprints here...
    app.register_blueprint(authRouter)
    app.register_blueprint(blogRouter)
    app.register_blueprint(userRouter)
    app.register_blueprint(adminRouter)
    
    app.add_url_rule("/", endpoint="index")

    return app
