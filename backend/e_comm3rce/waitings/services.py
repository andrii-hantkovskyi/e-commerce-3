from typing import List

from waitings.models import WaitingList, WaitingProduct


def get_all_waiting_lists():
    return WaitingList.objects.all()


def get_available_products_in_waiting_list(waiting_list: WaitingList) -> List[WaitingProduct]:
    return waiting_list.objects.prefetch_related('products').filter(product__is_available=True)
