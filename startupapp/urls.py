from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('course/<str:course_name>', views.course, name='course'),
    path('enroll/', views.enroll, name='enroll'),
    path('candidate_profile/', views.candidate_profile, name='candidate_profile'),
    path('candidate_update/<int:candidate_id>/', views.candidate_update, name='candidate_update'),
    path('attendance/', views.attendance, name='attendance'),
    path('search/', views.search, name='search'),
]
