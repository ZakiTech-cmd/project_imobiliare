from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('announce_details/<int:id>/', views.announce_details, name='announce_details'),
    path('my_announces/', views.my_announces, name='my_announces'),
    path('create_announce/', views.createAnnounce, name='create_announce'),
    path('update_announce/<int:id>/', views.updateAnnounce, name='update_announce'),
    path('delete_announce/<int:id>/', views.deleteAnnounce, name='delete_announce'),
    path('search', views.searchAnnounce, name='search_announce')
]