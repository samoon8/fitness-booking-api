# Fitness Booking API

REST API for managing fitness class schedules and customer bookings with Django and Django REST Framework.

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite for local development

## Features

- List all available fitness classes
- Book a class with client name and email
- Retrieve bookings for a given email address
- Importable Postman collection for quick API testing

## Project Structure

```text
booking_api/          Django project settings and root URLs
studio/               App containing models, serializers, views, and routes
Booking.postman_collection.json
manage.py
```

## Setup

```bash
git clone https://github.com/samoon8/fitness-booking-api.git
cd fitness-booking-api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/classes/` | Return all class schedules |
| POST | `/book/` | Create a booking for a class |
| GET | `/bookings/?email=<client_email>` | Return bookings for a client email |

The same routes are also mounted under `/studio/`:

- `/studio/classes/`
- `/studio/book/`
- `/studio/bookings/?email=<client_email>`

## Sample Requests

### Get classes

```bash
curl http://127.0.0.1:8000/classes/
```

### Book a class

```bash
curl -X POST http://127.0.0.1:8000/book/ \
  -H "Content-Type: application/json" \
  -d '{
    "class_id": 1,
    "client_name": "Sam",
    "client_email": "sam@example.com"
  }'
```

### List bookings

```bash
curl "http://127.0.0.1:8000/bookings/?email=sam@example.com"
```

## Data Model

### `ClassSchedule`

- `name`
- `date_time`
- `instructor`
- `total_slots`
- `available_slots`

### `Booking`

- `class_schedule`
- `client_name`
- `client_email`

## Postman

Import `Booking.postman_collection.json` into Postman to exercise the available endpoints.
