from src.hr.models import Direcciones
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from src.hr.api.serializers import DireccionesSerializer
from rest_framework import permissions

class DireccionesRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = DireccionesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Direcciones.objects.all()
    lookup_field = "ID_DIRECCION"

    def get_queryset(self):
        username = self.kwargs['ID_DIRECCION']
        return Direcciones.objects.filter(ID_DIRECCION=username)
        #return self.queryset.filter(o





class DireccionesListCreateAPIView(ListCreateAPIView):
    queryset = Direcciones.objects.all()
    serializer_class = DireccionesSerializer



