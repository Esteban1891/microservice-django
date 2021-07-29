from rest_framework import serializers
from src.hr.models import Direcciones


class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = '__all__'
        #exclude = ('state', 'created_date', 'modified_date', 'deleted_date')