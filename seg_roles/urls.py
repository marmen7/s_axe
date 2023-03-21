from django.urls import path
#from apps.users.api.api import UserAPIView
from .api import roles_api_view, rol_detalle_api_view

urlpatterns = [
    path('seg_roles/', roles_api_view, name='roles'),
    path('seg_roles/<int:pk>', rol_detalle_api_view, name='rol_detalle')
    #path('usuario/', UserAPIView.as_view(), name='usuario_api')
]
