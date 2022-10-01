from src.telegram import dispatcher_context
from src.core.settings import settings
from src.schemas import BotInDB


async def is_up(bot: BotInDB) -> bool:
    with dispatcher_context(bot.scenario, bot.id, bot.token) as dispatcher:
        webhook_info = await dispatcher.bot.get_webhook_info()
    return webhook_info.url == settings.WEBHOOK_URL


async def set_(bot: BotInDB) -> None:
    with dispatcher_context(bot.scenario, bot.id, bot.token) as dispatcher:
        await dispatcher.bot.set_webhook(
            url=settings.WEBHOOK_URL,
            secret_token=bot.webhook_key,
            drop_pending_updates=True
        )


async def delete(bot: BotInDB) -> None:
    with dispatcher_context(bot.scenario, bot.id, bot.token) as dispatcher:
        await dispatcher.bot.delete_webhook(drop_pending_updates=True)
