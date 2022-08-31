import re
from urllib import response
from ninja import NinjaAPI
from ninja import Schema
import hashlib
import json
from typing import List
from companies_app.models import Staff,Companies,Departments
from typing import List
from django.http import HttpResponse
api = NinjaAPI()
import redis

r = redis.Redis(
    host='redis',
    port=6379)

class comItem(Schema):
    name: str
    bin: str 
    role :int
    email: str

class selComItem(Schema):
    bin: str 
    role :int
    email: str


class depItem(Schema):
    id: int =None
    title: str = None

class empItem(Schema):
    user_id: int = None
    dep_id: int = None
    email: str =None
    role: str =None
    company_id: str=None


class companies(Schema):
    title: str = None
    bin: str = None

def userToken(request):
    res=[x.split('=') for x in request.headers['Authorization'].split(';') if x.strip().startswith("dyns_token")]
    if res:
        return res[0][1]
    else:
        return None



@api.post("/createCom")
def createCom(request,comItem: comItem):
    token=userToken(request)
    user_id=r.get(token)
    com=Companies.objects.create(title=comItem.name,bin=comItem.bin,created_by=user_id)
    try:
        Staff.objects.create(user_id=user_id,company_id=com.id,role=comItem.role,email=comItem.email)
        return True
    except:
        return False

@api.post("/selCom")
def selCom(request,item: selComItem):
    token=userToken(request)
    user_id=r.get(token)
    com=Companies.objects.filter(bin=item.bin).get()
    try:
        Staff.objects.create(user_id=user_id,company_id=com.id,role=item.role,email=item.email)
        return True
    except:
        return False


@api.get("/getCompanies")
def getCompanies(request):
    items= Companies.objects.all()
    items2=[]
    for item in items:
        items2.append({'code':item.bin,'label':item.title})
    return items2

@api.get("/getDepartments",response=List[depItem])
def getDepartments(request):
    items= Departments.objects.all()
    return items

@api.get("/getEmp",response=empItem)
def getCurrentEmp(request):
    token=userToken(request)
    user_id=r.get(token)
    try:
        return Staff.objects.get(user_id=user_id)
    except:
        None

@api.get("/getEmps",response=List[empItem])
def getEmps(request):
    token=userToken(request)
    user=getCurrentEmp(request)
    emps=Staff.objects.filter(company_id=user.company.id)
    return emps

@api.post("/createDepartment")
def createDepartment(request,depItem: depItem):
    token=userToken(request)
    user_id=r.get(token)
    emp=Staff.objects.get(user_id=user_id)
   
    dep=Departments.objects.create(title=depItem.title,company_id=emp.company.id,created_by=user_id)
    try:
        return True
    except:
        return False


@api.post("/changeEmpDep")
def changeEmpDep(request,empItem: empItem):
    token=userToken(request)
    try:
        print(empItem)
        user=Staff.objects.get(user_id=empItem.user_id)
        user.dep_id=empItem.dep_id
        user.save()
        return True
    except Exception as e:
        print(e)
        return False
    

