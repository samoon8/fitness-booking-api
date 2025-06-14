from django.db import models

class ClassSchedule(models.Model):
    name = models.CharField(max_length=50)  # Yoga, Zumba, HIIT
    date_time = models.DateTimeField()      # Date and time of the class
    instructor = models.CharField(max_length=100)
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} at {self.date_time} by {self.instructor}"


class Booking(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()

    def __str__(self):
        return f"{self.client_name} booked {self.class_schedule.name}"
