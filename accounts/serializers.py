from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from scholar_register.models import StudentProfile

class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(request=self.context.get('request'), username = email, password = password)
            if user:
                if user.is_active and user.role == User.STUDENT:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('user is not active or not a student')
            else:
                raise serializers.ValidationError("Unable to login with given credentials")
        else:
            raise serializers.ValidationError("must include email and password")
        
        return data

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentProfile
        fields = "__all__"