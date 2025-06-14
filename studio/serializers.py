from rest_framework import serializers
from .models import ClassSchedule, Booking

class ClassScheduleSerializer(serializers.ModelSerializer):
    date_time = serializers.DateTimeField(format="%d %B %Y, %I:%M %p")
    class Meta:
        model = ClassSchedule
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
