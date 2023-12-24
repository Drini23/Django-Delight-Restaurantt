from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from inventory.models import MenuItem



    
    
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'price']
    
    
    