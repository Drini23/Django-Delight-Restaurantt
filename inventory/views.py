from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView 
from django.views.generic.edit import DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import  MenuItem, Ingredient, Purchase, RecipeRequirement
from django.contrib.auth.models import User

from .forms import * 


# Create your views here.


def home(request):
    return render(request, 'inventory/home.html')


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm()
    return render(request, 'inventory/add_menu_item.html', {"form": form})



def add_ingredient(request):
    if request.method == 'POST':
        form = IngridientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IngridientForm()
    return render(request, 'inventory/add_ingredient.html', {'form': form})


def add_recipe(request):
    if request.method =='POST':
        form = RecipeRequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeRequirementForm()
    return render(request, 'inventory/add_recipe.html', {"form":form})


def record_purchase(request):
    if request.method =='POST':
        form = PurchasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = PurchasForm()
    return render(request, 'inventory/record.html', {"form":form})


def update_inventory(request, id):
    ingredient = get_object_or_404(Ingredient, pk=id)
    
    if request.method == 'POST':
        form = UpdateInventoryForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('add_menu_item')
    else:
        form = UpdateInventoryForm(instance=ingredient)
    
    return render(request, 'inventory/update_inventory.html', {"form": form})


class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    
    
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'
    
    
class DeleteIngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'inventory/delete_ingredient.html'
    success_url = reverse_lazy('add_menu_item')
    

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    context_object_name = 'purchases'
    
    
class ProfitRevenueView(TemplateView):
    template_name = 'inventory/profit_revenue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = Purchase.objects.all()
        total_revenue = sum(purchase.menu_item.price for purchase in purchases)
        total_cost = sum(RecipeRequirement.objects.filter(menu_item=purchase.menu_item).first().ingredient.unit_price * RecipeRequirement.objects.filter(menu_item=purchase.menu_item).first().quantity for purchase in purchases if RecipeRequirement.objects.filter(menu_item=purchase.menu_item).exists())
        total_profit = total_revenue - total_cost
        context['profit'] = total_profit
        context['revenue'] = total_revenue
        return context
    
class RecipeRequirementListView(ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_list.html'
    
def login_page(request):
    page = 'login'
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User dose not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User name dose not exist')
    context = {'page': page}
    return render(request, 'inventory/login_register.html', context)
    
def logout_page(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred registration ')
            
    return render(request, 'inventory/login_register.html', {'form': form})



