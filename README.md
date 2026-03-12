# 🏋️ Fitness Class Booking API

A RESTful API built with Django REST Framework for managing fitness 
studio class bookings, user authentication, and session scheduling.

## 🛠 Tech Stack
- **Backend:** Django 5, Django REST Framework
- **Database:** PostgreSQL (SQLite for dev)
- **Auth:** JWT (djangorestframework-simplejwt)
- **Testing:** Postman

## ✨ Features
- User registration & JWT login/logout
- Browse available fitness classes
- Book / cancel a class session
- View booking history
- Role-based access (admin vs user)

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register/ | Register new user |
| POST | /api/auth/login/ | Login, get JWT token |
| GET | /api/classes/ | List all fitness classes |
| POST | /api/bookings/ | Book a class |
| GET | /api/bookings/ | View my bookings |
| DELETE | /api/bookings/{id}/ | Cancel booking |

## ⚙️ Setup
```bash
git clone https://github.com/samoon8/fitness-booking-api
cd fitness-booking-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 📮 Postman Collection
Import `Booking.postman_collection.json` to test all endpoints instantly.
