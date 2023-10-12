from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extension import db


class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    body: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User")

    def __init__(self, title=None, body=None, user_id=None):
        self.title = title
        self.body = body
        self.user_id = user_id

    def __repr__(self):
        return f"<Post {self.title!r}>"
