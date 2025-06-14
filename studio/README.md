# Fitness Studio Booking API
Assignment: API for managing fitness class bookings at a fictional fitness studio offering using Django REST API Framework.

Author: Shyamala G
---

## Features

- View upcoming classes (`GET /classes`)
- Book a spot in a class (`POST /book`)
- View bookings by client email (`GET /bookings?email=`)

---

## Tech Stack

- Python 3.12
- Django 5.2
- Django REST Framework
- SQLite
- Postman for API testing

---

##  Setup Instructions

1. **Clone or unzip this project**
   ```bash
   cd assignment_booking_api
   ```

2. **Create and activate a virtual environment (in linux)**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencie**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the server**
    ```bash
    python manage.py runserver
    ```

6. **Visit endpoints using Postman or browser**

Note: To added Instructor and classes use Django Admin
to add User use the following command
```
python manage.py createsuperuser
```

## API Endpoints

### To return all classes
Returns all upcoming classes.
```
GET /classes
```

Response:
```
[
  {
    "id": 1,
    "name": "Yoga",
    "date_time": "2025-06-14T10:00:00Z",
    "instructor": "Aisha",
    "total_slots": 10,
    "available_slots": 2
  }
]
```

### To do booking
```
 POST /book
```
Books a class by class ID.
Request JSON:
```
{
  "class_id": 1,
  "client_name": "Shyam",
  "client_email": "shyam@example.com"
}
```


Success Response:
```
{
  "message": "Booking successful."
}
```

Error (if full):
```
{
  "error": "Class is fully booked."
}
```

### To get Bookings

```
GET /bookings?email=example@example.com
```

Returns all bookings for the given email.
Response:
```

[
  {
    "id": 1,
    "class_schedule": 1,
    "client_name": "name",
    "client_email": "example@example.com"
  }
]
```
