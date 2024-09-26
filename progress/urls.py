from django.urls import path
from . import views

appname ="progress"
urlpatterns = [
    path('',views.progress_view,name = "progress_view")
]