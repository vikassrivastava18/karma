from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Karma


class KarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karma
        fields = '__all__'
        
    def get_review_display(self, obj):
        return obj.get_review_display()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'