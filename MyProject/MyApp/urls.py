from django.urls import path
from .views import homeView,eligibility_view,nav_view,feature_view,fees_charges_view,req_doc_view

urlpatterns = [
    path('home/',homeView),
    path('nav/el/',eligibility_view,name='eligibility'),
    path('nav/',nav_view),
    path('nav/fet/',feature_view,name='features'),
    path('nav/fee/',fees_charges_view,name='fee_charges'),
    path('nav/doc/',req_doc_view,name='req_doc'),
]