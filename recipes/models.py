from django.db import models

# one
# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True)
    created = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return f"{self.name}  by {self.author}"


# many


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ingredients",
        on_delete=models.CASCADE,
    )
    measure = models.ForeignKey("Measure", on_delete=models.PROTECT)
    food = models.ForeignKey("FoodItem", on_delete=models.PROTECT)


class Step(models.Model):
    order = models.SmallIntegerField()
    directions = models.TextField()

    recipe = models.ForeignKey(
        "Recipe",
        related_name="steps",
        on_delete=models.CASCADE,
    )
    food_items = models.ManyToManyField(
        "recipes.FoodItem", null=True, blank=True
    )

    def __str__(self):
        return self.recipe.name
