from django.urls import path
#from apps.users.api.api import UserAPIView
from .api import emailes_api_view, email_detalle_api_view
from .api import telefonos_api_view, telefonos_detalle_api_view


urlpatterns = [
    path('datos/', emailes_api_view, name='emailes'),
    path('datos/<int:pk>', email_detalle_api_view, name='email_detalle'),
    path('telefonos/', telefonos_api_view, name='telefonos'),
    path('telefonos/<int:pk>', telefonos_detalle_api_view, name='telefonos_detalle')
    #path('usuario/', UserAPIView.as_view(), name='usuario_api')
]
