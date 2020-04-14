from rest_framework import serializers
from . import models


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'price', 'status', 'created_at', 'modified_at',)
        model = models.MenuResto
