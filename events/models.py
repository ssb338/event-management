from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)


class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_online = models.BooleanField(default=False)
    max_seats = models.PositiveIntegerField()
    booking_open_window_start = models.DateTimeField()
    booking_open_window_end = models.DateTimeField()

    def is_booking_open(self):
        now = timezone.now()
        return self.booking_open_window_start <= now <= self.booking_open_window_end

    def get_ticket_count(self):
        return self.tickets.count()


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    booking_open_window_start = models.DateTimeField(auto_now_add=True)
