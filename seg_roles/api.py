from rest_framework.response import Response #para responder
from .models import Seg_Roles
from .Seriealizers import AXESeriealizers
from rest_framework.decorators import api_view
from rest_framework import status

from django.db import connection

@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def roles_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        roles = Seg_Roles.objects.all() #todos los registros
        roles_serializer = AXESeriealizers(roles, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(roles_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        roles_serializer = AXESeriealizers(data= request.data)#
        
        cod_roles = request.data.get('cod_roles') #Extraemos el codigo del rol, para el que crearemos permosos
        tip_roles = request.data.get('tip_roles')
        des_roles = request.data.get('des_roles')
        if roles_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_ROLES('I', %s,%s,%s)", [cod_roles,tip_roles,des_roles])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Rol creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(roles_serializer.errors)       

        return Response({'message':'¡Ha ocurrido algo inesperado!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def rol_detalle_api_view(request, pk = None): #pk 2
    roles = Seg_Roles.objects.filter(cod_roles = pk).first()  
    if roles:
        if request.method == 'GET':

            roles_serializer = AXESeriealizers(roles)        

            return Response(roles_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_rol = request.data.get('cod_roles')

                #Llamamos el registro a modificar
                roles = Seg_Roles.objects.filter(cod_roles = cod_rol).first() 

                roles_serializer = AXESeriealizers(roles, data = request.data)
                if roles_serializer.is_valid():

                    cod_roles = request.data.get('cod_roles')
                    tip_roles = request.data.get('tip_roles') #no funcion
                    des_roles = request.data.get('des_roles')
                   

                    cursor = connection.cursor()                    
                    cursor.execute("SELECT SP_ROLES('U', %s, %s, %s)", [cod_roles, tip_roles, des_roles])
                    cursor.close() #para cerrar la conexion a base de dato
                    
                    return Response({'message':'¡Rol actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(roles_serializer.errors, status= status.HTTP_400_BAD_REQUEST)