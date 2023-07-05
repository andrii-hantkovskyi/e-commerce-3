
from django.urls import path

from waitings.views import test_email_send_view

urlpatterns = [
    path('send-mails/', test_email_send_view, name='email_send')
]
