from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_user/', views.add_user, name='add_user'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_record/', views.add_record, name='add_record'),
    path('view_record/<int:record_id>/', views.view_record, name='view_record'),
    path('edit_record/<int:record_id>/', views.edit_record, name='edit_record'),
    path('delete_record/<int:record_id>/', views.delete_record, name='delete_record'),
    path('search/', views.search, name='search'),
    path('error/', views.error, name='error'),
]