from django.contrib import admin
from .models import Companies,Departments,Staff
# Register your models here.
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_date')
    ordering = ['id']

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')
    ordering = ['id']

class StaffAdmin(admin.ModelAdmin):
    list_display = ('user_id','dep_id','company_id','role','email', 'parent','created_date')
    ordering = ['id']


admin.site.register(Companies,CompaniesAdmin)
admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Staff,StaffAdmin)