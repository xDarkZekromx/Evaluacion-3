from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Contacto

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'url', 'nombre', 'telefono', 'correo', 'direccion']

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'url', 'nombre', 'telefono', 'correo', 'direccion']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]