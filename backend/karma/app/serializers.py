from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Karma, Todo


class KarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karma
        fields = '__all__'
        
    def get_review_display(self, obj):
        return obj.get_review_display()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'