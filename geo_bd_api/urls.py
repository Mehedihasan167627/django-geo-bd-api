
from django.urls import path

from .views import*

urlpatterns = [
      path('divisions/',DivisionView.as_view()),
   
      path('districts/<int:division_id>/',DistrictView.as_view()),
    
      path('upazilas/<int:district_id>/',UpazilaView.as_view()),
    
      path('unions/<int:upazila_id>/',UnionView.as_view()),
     
]


