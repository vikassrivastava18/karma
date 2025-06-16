from django.shortcuts import render
from twilio.rest import Client
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse

from django.contrib.auth.models import User
from api.models import Todo, UserProfile

# Create your views here.
def my_hourly_status():
    # Send messages to vikas
    users = User.objects.all()
    for user in users:
        # Find pending todos that are not archived, and send sms
        phone_number = UserProfile.objects.get(user=user).phone_number
        if not phone_number:
            continue
        pending_todos = Todo.objects.filter(
            Q(status='TODO') | Q(status='PROGRESS'),
            deadline__lt=timezone.now(),
            user=user,
            archived=False
        )
        message_to_broadcast = "\n".join([todo.todo for todo in pending_todos])

        message_to_broadcast = ("Pending Todos:")
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(to=phone_number,
                                    from_=settings.TWILIO_NUMBER,
                                    body=message_to_broadcast)

    return HttpResponse("messages sent!" + message_to_broadcast, 200)

def my_daily_update():
    message_to_broadcast = ("How was your day? Please complete the daily feedback")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!" + message_to_broadcast, 200)


def my_todays_todos():
    message_to_broadcast = ("Good morning? Please complete your today's task plan")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!" + message_to_broadcast, 200)
