from django.contrib.auth import views as auth_views
from django.urls import path

from recipes import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.add_recipe, name="add_recipe"),
    path("search", views.search, name="search"),
    path("<int:user_id>/recipes", views.my_recipes, name="my_recipes"),
    path("password-reset",
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="password_reset")

]