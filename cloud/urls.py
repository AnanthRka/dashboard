from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('vmrequest/',views.vmrequest,name='vmrequest'),
    path('cloud_edit/',views.cloud_mod1,name='cloud_edit'),
    path('vm_reservation/',views.vm_reservation,name='vm_reservation'),
    path('physical_ser_det/',views.physical_server_details,name='physical_server_details'),
    path('physical_ser_cap/',views.physical_server_capacity,name='physical_server_capacity'),
    path('storage/',views.storage,name='storage'),
    path('vm_inventory/',views.vm_inventory,name='vm_inventory'),
    path('application_inv/',views.application_inventory,name='application_inventory'),
    path('contact_det_inv/',views.contact_details_inventory,name='contact_detail_inventory')
]