from django import forms 
from .models import MenuItem, Purchase, RecipeRequirement, Ingredient


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["title", "price",]
        

class IngridientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "quantity", "unit", "unit_price"]
        
        
class PurchasForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ['timestamp']
        

        
        
class UpdateInventoryForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'unit_price']
        
        
class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ['menu_item', 'ingredient', 'quantity']