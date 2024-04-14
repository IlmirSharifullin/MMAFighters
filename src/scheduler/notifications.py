from typing import Optional


async def send_message(bot, chat_id, text, reply_markup, parse_mode=None) -> Optional[Exception]:
    try:
        await bot.send_message(chat_id, text, reply_markup=reply_markup, parse_mode=parse_mode)
        return None
    except Exception as ex:
        return ex
