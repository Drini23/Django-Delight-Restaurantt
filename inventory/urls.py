from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("inventory/", views.add_menu_item, name='add_menu_item'),
    path("ingredient/", views.add_ingredient, name='add_ingredient'),
    path("recipe/", views.add_recipe, name='recipe'),
    path("record/", views.record_purchase, name="record"),
    path('update_inventory/<int:id>/', views.update_inventory, name='update_inventory'),
    
    
    path('menu/', views.MenuItemListView.as_view(), name='menu'),
    path('ingredient_list/', views.IngredientListView.as_view(), name='ingredient'),
    path('ingredients/<int:pk>/delete/', views.DeleteIngredientDeleteView.as_view(), name='ingredient-delete'),
    path('purchase/', views.PurchaseListView.as_view(), name='purchase'),
    path('recipe_list/', views.RecipeRequirementListView.as_view(), name='recipe_list'),
    path('profit_revenue/', views.ProfitRevenueView.as_view(), name='profit'),
    
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.registerPage, name='register')
]