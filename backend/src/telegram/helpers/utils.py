import httpx
from aiogram.bot.api import check_token
from aiogram.utils.exceptions import ValidationError


async def validate_token(token: str) -> bool:
    try:
        check_token(token)
    except ValidationError:
        return False
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f'https://api.telegram.org/bot{token}/getMe'
        )
    if res.status_code != 200:
        return False
    return True
