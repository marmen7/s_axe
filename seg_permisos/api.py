from rest_framework.response import Response #para responder
from .models import seg_permisos
from .serializers import PermisosSerializer
from rest_framework.decorators import api_view
from rest_framework import status

from django.db import connection

@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def permiso_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        permisos = seg_permisos.objects.all() #todos los registros
        permisos_serializer = PermisosSerializer(permisos, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(permisos_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        request.data['cod_permisos'] = 0 #
        permiso_serializer = PermisosSerializer(data= request.data)#
        
        cod_rol = request.data.get('cod_rol') #Extraemos el codigo del rol, para el que crearemos permosos

        if permiso_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_PERMISOS_INS_UPD('I', %s)", [cod_rol])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Usuario creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(permiso_serializer.errors)       

        return Response({'message':'¡Ha ocurrido algo inesperado!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def permiso_detalle_api_view(request, pk = None): #pk 2
    permiso = seg_permisos.objects.filter(cod_permisos = pk).first()  
    if permiso:
        if request.method == 'GET':

            permisos_serializer = PermisosSerializer(permiso)        

            return Response(permisos_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_permiso = request.data.get('cod_permisos')

                #Llamamos el registro a modificar
                permiso = seg_permisos.objects.filter(cod_permisos = cod_permiso).first() 

                permiso_serializer = PermisosSerializer(permiso, data = request.data)
                if permiso_serializer.is_valid():

                    cod_permiso = request.data.get('cod_permisos')
                    cod_rol = request.data.get('cod_rol') #no funcion
                    pr_insercion = request.data.get('per_insercion')
                    pr_actualizar = request.data.get('per_actualizar')
                    pr_consultar = request.data.get('per_consultar')

                    cursor = connection.cursor()                    
                    cursor.execute("SELECT SP_PERMISOS_INS_UPD('U', %s, %s, %s, %s, %s)", [cod_rol, cod_permiso, pr_insercion, pr_actualizar, pr_consultar])
                    cursor.close() #para cerrar la conexion a base de dato
                    
                    return Response({'message':'¡Usuario actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(permiso_serializer.errors, status= status.HTTP_400_BAD_REQUEST)