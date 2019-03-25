from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import UserCreateForm, BookForm, AuthorForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic.base import View
from django.contrib.auth import logout
from .models import Author, Book
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.db import models



# Create your views here.

def resume(request):
    return render(request, 'resume.html')

class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/my-web/login"

    template_name = "register.html"

    def form_valid(self , form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/my-web/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/my-web/")

def validate_email(request):
    if request.GET:
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            data  = {
                "is_taken" : "На этот почтовый ящик уже зарегистрирован пользователь!"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'ok': "На этот почтовый адрес не было регистраций"})


def main(request):
    book_form = BookForm
    author_form = AuthorForm
    all_books = Book.objects.all()
    if request.POST:
        query = request.POST['search']
        result_list  = Book.objects.filter(title__contains=query)
        if result_list.count() != 0:
            context = {
                'all_books': all_books,
                'result_list': result_list,
                'query': query,
                'book_form': book_form,
                'author_form': author_form,
            }
        else:
            context ={
                'all_books': all_books,
                'empty': "Совпадений не найдено!",
                'query': query,
            }
    else:
        context ={
                'all_books': all_books,
                'book_form': book_form,
                'author_form': author_form,
                }
    return render(request , 'home.html' , context)


@csrf_exempt
def add_book(request):
    book_form = BookForm
    if request.POST:
        book_form = BookForm(request.POST)
        if book_form.is_valid:
            book_form.save()
            return redirect("/my-web")  
        else:
            book_form = BookForm()
    return redirect("/my-web")


@csrf_exempt
def add_author(request):
    author_form = AuthorForm
    if request.POST:
        author_form = AuthorForm(request.POST)
        if author_form.is_valid:
            author_form.save()
            return redirect("/my-web")  
        else:
            author_form = AuthorForm()
    return redirect("/my-web")


def destroy(request, id):  
    book = Book.objects.get(id=id)  
    book.delete()  
    return redirect("/my-web")


def edit(request, id):  
    book = Book.objects.get(id=id) 
    book_form = BookForm
    ctx = {
        'book': book,
        'book_form': book_form,
        }
        
    return render(request,'edit.html', ctx)

def update(request, id):
    book_form = BookForm
    book = Book.objects.get(id=id)  
    form = BookForm(request.POST, instance = book)  
    if form.is_valid():  
        form.save()  
        return redirect("/my-web")  
    ctx = {
        'book': book,
        'book_form': book_form,
        }
    return render(request, 'edit.html', ctx) 