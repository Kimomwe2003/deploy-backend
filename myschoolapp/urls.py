from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [

    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('school/', manage_school),
    path('school/<int:id>/', manage_school),

    path('grade/', manage_grade),
    
    path('grade/<int:id>/', manage_grade),

    path('students/', manage_student),
    path('students/<int:id>/', manage_student),


    path('teacher/', manage_teacher),
    path('teacher/<int:id>/', manage_teacher),

    path('subjects/', manage_subjects),
    path('subjects/<int:id>/', manage_subjects),



]
