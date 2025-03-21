from django.contrib import admin

from .models import Karma, Todo, Reflection

# Register your models here.
admin.site.register(Karma)
admin.site.register(Todo)
admin.site.register(Reflection)

