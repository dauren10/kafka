from rest_framework import serializers
from .models import Companies,Departments,Staff


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
      model = Companies
      fields = ('id', 'label')

class DepartmentsSerializer(serializers.ModelSerializer):
    #options = OptionSerializer(many=True)
    class Meta:
        model = Departments
        fields = ('title','id')


class StaffSerializer(serializers.ModelSerializer):
    dep= DepartmentsSerializer()
    class Meta:
        model = Staff
        fields = ('email','user_id','email','dep_id','dep')


