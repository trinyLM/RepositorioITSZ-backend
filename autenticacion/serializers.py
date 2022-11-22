from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from .models import CustomUser
# ...

#from rest_framework.authtoken.models import Token


from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from django.contrib.auth import authenticate



#serializador para el registro de nuevos usuarios
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True,)
    
    def validate_password(self, value):
        return make_password(value)
    class Meta:
        model = CustomUser
        fields = ('username','email', 'password', 'matricula', "first_name",
                  "last_name", 'apellido_materno')
        extra_kwargs = {
            'matricula': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def validate(self, attrs):
        if not attrs['email'].endswith("zongolica.tecnm.mx"):
            raise serializers.ValidationError({"email": "solo se aceptan correos instucionales"})
        return attrs
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data["password"],
            matricula=validated_data['matricula'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            apellido_materno=validated_data['apellido_materno']
        )

        
        user.set_password(validated_data['password'])
        user.save()
        return user

    



#Serializador para reliazar login
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Correo o contraseña incorrectas.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs