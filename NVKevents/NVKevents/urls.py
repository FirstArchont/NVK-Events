"""
URL configuration for NVKevents project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('events-creater/<int:telegram_id>', events_creater, name="events_creater"),
    path('events-participant/<int:telegram_id>', events_participant, name="events_participant"),
    path('list-events', list_events, name="list_events"),
    path('reviews-creater', reviews_creater, name="reviews_creater"),
    path('reviews-participant', reviews_participant, name="reviews_participant"),
    path('create-event/<int:telegram_id>', create_event, name="create_event"),
    path('registration/<int:event_id>/<int:telegram_id>', registration, name="registration"),
    path('delete/<int:event_id>', delete, name="delete"),
    path('leave/<int:event_id>/<int:telegram_id>', leave, name="leave"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
