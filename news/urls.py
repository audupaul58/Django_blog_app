from django.urls import path
from .views import *

urlpatterns = [
    path('', News_List.as_view(), name='home'),
    path('<int:pk>/', News_Details.as_view(), name='details'),
    path('create/', News_Create.as_view(), name='create'),
    
]