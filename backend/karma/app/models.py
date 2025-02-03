from datetime import timedelta

from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.db import models

# Create your models here.

def next_day_date():
    # Get the next date from now
    return timezone.now() + timedelta(days=1)

def prev_day_date():
    return timezone.now() - timedelta(days=1)


class KarmaType(models.TextChoices):
    PRAYER = "pr", _("Prayer")
    STUDY = "st", _("Study")
    WORK = "wo", _("Work")
    FAMILY = "ho", _("Home")
    PUBLIC = "pu", _("People")
    PLAY = "pl", _("Play")


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
    date = models.DateField()
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

    def get_review_display_name(self):
        return self.get_review_display()
    
    def __str__(self):
        return f"{self.get_review_display_name()}, {self.karma:20}, {self.date}"
    

class DayReview(models.Model):
    """
        Add a review for how the day went on a day-to-day basis
    """
    review = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review: {self.review:20}"


class TodoStatus(models.TextChoices):
    TODO = "to", _("Todo")
    PROGRESS = "pr", _("Progress")
    COMPLETE = "co", _("Complete")


class Todo(models.Model):
    """
        Represents tasks with todo, in-progress, complete status
    """
    todo = models.CharField(max_length=100)
    todo_type = models.CharField(
        max_length=2,
        choices=KarmaType.choices,
        default=KarmaType.STUDY
    )
    status = models.CharField(
        max_length=2,
        choices=TodoStatus.choices,
        default=TodoStatus.TODO
    )
    created_on = models.DateField(auto_now=True)
    deadline = models.DateField()

    def get_todo_type_display_name(self):
        return self.get_todo_type_display()

    def __str__(self):
        return f"{self.get_todo_type_display_name()}, {self.todo}"
    

class Reflection(models.Model):
    """
        Add reflection for the day
    """
    reflection = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date}, Reflection: {self.reflection:20}"
 

