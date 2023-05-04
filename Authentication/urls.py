from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('home/', views.homePage, name='home'),
    path('logout/',views.logoutUser,name='logout'),
    path('user/',views.userPage,name='user'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="authenticate/password_reset.html"), name = "reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name = "password_reset_complete"),
]