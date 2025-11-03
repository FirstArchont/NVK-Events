from django.conf import settings
from django.core.management import BaseCommand
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
) 

from bot.handlers import (
    start
)

class Command(BaseCommand):
    """Запускает бота"""
    bot = Application.builder().token(settings.TG_BOT_TOKEN).build()

    bot.add_handler(CommandHandler("start", start.main))

    bot.run_polling(allowed_updates=Update.ALL_TYPES)