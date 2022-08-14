from django.urls import path
from . import views as vw

urlpatterns = [
    path('', vw.home, name='home'),
    path('services', vw.services, name='services'),
    path('design', vw.mockup, name='design'),
]
