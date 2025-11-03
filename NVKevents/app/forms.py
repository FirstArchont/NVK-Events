from django import forms
from app.models import Event
from django.utils import timezone

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'profile',
            'title',
            'description',
            'short_description',
            'location',
            'datetime',
            'participants_requirements',
            'quantity',
            'cover',
        )
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'participants_requirements': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_datetime(self):
        datetime = self.cleaned_data['datetime']
        if datetime < timezone.now():
            raise forms.ValidationError("Дата мероприятия не может быть в прошлом!")
        return datetime