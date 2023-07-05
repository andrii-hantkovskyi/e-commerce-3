from django.contrib.auth import get_user_model

from favorites.services import create_favorite_list
from users.models import Customer
from waitings.services import create_waiting_list

User = get_user_model()


def _create_user(email: str, password: str) -> User:
    user = User.objects.create_user(email=email, password=password)
    return user


def _create_customer(user: User, first_name: str, last_name: str, phone: str) -> Customer:
    customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name, phone_number=phone)
    return customer


def register_new_customer(email: str, password: str, first_name: str, last_name: str, phone: str) -> Customer | None:
    if not all((email, password, first_name, last_name, phone)):
        raise ValueError('Not all fields provided')
    user = _create_user(email=email, password=password)
    customer = _create_customer(user=user, first_name=first_name, last_name=last_name, phone=phone)
    create_waiting_list(customer)
    create_favorite_list(customer)
    return customer


def update_customer_info(customer: Customer, email, first_name, last_name, phone) -> Customer:
    if email and customer.user.email != email:
        customer.user.email = email
    if first_name and customer.first_name != first_name:
        customer.first_name = first_name
    if last_name and customer.last_name != last_name:
        customer.last_name = last_name
    if phone and customer.phone_number != phone:
        customer.phone_number = phone

    if any((email, first_name, last_name, phone)):
        customer.save()

    return customer
