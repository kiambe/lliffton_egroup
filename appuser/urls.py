from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from appuser.ussd_views import App_USSD
from .views import *


urlpatterns = [
    #for ussd
    path(f'', App_USSD.as_view(), name="ussd_route"),

    #end for ussd

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

