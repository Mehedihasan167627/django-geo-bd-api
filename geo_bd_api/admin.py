from django.contrib import admin
from .models import*
# Register your models here.


@admin.register(Division)
class DivitionAdmin(admin.ModelAdmin):
    list_display=["english_name","bangla_name","id","website"]
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display=["english_name","bangla_name","latitude","longititude","id","division","website"]
@admin.register(Upazila)
class UpazilaAdmin(admin.ModelAdmin):
    list_display=["english_name","bangla_name","district","website","id"]
@admin.register(Union)
class UnionAdmin(admin.ModelAdmin):
   list_display=["english_name","bangla_name","upazila","district","division","website","id"]
