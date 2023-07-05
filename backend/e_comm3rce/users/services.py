from django.contrib.auth import get_user_model

from users.models import Customer

User = get_user_model()


def _create_user(email: str, password: str) -> User:
    user = User.objects.create_user(email=email, password=password)
    return user


def _create_customer(user: User, first_name: str, last_name: str, phone: str) -> Customer:
    customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name, phone_number=phone)
    return customer


def register_new_customer(email: str, password: str, first_name: str, last_name: str, phone: str) -> Customer:
    user = _create_user(email=email, password=password)
    customer = _create_customer(user=user, first_name=first_name, last_name=last_name, phone=phone)
    return customer
