from cart.models import Cart, CartProduct


def get_last_cart_by_customer_id_or_create(customer_id: int) -> Cart:
    cart = Cart.objects.filter(owner_id=customer_id, order=None).last()
    if not cart:
        created_cart = Cart.objects.create(owner_id=customer_id)
        return created_cart
    return cart


def get_cart_by_id(cart_id: int) -> Cart:
    return Cart.objects.get(id=cart_id)


def add_product_to_cart(cart_id: int, product_id: int) -> None:
    CartProduct.objects.create(cart_id=cart_id, product_id=product_id, qty=1)


def change_product_qty(cp_id: int, qty: int) -> None:
    cp = _get_cart_product_by_id(cp_id)
    cp.qty = int(qty)
    cp.save()


def remove_product_from_cart(cp_id: int) -> None:
    cp = _get_cart_product_by_id(cp_id)
    cp.delete()


def _get_cart_product_by_id(cp_id: int) -> CartProduct:
    return CartProduct.objects.get(id=cp_id)
