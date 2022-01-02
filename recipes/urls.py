from django.urls import path

from recipes import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.add_recipe, name="add_recipe"),
    path("<int:user_id>/recipes", views.my_recipes, name="my_recipes")
]