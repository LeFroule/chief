from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Recipe, RecipeProduct, Product, CookedRecipes


# Create your views here.
def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    recipe_product.weight = weight
    recipe_product.save()

    return HttpResponse("Продукт успешно добавлен к рецепту")


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe_products = RecipeProduct.objects.filter(recipe=recipe)

    for recipe_product in recipe_products:
        cooked_recipe, created = CookedRecipes.objects.get_or_create(recipe=recipe_product.recipe)
        cooked_recipe.count += 1
        cooked_recipe.save()

    return HttpResponse("Рецепт приготовлен")


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product)
    recipes_less_than_10g = RecipeProduct.objects.filter(product=product, weight__lt=10).values_list('recipe_id',
                                                                                                     flat=True)

    context = {
        'recipes_without_product': recipes_without_product,
        'recipes_less_than_10g': recipes_less_than_10g,
    }

    return render(request, 'recipes_without_product.html', context)
