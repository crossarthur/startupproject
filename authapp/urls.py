from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handle_login, name='handle_login'),
    path('logout/', views.handle_logout, name='handle_logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
