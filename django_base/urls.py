"""django_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from users.views import EmailVerification
from dj_rest_auth.registration.views import ResendEmailVerificationView, RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path("social-accounts/", include("allauth.socialaccount.urls")),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
    re_path("signup/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", EmailVerification.as_view(), name='account_confirm_email'),
    path('account-email-verification-sent/', EmailVerification.as_view(), name='account_email_verification_sent'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    # Apps
    path('api/users/', include('users.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
