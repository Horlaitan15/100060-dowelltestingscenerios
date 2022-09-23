from django.urls import path
from .views import HomePageView,CalendlyPageView,AboutPageView,records_view,WebsocketPermissionView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('recordings/', records_view, name='view_records'),
    path('calendly/', CalendlyPageView.as_view(), name='calendly'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('websocketpermission/', WebsocketPermissionView.as_view(), name='websocketpermission'),
]