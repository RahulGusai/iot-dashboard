from django.urls import path

from . import views

app_name = 'sensors'
urlpatterns = [
    path('', views.loginPage, name='loginPage'),

    path('authLogin/', views.authenticateLogin.as_view(), name='authenticateLogin'),

    path('dashboard', views.dashboardPage, name='dashboard'),
]
        
