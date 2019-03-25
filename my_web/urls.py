from . import views
from django.conf.urls import include, url
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.main),
    url(r'resume/$', views.resume),
    url(r'^register', views.RegisterFormView.as_view()),
    url(r'^login', views.LoginFormView.as_view()),
    url(r'^logout', views.LogoutView.as_view()),
    url(r'^validate-email' , views.validate_email),
    url(r'^add-book/' , views.add_book),
    url(r'^add-author/', views.add_author),
    url(r'^delete/([\d])', views.destroy),
    url(r'^edit/([\d])', views.edit),
    url(r'^update/([\d])', views.update),

]
