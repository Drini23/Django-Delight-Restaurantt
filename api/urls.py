from django.urls import path 
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('menu', views.MenuViewSet )
router.urls
urlpatterns=router.urls

"""
urlpatterns = [
    path('menu', views.menu_item),
    path('menu/<int:pk>/', views.menu_detail)
] """