from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from itertools import chain
from django.urls import reverse

from .Form import FoodInput

def recipe_list(request, c):
    form = request.session['form']
    # requesting all the variables
    vegetarien = form["vegetarien"]
    vegetable = form["vegetables"]
    meat = form["meat"]
    z = int(c)
    # finding the corrsponding recipes
    # splitting up all the different ingredients
    vegetables = vegetable.split(', ')
    meats = meat.split(', ')
    #checking the Dietary characterization
    recipes = Recipe.objects.none()
    if(int(vegetarien) == 1):
        for vegetable in vegetables:
            recipes = recipes.union(Recipe.objects.filter(vegetables__icontains=vegetable))
        for meat in meats:
            recipes = recipes.union(Recipe.objects.filter(meat__icontains=meat))
    elif(int(vegetarien) == 2):
        for meat in meats:
            recipes = recipes.union(Recipe.objects.filter(meat__icontains=meat))
    elif(int(vegetarien) == 3):
        for vegetable in vegetables:
            recipes = recipes.union(Recipe.objects.filter(vegetables__icontains=vegetable))
    # checking how many recipes where found
    n = recipes.count()
    # we want 6 recipes per page, this is checking how many pages we have
    n = int(n/6) + 1
    # creating a list so we can itterate over it for the guidance at the bottom of the page
    list = []
    for i in range (0,min(n, 6)):
        list.append(i)
    # finding the recipes that need to be placed on that subpage
    x = z*6 - 6
    y = z*6
    recipes = recipes[x:y]
    # check whether there is a previous Page
    if(z == 1):
         previous = 1
    else:
        previous = z-1

    # check wheter there exists a next Page
    if(z < n):
        next = z + 1
    else:
        next = z
    return render(request, 'recipe/recipe_list/recipe_list.html', {'recipes': recipes, 'list': list, 'previous': previous, 'next': next, 'n': n})

def index(request):
    if request.method == 'POST':
        form = FoodInput(request.POST)
        if form.is_valid():
            vegetarien = form.cleaned_data['vegetarien']
            vegetables = form.cleaned_data['vegetables']
            meat = form.cleaned_data['meat']
            request.session['form'] = {'vegetarien':vegetarien, 'vegetables':vegetables, 'meat':meat}
            return redirect('recipe_list', c=1)
    else:
        form = FoodInput()
    n = Recipe.objects.order_by('-seen')
    x = n[0:4]
    return render(request, 'recipe/home/index.html', {'x' : x, 'form': form})

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/recipe_list/recipe.html', {'recipe': recipe})

def construction(request):
    return render(request, 'recipe/construction/construction.html')
