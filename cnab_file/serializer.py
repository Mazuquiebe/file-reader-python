from rest_framework import serializers
from .models import CNABData

class CNABDataSerializer(serializers.ModelSerializer):

    class Meta:

        model  = CNABData
        fields = [
            "id",
            "type",
            "date",  
            "value", 
            "cpf",
            "card",  
            "owner", 
            "store",
        ]


    def create(self, validated_data:dict) -> CNABData:
        return CNABData.objects.create(**validated_data)



