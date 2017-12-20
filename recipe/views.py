from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    n = Recipe.objects.all().count()
    n = int(n/6) + 1
    x = 0
    y = 6
    list = []
    for i in range (0,min(n, 6)):
        list.append(i)
    recipes = Recipe.objects.all()[x:y]
    return render(request, 'recipe/recipe_list/recipe_list.html', {'recipes': recipes, 'list': list, 'n': n})
