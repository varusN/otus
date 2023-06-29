"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def get_data(url: str):
    async with ClientSession() as session:
        async with session.get(url) as response:
            dict = await response.json()
            return dict

async def get_users_data():
    result = await get_data(USERS_DATA_URL)
    return result

async def get_posts_data():
    result = await get_data(POSTS_DATA_URL)
    return result