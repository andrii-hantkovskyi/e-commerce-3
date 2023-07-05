from typing import List

from django.contrib.auth import get_user_model

from waitings.models import WaitingList, WaitingProduct

User = get_user_model()


def get_all_waiting_lists() -> List[WaitingList]:
    return WaitingList.objects.all()


def get_available_products_in_waiting_list(waiting_list: WaitingList) -> List[WaitingProduct]:
    return waiting_list.objects.prefetch_related('products').filter(product__is_available=True)


def create_waiting_list(user: User) -> WaitingList:
    return WaitingList.objects.create(owner=user)
