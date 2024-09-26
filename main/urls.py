from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('thankyou/', views.thankyou, name='thankyou'),  # Ensure trailing slash here
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('accounts/', include('accounts.urls')),  # Account registration URLs
    path('auth/', include('authentications.urls')), # Login URLs
    path('progress/',include('progress.urls')),
    path('activity/',include('activity.urls')),
]
