from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_register, name='login'),
    path('announce_details/<int:id>/', views.announce_details, name='announce_details')
]