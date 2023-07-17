from typing import List

from cart.services import get_cart_by_id
from orders.models import Order


def get_customer_orders(customer_id: int) -> List[Order]:
    return Order.objects.filter(owner_id=customer_id)


def get_customer_order(order_id: int, customer_id: int) -> Order:
    return Order.objects.get(id=order_id, owner_id=customer_id)


def create_new_order(customer_id: int, cart_id: int, delivery_type: str, address: str) -> None:
    cart = get_cart_by_id(cart_id)
    if not cart.products.exists():
        raise ValueError("Cart is empty")
    if Order.objects.filter(cart_id=cart_id).exists():
        raise ValueError("Cart is already in an order")
    if cart.owner.id != customer_id:
        raise ValueError("It's not you cart")
    Order.objects.create(owner_id=customer_id, cart_id=cart_id, delivery_type=delivery_type, address=address)
