from sqlalchemy import Integer, String, Text, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.extension import db

# from app.models import User


class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    body: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())

    # Read more about Models and Tables, https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html
    user: Mapped["User"] = relationship(back_populates="posts")

    def __init__(self, title=None, body=None, user_id=None, created_at=None):
        self.title = title
        self.body = body
        self.user_id = user_id
        self.created_at = created_at

    def __repr__(self):
        return f"<Post {self.id, self.title!r}>"
