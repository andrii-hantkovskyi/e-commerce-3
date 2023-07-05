from django.http import HttpResponse

from waitings.tasks import send_mails_for_waiting_users


# Create your views here.

def test_email_send_view(request):
    send_mails_for_waiting_users.delay()
    return HttpResponse('Task started')
