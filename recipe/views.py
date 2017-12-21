from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from itertools import chain

from .Form import FoodInput

def recipe_list(request, c):
    recipes = Recipe.objects.all()
    # checking how many recipes where found
    n = Recipe.objects.all().count()
    # we want 6 recipes per page, this is checking how many pages we have
    n = int(n/6) + 1
    # creating a list so we can itterate over it for the guidance at the bottom of the page
    list = []
    for i in range (0,min(n, 6)):
        list.append(i)
    # finding the recipes that need to be placed on that subpage
    x = int(c)*6 - 6
    y = int(c)*6
    recipes = recipes[x:y]

    # check whether there is a previous Page
    if(int(c) == 1):
         previous = 1
    else:
        previous = int(c)-1

    # check wheter there exists a next Page
    if(int(c) < n):
        next = int(c) + 1
    else:
        next = int(c)
    return render(request, 'recipe/recipe_list/recipe_list.html', {'recipes': recipes, 'list': list, 'previous': previous, 'next': next, 'n': n})

def index(request):
    n = Recipe.objects.order_by('-seen')
    x = n[0:4]
    return render(request, 'recipe/home/index.html', {'x' : x})

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/recipe_list/recipe.html', {'recipe': recipe})

def construction(request):
    return render(request, 'recipe/construction/construction.html')
