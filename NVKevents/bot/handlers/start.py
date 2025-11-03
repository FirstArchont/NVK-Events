from re import findall
from telegram.ext import ContextTypes, ConversationHandler
from asgiref.sync import sync_to_async
from telegram import ReplyKeyboardMarkup, Update
from django.utils import timezone
from bot.models import Profile
import os

@sync_to_async
def update_or_create_profile(tg_id, username, first_name, last_name, photo):
    """Создает или обновляет профиль пользователя"""
    profile, created = Profile.objects.update_or_create(
        tg_id=tg_id,
        defaults={
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "photo": photo,
        },
    )
    if created:
        profile.registration_date = timezone.now().date()
    profile.save()

async def main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Приветствует пользователя"""
    user = update.effective_user
    matches = dict(findall(r"(\w+)='?([^',)]+)'?", str(user)))

    tg_id = int(matches.get("id"))
    username = matches.get("username")
    first_name = matches.get("first_name")
    last_name = matches.get("last_name")
    photos = await context.bot.get_user_profile_photos(tg_id, limit=1)
    
    if photos.photos:
        # Берем фото с самым высоким разрешением (последнее в списке)
        photo = photos.photos[0][-1]
        file = await context.bot.get_file(photo.file_id)
        
        # Формируем путь для сохранения
        filename = f"bot/profiles/{user.id}.jpg"
        
        # Скачиваем фото
        await file.download_to_drive(f"{os.getcwd()}/media/{filename}")
    await update_or_create_profile(tg_id, username, first_name, last_name, filename)

    await update.message.reply_html(
        f"Привет, {user.mention_html()} 👋\n\n"
    )