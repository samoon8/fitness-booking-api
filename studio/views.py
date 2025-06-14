from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClassSchedule, Booking
from .serializers import ClassScheduleSerializer, BookingSerializer
from django.shortcuts import get_object_or_404

import logging
logger = logging.getLogger(__name__)


class ClassListView(APIView):
    def get(self, request):
        classes = ClassSchedule.objects.all()
        serializer = ClassScheduleSerializer(classes, many=True)
        return Response(serializer.data)

class BookClassView(APIView):
    def post(self, request):
        data = request.data

        # Validate required fields
        required_fields = ['class_id', 'client_name', 'client_email']
        missing = [field for field in required_fields if not data.get(field)]
        if missing:
            return Response(
                {"error": f"Missing required field(s): {', '.join(missing)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Reload the class schedule with fresh data
        class_obj = get_object_or_404(ClassSchedule, id=data.get('class_id'))

        # Refresh from DB before checking slots
        class_obj.refresh_from_db()

        if class_obj.available_slots <= 0:
            return Response({"error": "Class is fully booked."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the booking
        booking = Booking.objects.create(
            class_schedule=class_obj,
            client_name=data.get('client_name'),
            client_email=data.get('client_email')
        )

        class_obj.available_slots -= 1
        class_obj.save()

        logger.info(f"Booking created: {booking.client_name} booked {class_obj.name} (ID: {class_obj.id})")

        return Response({"message": "Booking successful."}, status=status.HTTP_201_CREATED)

class BookingListView(APIView):
    def get(self, request):
        email = request.GET.get('email')
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
