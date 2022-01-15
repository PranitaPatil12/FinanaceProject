from django.urls import path
from .views import homeView,eligibility_view,nav_view

urlpatterns = [
    path('home/',homeView),
    path('nav/el/',eligibility_view,name='eligibility'),
    path('nav/',nav_view)
]