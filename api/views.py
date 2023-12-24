from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import MenuItemSerializer
from inventory.models import MenuItem

# Create your views here.
"""
@api_view(['GET', 'POST'])
def menu_item(request):
    if request.method == 'GET':
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['PUT',  'GET', 'DELETE'])
def menu_detail(request, pk):
    menu = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'GET':    
        serializer = MenuItemSerializer(menu) 
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MenuItemSerializer(menu, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if menu.price >= 3:
            return Response({'error' 'nuk fshihet objekti '})
        menu.delete()
        return Response({"error": 'objekti u fshi'})"""
    
    
class MenuViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    def delete(self, request, pk):
        menu = get_object_or_404(MenuItem, pk=pk)
        if menu.price >= 3:
            return Response({'error' 'nuk fshihet objekti '})
        menu.delete()
        return Response({"error": 'objekti u fshi'})
