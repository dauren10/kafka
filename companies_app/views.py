from yaml import serialize
from companies_app.models import Companies,Staff,Departments
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .serializers import StaffSerializer,CompaniesSerializer,DepartmentsSerializer


class StaffListView(APIView):
    def get(self,format=None):
        items=Staff.objects.all()
        serializer=StaffSerializer(items,many=True)
        return Response(serializer.data)

# class EntryDetailView(APIView):
#     def get(self,request,pk,format=None):
#         item=Datatables.objects.get(id=pk)
#         serializer=DataSerializer(item)
#         return Response(serializer.data)

