from rest_framework import serializers
from . models import approvols

class approvalsSerializers(serializers.ModelSerializer):
    class Meta:
        model = approvols
        fields = '__all__'