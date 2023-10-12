from flask import render_template


class UserController:
    def user_home(self):
        return render_template("user/index.html")
