from django.urls import path
from .views import ClassListView, BookClassView, BookingListView

urlpatterns = [
    path('classes/', ClassListView.as_view(), name='get_classes'),
    path('book/', BookClassView.as_view(), name='book_class'),
    path('bookings/', BookingListView.as_view(), name='get_bookings'),
]
