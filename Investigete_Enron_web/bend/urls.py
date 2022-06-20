from django.urls import path

from . import views

app_name = 'bend'

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('result/<int:pk>', views.result, name='results'),
    path('autofill/', views.autofill, name='autofill'),
]

