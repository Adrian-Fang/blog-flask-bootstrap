from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extension import db


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    password: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120), nullable=True, unique=True)
    posts = relationship("Post", back_populates="user", lazy="dynamic")

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"
