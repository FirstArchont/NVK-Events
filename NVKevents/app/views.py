from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from app.forms import EventForm
from app.models import Event, ProfileToEvents
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import json
from django.test import Client
import os
from django.conf import settings
from urllib.parse import urlencode

@csrf_exempt
def index(request):
    if (request.method == "POST"):
        data = json.loads(request.body)
        telegram_id = data.get('telegram_id')
        username = data.get('username')
        profile, created = ProfileToEvents.objects.update_or_create(
            profile=telegram_id,  # Поля для поиска
            defaults={
                'username': username  # Поля для обновления/создания
            }
        )

    events = Event.objects.order_by('datetime')
    return render(request, 'app/index.html', {'events': events})

@csrf_exempt
def events_creater(request, telegram_id):
    profile = ProfileToEvents.objects.get(profile=telegram_id)
    events = Event.objects.filter(profile=profile)
    return render(request, 'app/events_creater.html', {'events': events})

@csrf_exempt
def reviews_creater(request):
    return render(request, 'app/reviews_creater.html')

@csrf_exempt
def reviews_participant(request):
    return render(request, 'app/reviews_participant.html')

@csrf_exempt
def create_event(request, telegram_id):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            profile = ProfileToEvents.objects.get(profile=telegram_id)
            event = form.save(commit=False)
            event.profile = profile  # Устанавливаем связь с профилем
            event.save()
            messages.success(request, 'Мероприятие успешно создано!')
            return redirect('events_creater', telegram_id)  # Перенаправляем на список мероприятий
    else:
        form = EventForm()

    return render(request, 'app/create_event.html', {'form': form})

@csrf_exempt
def list_events(request):
    events = Event.objects.order_by('datetime')
    return render(request, 'app/list.html', {'events': events})

@csrf_exempt
def events_participant(request, telegram_id):
    profile = ProfileToEvents.objects.get(profile=telegram_id)
    events = set()
    for i in Event.objects.all():
        if (profile.username in i.participants):
            events.add(i)
    return render(request, 'app/events_participant.html', {'events': events})

@csrf_exempt
def registration(request, event_id, telegram_id):
    profile = ProfileToEvents.objects.get(profile=telegram_id)
    event = Event.objects.get(id=event_id)
    if profile.username not in event.participants.split("#@#"):
        event.participants += profile.username + "#@#"
    event.save()
    return redirect(f"/events-participant/{telegram_id}")

@csrf_exempt
def delete(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    events = Event.objects.order_by('datetime')
    return render(request, 'app/index.html', {'events': events})

@csrf_exempt
def leave(request, event_id, telegram_id):
    event = Event.objects.get(id=event_id)
    profile = ProfileToEvents.objects.get(profile=telegram_id)
    event.participants = event.participants.replace(profile.username + "#@#", "")
    event.save()
    return redirect(f"/events-participant/{telegram_id}")
    