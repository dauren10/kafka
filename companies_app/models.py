from statistics import mode
from django.db import models

from datetime import datetime
# Create your models here.


class Companies(models.Model):
    title=models.CharField(max_length=100)
    bin=models.BigIntegerField(unique=True)
    created_by=models.IntegerField()
    created_date=models.DateField(default=datetime.now)
    updated_date=models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

class Departments(models.Model):
    title=models.CharField(max_length=100)
    #in case foreignKey _id generated automatically
    parent=models.ForeignKey('self',blank=True, null=True,on_delete=models.SET_NULL)
    company=models.ForeignKey(Companies,null=True,on_delete=models.SET_NULL)
    created_by=models.IntegerField()
    created_date=models.DateField(default=datetime.now)
    updated_date=models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

class Staff(models.Model):
    ROLES=(
        (1, 'Personal'),
        (2, 'Corp'),
        (3, 'Emp'),
    )
    parent=models.ForeignKey('self',blank=True, null=True,on_delete=models.SET_NULL)
    user_id=models.IntegerField(unique=True)
    company=models.ForeignKey(Companies,null=True,on_delete=models.SET_NULL)
    dep=models.ForeignKey(Departments,null=True,related_name="dep", blank=True, on_delete=models.SET_NULL)
    role=models.IntegerField(choices=ROLES)
    position=models.CharField(max_length=200,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=200)
    created_date=models.DateField(default=datetime.now)
    updated_date=models.DateField(default=datetime.now)




    
    