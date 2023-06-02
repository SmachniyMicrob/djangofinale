from django.forms import ModelForm
from . import models


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = {'name', 'product_type'}


class RecipeForm(ModelForm):
    class Meta:
        model = models.Recipe
        fields = {'product', 'dish', 'quantity'}


class ProductTypeForm(ModelForm):
    class Meta:
        model = models.ProductType
        fields = {'name'}


class DishForm(ModelForm):
    class Meta:
        model = models.Dish
        fields = {'name', 'products'}
