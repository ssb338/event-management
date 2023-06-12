from django.urls import path
from .views import (
    UserCreateView,
    EventListView,
    EventCreateView,
    EventUpdateView,
    EventSummaryView,
    TicketCreateView,
    TicketListView,
)
from .swagger import schema_view
app_name = 'events'

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/summary/', EventSummaryView.as_view(), name='event-summary'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
]
