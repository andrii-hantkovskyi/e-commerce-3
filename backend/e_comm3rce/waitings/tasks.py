from celery import shared_task


@shared_task
def send_mails_for_waiting_users():
    from django.conf import settings
    from django.core.mail import send_mail
    from waitings.services import get_all_waiting_lists, get_available_products_in_waiting_list

    waiting_lists = get_all_waiting_lists()

    for waiting_list in waiting_lists:
        available_products = get_available_products_in_waiting_list(waiting_list)
        if len(available_products) > 0:
            products = [product.product for product in available_products]
            send_mail(
                f'Waiting products are available!',
                'Hey! Your products:\n{0} are available for purchase!'.format(
                    ",\n".join([product.name for product in products])),
                settings.EMAIL_SENDER,
                [waiting_list.owner.user.email],
                fail_silently=False,
            )
    return None
