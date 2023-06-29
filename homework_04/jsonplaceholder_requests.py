"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

from aiohttp import ClientSession

async def get_data(url: str):
    async with ClientSession() as session:
        async with session.get(url) as response:
            dict = await response.json()
            return dict


