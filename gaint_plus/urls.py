from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
   
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    prefix_default_language=True,
) +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('website.urls')),
#     # prefix_default_language=False,
#  ] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 'django-insecure-+sh4+)77v(bv(atm-)=_^4bhu@u%tw!j04#2xs847sz)*l&v+6'