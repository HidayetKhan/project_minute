from Ticket.views import *
from django.urls import path
urlpatterns = [
    path('parsel/',import_from_excel, name='import_from_excel'),
    path('hello/',user_master_file_parsel, name='import_from_excel'),
]