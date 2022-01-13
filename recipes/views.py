import os
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from recipes.forms import CustomUserCreationForm, RecipeForm
from recipes.models import Recipe, User


User = get_user_model()


def index(request):
    return render(request, "recipes/index.html")


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             # Change this
#             return HttpResponse("you don't even exist")
    
#     return render(request, "recipes/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        return render(request, "recipes/register.html", {"form": form})
    else:
        form = CustomUserCreationForm()
        return render(request, "recipes/register.html", {"form": form})



def add_recipe(request):
    if request.method == "POST":
        f = RecipeForm(request.POST)
        if f.is_valid():
            new_recipe = f.save(commit=False)
            new_recipe.user = User.objects.get(id=request.user.id)
        # I need to find a way for this NOT to be null, but for the form to still go through.
            new_recipe.save()
            return HttpResponseRedirect(reverse("my_recipes", args=[request.user.id]))

    recipe_form = RecipeForm()
    return render(request, "recipes/add_recipe.html", {
        "recipe_form": recipe_form
    })


@login_required
def my_recipes(request, user_id):
    recipes = Recipe.objects.filter(user_id=user_id).order_by("title")
    paginator = Paginator(recipes, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "recipes/my_recipes.html", {
        "page_obj": page_obj
    })


@login_required
def search(request):
    if request.method == "POST":
        search = request.POST["search"]
        recipes = Recipe.objects.all()
        filtered_recipes = []
        for recipe in recipes:
            if search.lower() in recipe.title.lower():
                filtered_recipes.append(recipe)
        paginator = Paginator(filtered_recipes, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # Maybe change this to be rendered by Javascript
        return render(request, "recipes/my_recipes.html", {"page_obj": page_obj})