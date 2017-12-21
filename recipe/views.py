from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.http import HttpResponseRedirect

from .Form import FoodInput

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

def index(request):
    if request.method == 'POST':
        form = FoodInput(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = FoodInput()
    n = Recipe.objects.order_by('seen')
    x = n[0:4]
    return render(request, 'recipe/home/index.html', {'x' : x, 'form': form})

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/recipe_list/recipe.html', {'recipe': recipe})

def construction(request):
    return render(request, 'recipe/construction/construction.html')
