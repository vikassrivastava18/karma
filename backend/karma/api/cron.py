from datetime import timedelta
from django.utils import timezone
from .models import Karma

# Get today's date
today = timezone.now().date()

def my_cron_job():
    karmas = Karma.objects.filter(date=today)
    checked = all(karma.review != 'pe' for karma in karmas)

    if not checked:
    #     Send email
        pass
