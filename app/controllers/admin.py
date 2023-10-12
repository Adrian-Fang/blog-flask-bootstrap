from flask import render_template


class AdminController:
    def adminHome():
        return render_template("admin/index.html")
