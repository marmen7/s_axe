
#TABLA PERSON_EMAILES API (Marleny)
from email.message import EmailMessage
from rest_framework.response import Response #para responder
from .models import Person_Emailes, Person_Telefonos
from .serializers import EmailesSerializers, TelefonosSerializers
from rest_framework.decorators import api_view
from rest_framework import status

from django.db import connection

@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def emailes_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        emailes = Person_Emailes.objects.all() #todos los registros
        emailes_serializer = EmailesSerializers(emailes, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(emailes_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        emailes_serializer = EmailesSerializers(data= request.data)#
        
        cod_email = request.data.get('cod_email')
        dir_correo= request.data.get('dir_correo') #no funcion
        des_correo = request.data.get('des_correo')
        
        if emailes_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_PERSON_EMAILES('I', %s,%s,%s)", [cod_email, dir_correo, des_correo, ])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Email creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(emailes_serializer.errors)       

        return Response({'message':'¡Error al ingresar Email!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def email_detalle_api_view(request, pk = None): #pk 2
    emailes = Person_Emailes.objects.filter(cod_email = pk).first()  
    if emailes:
        if request.method == 'GET':

            emailes_serializer = EmailesSerializers(emailes)        

            return Response(emailes_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_correo = request.data.get('cod_email')

                #Llamamos el registro a modificar
                emailes = Person_Emailes.objects.filter(cod_email = cod_correo).first() 

                emailes_serializer = EmailesSerializers(emailes,data = request.data)
                if emailes_serializer.is_valid():

                 cod_email = request.data.get('cod_email')
                 dir_correo= request.data.get('dir_correo') #no funcion
                 des_correo = request.data.get('des_correo')
                       
                   

                 cursor = connection.cursor()                    
                 cursor.execute("SELECT SP_PERSON_EMAILES('U', %s, %s, %s)", [cod_email, dir_correo, des_correo])
                 cursor.close() #para cerrar la conexion a base de dato
                    
                 return Response({'message':'¡Email actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
        else:
                 return Response(emailes_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


#API PERSON TELEFONOS(Marleny)
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def telefonos_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        telefonos = Person_Telefonos.objects.all() #todos los registros
        telefonos_serializer = TelefonosSerializers(telefonos, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(telefonos_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_telefono']  #
        telefonos_serializer = TelefonosSerializers(data= request.data)#
        
        cod_telefono = request.data.get('cod_telefono')
        num_telefono = request.data.get('num_telefono') #no funcion
        tip_telefono = request.data.get('tip_telefono')

        if telefonos_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_PERSON_TELEFONOS('I', %s,%s,%s)", [cod_telefono, num_telefono, tip_telefono])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Telefono creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(telefonos_serializer.errors)       

        return Response({'message':'¡Error al ingresar telefono!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def telefonos_detalle_api_view(request, pk = None): #pk 2
    telefonos = Person_Telefonos.objects.filter(cod_telefono = pk).first()  
    if telefonos:
        if request.method == 'GET':

            telefonos_serializer = TelefonosSerializers(telefonos)        

            return Response(telefonos_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_telefonos = request.data.get('cod_telefono')

                #Llamamos el registro a modificar
                telefonos = Person_Telefonos.objects.filter(cod_telefono = cod_telefonos).first() 

                telefonos_serializer = TelefonosSerializers(telefonos, data = request.data)
                if telefonos_serializer.is_valid():

                    cod_telefono = request.data.get('cod_telefono')
                    num_telefono = request.data.get('num_telefono') #no funcion
                    tip_telefono = request.data.get('tip_telefono') 

                    cursor = connection.cursor()                    
                    cursor.execute("SELECT  SP_PERSON_TELEFONOS('U', %s, %s, %s)", [cod_telefono, num_telefono, tip_telefono])
                    cursor.close() #para cerrar la conexion a base de dato
                    
                    return Response({'message':'¡Telefono actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(telefonos_serializer.errors, status= status.HTTP_400_BAD_REQUEST)