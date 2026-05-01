from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.show_exam, name='exam'),
    path('submit/', views.submit, name='submit'),
    path('result/<int:submission_id>/', views.show_exam_result, name='result'),
]
