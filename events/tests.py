from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Event, Ticket, User
from .serializers import EventSerializer, TicketSerializer, UserSerializer


class EventListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('events:event-list')

    def test_event_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EventCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('events:event-create')

    def test_event_create_view(self):
        data = {
            'event_type': 'online',
            'title': 'Test Event',
            'description': 'This is a test event.',
            'is_online': True,
            'max_seats': 100,
            'booking_open_window_start': '2023-01-01T00:00:00Z',
            'booking_open_window_end': '2023-01-02T00:00:00Z'
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TicketCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('events:ticket-create')
        self.user = User.objects.create(username='testuser')

    def test_ticket_create_view(self):
        event = Event.objects.create(
            event_type='online',
            title='Test Event',
            description='This is a test event.',
            is_online=True,
            max_seats=100,
            booking_open_window_start='2023-01-01T00:00:00Z',
            booking_open_window_end='2023-01-02T00:00:00Z'
        )

        data = {
            'event': event.id,
            'user': self.user.id
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
