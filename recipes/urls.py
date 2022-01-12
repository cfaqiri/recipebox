from django.contrib.auth import views as auth_views
from django.urls import path

from recipes import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("add/", views.add_recipe, name="add_recipe"),
    path("search/", views.search, name="search"),
    path("<int:user_id>/recipes/", views.my_recipes, name="my_recipes"),
    path("password_reset/",
        auth_views.PasswordResetView.as_view(template_name="recipes/password_reset_form.html"),
        name="password_reset"),
    path("password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="recipes/password_reset_done.html"),
        name="password_reset_done"),
    path("password_reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="recipes/password_reset_confirm.html"),
        name="password_reset_confirm"),
    path("password_reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="recipes/password_reset_complete.html"),
        name="password_reset_complete")
]