from django.urls import path
from . import views as vw

urlpatterns = [
    path('', vw.home, name='home'),
    path('our-products', vw.services, name='products'),
    # path('terms', vw.terms, name='terms'),
    # path('return-ploicy', vw.returnPolicy, name='return_policy'),
    # path('design', vw.mockup, name='design'),
]
