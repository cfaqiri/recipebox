from django import forms 
from django.forms import ModelForm

from recipes.models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "url"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "form-control", "autofocus": "autofocus"})
        self.fields['url'].widget.attrs.update({"class": "form-control"})