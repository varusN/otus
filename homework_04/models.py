"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

from sqlalchemy import create_engine

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)

from sqlalchemy.orm import (
    declarative_base,
    relationship,
    scoped_session,
    sessionmaker,
)

import config

engine = create_engine(
    url=config.DB_CONN,
    echo=config.DB_ECHO,
)

Base = declarative_base()

Session = scoped_session(sessionmaker(
    bind=engine,
    expire_on_commit=False,
))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=False,
    )

    title = Column(String)
    body = Column(Text)

    user = relationship(
        "User",
        back_populates="posts",
        uselist=True,
    )