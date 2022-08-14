
from rest_framework import serializers
from .models import* 

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Division
        fields=["serial","english_name","bangla_name","website"]

        
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields=["serial","english_name","bangla_name","latitude","longititude","website"]

class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upazila
        fields=["serial","english_name","bangla_name","website"]

class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Union
        fields=["serial","english_name","bangla_name","website"]
