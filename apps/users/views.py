from utils.permissions import funcpermission
from .serializers import PermissionSerializer, RoleSerializer
from .models import Permission, Roles
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
import random

class UserDetailListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        user_list = User.objects.all()
        serializer = UserSerializer(user_list,many=True)
        return Response(serializer.data)

    def post(self,request):
    # Obter os valores de firstName e lastName do request
        first_name = request.data.get('firstName', '')
        last_name = request.data.get('lastName', '')

        # Concatenar os valores para formar o nome completo
        request.data['name'] = f"{first_name} {last_name}"
        request.data['role'] = [{'display': 'cliente'}]

        # Prefixo do número de telefone para Angola
        prefix = "+2449"
        
        # Gerar os 8 dígitos aleatórios restantes
        suffix = ''.join(random.choices('0123456789', k=8))
        
        # Concatenar prefixo e sufixo para formar o número completo
        phone_number = prefix + suffix

        request.data['mobile'] = phone_number
        print('-------------------------------------------------->')
        print(request.data)
        print('-------------------------------------------------->')

        # Print para depuração (opcional)
        print(request.data['name'])
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CreatePermissionForRoleView(APIView):
    def post(self, request, *args, **kwargs):
        role_serializer = RoleSerializer(data=request.data['role'])
        permission_serializer = PermissionSerializer(data=request.data['permission'])

        if role_serializer.is_valid() and permission_serializer.is_valid():
            role_instance = role_serializer.save()
            permission_instance = permission_serializer.save()

            role_instance.permissions.add(permission_instance)

            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': role_serializer.errors, 'permission_errors': permission_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class AssignPermissionToRoleView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            role_instance = Roles.objects.get(pk=request.data['role_id'])
            permission_instance = Permission.objects.get(pk=request.data['permission_id'])

            role_instance.permissions.add(permission_instance)

            return Response({'success': True}, status=status.HTTP_200_OK)
        except Roles.DoesNotExist:
            return Response({'error': 'Role not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Permission.DoesNotExist:
            return Response({'error': 'Permission not found.'}, status=status.HTTP_404_NOT_FOUND)



class SomeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        codename = 'partient'  # Substitua isso pelo codename desejado
        if funcpermission(request.user, codename):
            # O usuário possui a permissão, continue com a lógica da view
            return Response({"message": "Usuário tem permissão para acessar esta visualização."})
        else:
            # O usuário não possui a permissão, retorne uma resposta de não autorizado
            return Response({"message": "Usuário não tem permissão para acessar esta visualização."}, status=status.HTTP_403_FORBIDDEN)