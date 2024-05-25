from django.urls import path
from . import views

# urls path are created here 
urlpatterns = [
    path('', views.survey_view, name='survey'),
    path('preference/<str:id>/', views.survey_view_pre, name='preference')
]
