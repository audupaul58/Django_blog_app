from django.urls import path
from .views import *


urlpatterns = [
    path('', Post_List.as_view(), name='blog_home'),
    path("<int:pk>/", post_detail, name='blog_detail'),
    path("<category>/", Category_List.as_view(), name='blog_category'),
    path("creat", Post_Create.as_view(), name='post_create'),
    path('search/', Search_Page.as_view(), name='search_page'),
]