
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import*
from .models import*


def make_json(queryset,language):
        payload=[]
        district=False 
        for query in queryset:
            if language=="en":name=query.english_name 
            else:name=query.bangla_name 
            try:
                if query.latitude:district=True 
            except:district=False 
            if district:
                payload.append({
                    "id":query.serial,
                    "name":name,
                    "latitude":query.latitude,
                    "longititude":query.longititude,
                    "website":query.website,
    
                })
            else:
                payload.append({
                    "id":query.serial,
                    "name":name,
                    "website":query.website,
        
                })

            
           
        return payload
     
class DivisionView(APIView):
    def get(self,request,format=None):
        queryset = Division.objects.all()
        serializer = DivisionSerializer(queryset, many=True)
        return Response(serializer.data)

class DistrictView(APIView):
    def get(self,request,division_id):
        queryset = District.objects.filter(division__serial=division_id)
        serializer = DistrictSerializer(queryset, many=True)
        return Response(serializer.data)

class UpazilaView(APIView):
    def get(self,request,district_id):
        queryset=Upazila.objects.filter(district__serial=district_id)
        serializer=UpazilaSerializer(queryset,many=True)
        return Response(serializer.data)
        
class UnionView(APIView):
    def get(self,request,upazila_id,format=None):
        queryset=Union.objects.filter(upazila__serial=upazila_id)
        serializer=UnionSerializer(queryset,many=True)
        return Response(serializer.data)

    