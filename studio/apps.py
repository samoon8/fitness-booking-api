from django.apps import AppConfig
from django.utils.timezone import now
from datetime import timedelta

class StudioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studio'

    def ready(self):
        from .models import ClassSchedule
        if not ClassSchedule.objects.exists():
            ClassSchedule.objects.bulk_create([
                ClassSchedule(name="Yoga", date_time=now() + timedelta(days=1), instructor="Aisha", total_slots=10, available_slots=10),
                ClassSchedule(name="Zumba", date_time=now() + timedelta(days=2), instructor="Carlos", total_slots=12, available_slots=12), 
                ClassSchedule(name="HIIT", date_time=now() + timedelta(days=3), instructor="Raj", total_slots=15, available_slots=15),
            ])
