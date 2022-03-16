from django.urls import path
from home.views import *

app_name='home'

urlpatterns = [
    path('', home , name='home'),
    path('edit/<pk>/', update_page , name='edit'),
    path('chart/', chatshow , name='chat'),
    path('barchart/', bar_chart , name='barchart'),
    path('resetdata/', resetdata , name='resetdata'),
    path('delete/<pk>/', delete_page , name='delete'),
    path('add_data/', add_data , name='add_data'),
]