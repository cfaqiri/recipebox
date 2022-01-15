from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from recipes.models import Recipe, User


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Making email required
        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "url"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "form-control", "autofocus": "autofocus"})
        self.fields['url'].widget.attrs.update({"class": "form-control"})


class EmailForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({"class": "form-control", "autofocus": "autofocus"})
