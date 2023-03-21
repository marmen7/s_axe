
from django.urls import path
from .api import permiso_api_view, permiso_detalle_api_view

urlpatterns = [
    path('seg_permisos/', permiso_api_view, name='permiso'),
    path('seg_permisos/<int:pk>', permiso_detalle_api_view, name='permiso_detalle')
]
