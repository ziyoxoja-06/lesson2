from .views import HompageView
from django.urls import path
urlpatterns = [
    path('', HompageView.as_view(), name='home')
]