from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
    path('', login_, name='login'),
    path('logout/', logout_, name='logout'),
]