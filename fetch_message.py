import random
import aiohttp

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        message_url = f"https://christmas-ea96b.firebaseapp.com/api/christmas-messages/{random.randint(1,70)}"
        async with session.get(message_url) as resp:
            message = await resp.json()
            return(message['message'])