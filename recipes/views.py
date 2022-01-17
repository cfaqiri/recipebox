import os
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from recipes.forms import CustomUserCreationForm, EmailForm, RecipeForm
from recipes.models import Recipe, User


User = get_user_model()


def index(request):
    if request.user.is_authenticated:
        recipes = Recipe.objects.filter(user_id=request.user.id).order_by("title")
        paginator = Paginator(recipes, 36)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "recipes/index.html", {
        "page_obj": page_obj
    })
    return render(request, "recipes/index.html")


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
            new_recipe.save()
            return redirect("index")

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

def test(request):
    return render(request, "recipes/test.html")


def profile(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.get(id=request.user.id)
            user.email = email
            user.save()
            messages.success(request, "Your email has been changed!")
            return redirect("profile")

    else:
        form = EmailForm()
    return render(request, "recipes/profile.html", {"form": form})


def email_change(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.get(id=request.user.id)
            user.email = email
            user.save()
            return HttpResponse(user.email)

    else:
        form = EmailForm()

    return render(request, "recipes/change_email.html", {"form": form})


def get_recipes(request):
    pass


## Understand this thinggggg

class CustomPasswordChangeView(PasswordChangeView):
    # Optional (default: 'registration/password_change_form.html')
    template_name = 'recipes/password_change.html'
    # Optional (default: `reverse_lazy('password_change_done')`)
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed!')
        # Understand what this is doing??
        return super().form_valid(form)


def recipe_details(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, "recipes/recipe_details.html", {"recipe": recipe})