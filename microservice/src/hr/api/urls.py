from django.urls import path 
from src.hr.api.api import DireccionesListCreateAPIView,  DireccionesRetrieveDestroyAPIView


urlpatterns = [
    path('direccionesRetrieve/<ID_DIRECCION>/',  DireccionesRetrieveDestroyAPIView.as_view(), name = 'district'),
    path('direccionesObtains/',  DireccionesListCreateAPIView.as_view(), name = 'district'),

]


