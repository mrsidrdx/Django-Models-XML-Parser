from django.urls import path
from .views import generateXMLFile

urlpatterns = [
    path('', generateXMLFile, name='generate_xml'),
]
