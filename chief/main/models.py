from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.TextField()
    products = models.ManyToManyField(Product, through='RecipeProduct')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField()

    class Meta:
        verbose_name = 'Продукты в рецепте'

    def __str__(self):
        return self.recipe


class CookedRecipes(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Приготовленные блюда'

    def __str__(self):
        return self.count