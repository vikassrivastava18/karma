from datetime import timedelta, timezone

from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.db import models

# Create your models here.

def next_day_date():
    # Get the next date from now
    return timezone.now() + timedelta(days=1)


class KarmaType(models.TextChoices):
    PRAYER = "pr", _("Prayer")
    STUDY = "st", _("Study")
    WORK = "wo", _("Work")
    FAMILY = "ho", _("Home")
    PUBLIC = "pu", _("People")


class KarmaReview(models.TextChoices):
    PENDING = "pe", _("Pending")
    SATISFIED = "sa", _("Satisfied")
    UNSATISFIED = "us", _("Unsatisfied")
        

class Karma(models.Model):
    """
        Represents daily routines like Puja, Study, etc.
        Every karma is either type daily(prayer, regular)
        Every karma has three possible state - Pending, Good, Bad
    """
    title = models.CharField(max_length=32)
    karma = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=next_day_date)
    daily = models.BooleanField(default=True)
    type = models.CharField(
         max_length=2,
         choices=KarmaType.choices,
         default=KarmaType.STUDY
    )    
    review = models.CharField(
        max_length=2, 
        choices= KarmaReview.choices,
        default=KarmaReview.PENDING
    )

    def __str__(self):
        return f"Task: {self.karma}, Review: {self.review}"
    

class DayReview(models.Model):
    """
        Add a review for how the day went on a day to day basis
    """
    review = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review: {self.review:20}"
    