from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('registrar/', views.registrar),
    path('login/', LoginView.as_view(template_name = "login.html")),
    path('logout/', LogoutView.as_view(template_name = "logout.html")),
]