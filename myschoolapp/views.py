from . models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from . serializers import *
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


@permission_classes([IsAuthenticated])  # Enforce authentication for all methods
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])  # List of allowed HTTP methods
    def api(request, id=None):
        # Handle GET requests
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'error': 'Object not found'}, status=404)
            else:
                instances = model_class.objects.all()
                serializer = serializer_class(instances, many=True)
                return Response(serializer.data)

        # Handle POST requests
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)  # Return 201 for created resource
            return Response(serializer.errors, status=400)  # Return 400 for invalid data

        # Handle PUT requests
        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=400)
                except model_class.DoesNotExist:
                    return Response({'error': 'Object not found'}, status=404)
            return Response({'error': 'ID is required for updating'}, status=400)

        # Handle DELETE requests
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'}, status=204)
                except model_class.DoesNotExist:
                    return Response({'error': 'Object not found'}, status=404)
            return Response({'error': 'ID is required for deleting'}, status=400)

    return api





manage_school = generic_api(School, SchoolSerializer)
manage_subjects = generic_api(Subjects, SubjectSerializer)
manage_grade= generic_api(Grade, GradeSerializer)
manage_teacher= generic_api(Teacher, TeacherSerializer)
manage_student= generic_api(Student, StudentSerializer)
        

# customized login
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer