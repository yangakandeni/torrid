from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

from .views import dashboard, register

# app_name = "account"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("password/change/", PasswordChangeView.as_view(), name="password_change"),
    path("password/change/success/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
