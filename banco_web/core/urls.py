from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


USER_URLS = [
    path('login', auth_views.login, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path(
        'logout',
        auth_views.LogoutView.as_view(
            template_name='registration/logout.html'
        ),
        name='logout'
    ),
]

urlpatterns = [
    path('', views.home, name='home'),
] + USER_URLS
