"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import os
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import jsonplaceholder_requests as js
import config

from models import Base, User, Post, Session

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or config.DB_ASYNC_CONN

async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=config.DB_ECHO,
)


def create_user(session: Session, id: int, name: str, username: str, email: str) -> User:
    user = User(
        id=id,
        name=name,
        username=username,
        email=email,
    )
    session.add(user)
    session.commit()
    return user


def create_post(session: Session, id: int, user_id: int, title: str, body: str) -> Post:
    post = Post(
        id=id,
        user_id=user_id,
        title=title,
        body=body,
    )
    session.add(post)
    session.commit()


def upload_users(list):
    for user in list:
        create_user(
            Session,
            id=user["id"],
            name=user["name"],
            username=user["username"],
            email=user["email"],
        )


def upload_posts(list):
    for post in list:
        create_post(
            Session,
            id=post["id"],
            user_id=post["userId"],
            title=post["title"],
            body=post["body"],
        )


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    users_data, posts_data = await asyncio.gather(
        js.get_data(config.USERS_DATA_URL),
        js.get_data(config.POSTS_DATA_URL),
    )
    return users_data, posts_data


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    users_data, posts_data = asyncio.run(async_main())
    upload_users(users_data)
    upload_posts(posts_data)


if __name__ == "__main__":
    main()
