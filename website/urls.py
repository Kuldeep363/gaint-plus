from django.urls import path
from . import views as vw

urlpatterns = [
    path('', vw.home, name='home'),
    path('our-products', vw.services, name='products'),
    # path('design', vw.mockup, name='design'),
]
