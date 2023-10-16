from flask import render_template


class AdminController:
    def render_homepage(self):
        return render_template("admin/index.html")
