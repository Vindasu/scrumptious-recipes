from django.urls import path

from recipes.views import (
    create_recipe,
    change_recipe,
    show_recipe,
    RecipeListView,
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", show_recipe, name="recipe_detail"),
    path("new/", create_recipe, name="recipe_new"),
    path("edit/", change_recipe, name="recipe_edit"),
]
