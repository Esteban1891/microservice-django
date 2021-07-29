from django.urls import path 
from src.hr.api.api import DireccionesListCreateAPIView,  DireccionesRetrieveDestroyAPIView


urlpatterns = [
    #path('direccionesRetrieve/<DIRECCION>/',  DireccionesRetrieveDestroyAPIView.as_view(), name = 'district'),
    path('direccionesObtains/<DIRECCION>/',  DireccionesListCreateAPIView.as_view(), name = 'district'),

]


