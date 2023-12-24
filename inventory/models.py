from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=5, decimal_places=2)  
    image_url = models.URLField(blank=True, null=True) 
    recipe_url = models.URLField(blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2) 
    unit = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self) :
        return self.name
    
    
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.menu_item.title} - {self.timestamp}"
    
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE) 
    quantity = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.menu_item.title} - {self.ingredient.name} - {self.quantity}  {self.ingredient.unit}"