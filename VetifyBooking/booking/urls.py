
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('booking/', views.booking_view, name='booking'),
    path('appointments/', views.appointments_view, name='appointments'),

    path('register-pet/', views.register_pet_view, name='register_pet'),
    path('edit-pet/<int:pet_id>/', views.edit_pet_view, name='edit_pet'),
    path('delete-pet/<int:pet_id>/', views.delete_pet_view, name='delete_pet'),
    path('documents/', views.documents_view, name='documents'),
    
    path('services-schedules/', views.services_schedules_view, name='services_schedules'),
    # URLs del perfil
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/avatar/', views.update_avatar, name='update_avatar'),
    path('pet/<int:pet_id>/edit/', views.edit_pet, name='edit_pet'),
    path('pet/<int:pet_id>/delete/', views.delete_pet, name='delete_pet'),
    path("change-password/",auth_views.PasswordChangeView.as_view(template_name="booking/change_password.html",success_url=reverse_lazy("profile")),name="change_password"),
    path('change-password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),name='password_change_done'),
]

