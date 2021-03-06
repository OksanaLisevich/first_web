from django.forms import ModelForm
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Author, Book

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


