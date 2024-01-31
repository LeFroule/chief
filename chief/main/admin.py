from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]


class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'product', 'weight')


admin.site.register(Product)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeProduct, RecipeProductAdmin)
