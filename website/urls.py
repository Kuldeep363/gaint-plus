from django.urls import path
from . import views as vw

urlpatterns = [
    # path('', vw.home, name='home'),
    path('design', vw.mockup, name='design'),
]
