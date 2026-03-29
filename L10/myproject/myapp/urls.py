from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_view, name='form'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
