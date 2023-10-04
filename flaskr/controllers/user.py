from flask import render_template


class UserController:
    def userHome():
        return render_template("user/index.html")
