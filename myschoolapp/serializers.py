from rest_framework import serializers
from .models import School, Grade, Teacher, Subjects, Student
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .views import *

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'address', 'email', 'capacity']

class GradeSerializer(serializers.ModelSerializer):
    # Display the school name instead of its ID
    school = serializers.SlugRelatedField(slug_field='name', queryset=School.objects.all())
    
    class Meta:
        model = Grade
        fields = ['id', 'name', 'school']

class TeacherSerializer(serializers.ModelSerializer):
    # Display the grade name instead of its ID
    grade = serializers.SlugRelatedField(slug_field='name', queryset=Grade.objects.all())

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'age', 'gender', 'grade']

    # def get_gender(self, obj):
    #     return dict(Teacher.GENDER_CHOICES).get(obj.gender, "Unknown")

class SubjectSerializer(serializers.ModelSerializer):
    # Display the grade name instead of its ID
    grade = serializers.SlugRelatedField(slug_field='name', queryset=Grade.objects.all())
    
    class Meta:
        model = Subjects
        fields = ['id', 'name', 'grade']

class StudentSerializer(serializers.ModelSerializer):
    # Display the grade name instead of its ID
    grade = serializers.SlugRelatedField(slug_field='name', queryset=Grade.objects.all())
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'gender', 'grade']

    def get_gender(self, obj):
        return dict(Student.GENDER_CHOICES).get(obj.gender, "Unknown")



# customized login
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the token
        token['email'] = user.email
        token['username'] = user.username

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Include user-specific data in the response
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return data
