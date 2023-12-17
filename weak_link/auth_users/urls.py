from django.urls import path

# from weak_link.auth_users.forms import LoginForm
from .views import ChangePasswordView, CustomLoginView, ResetPasswordView, home, RegisterView #, AdsList, AdsAdd
from auth_users.views import CustomLoginView, ResetPasswordView, profile, ChangePasswordView
from django.views.decorators.cache import cache_page
from django.contrib.auth import views as auth_views
from auth_users.forms import LoginForm

urlpatterns = [
    # path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/authorization.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]