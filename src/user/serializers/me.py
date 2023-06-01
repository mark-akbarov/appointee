from rest_framework import serializers
from models.base import BaseUser


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'phone_number',
            )