from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from .models import Karma

# Get today's date
today = timezone.now().date()

def my_daily_update():
    send_mail("This is a test email", "Test message", settings.EMAIL_HOST_USER, ["vikassrinitb@gmail.com"])
    return None
    # karmas = Karma.objects.filter(date=today)
    # checked = all(karma.review != 'pe' for karma in karmas)
    #
    # if not checked:
    # #     Send email
    #     pass
