from django.db import models

# Create your models here.
class Cloud(models.Model):
    project_name = models.CharField(max_length=30)
    project_id = models.IntegerField()
    client_name = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    contact_name_1 = models.CharField(max_length=30)
    contact_phone_1 = models.IntegerField()
    contact_email_1 = models.EmailField()
    contact_name_2 = models.CharField(max_length=30)
    contact_phone_2 = models.BigIntegerField()
    contact_email_2 = models.EmailField()
    contact_name_3 = models.CharField(max_length=30)
    contact_phone_3 = models.BigIntegerField()
    contact_email_3 = models.EmailField()
    work_order_valid = models.DateField()
    scope = models.CharField(max_length=30)


class VmRequest(models.Model):
    req_choice = (
        ("Elcot Official","ELCOT Official"),
        ("Department","Department"),
        ("Developer","Developer"),
        ("DCO","DCO")
    )
    req_through = (
        ("Mail","Mail"),
        ("Whatsapp","Whatsapp"),
        ("Hard copy","Hard copy")
    )
    approval_choice = (
        ("Approved","Approved"),
        ("Rejected","Rejected")
    )

    request_id = models.IntegerField()
    department_id = models.IntegerField()
    department_name = models.CharField(max_length=30)
    request_recieved_detail = models.CharField(max_length=100)
    request_recieved_time = models.TimeField()
    request_from = models.CharField(max_length=30,choices=req_choice)
    name_official = models.CharField(max_length=30)
    mail_id = models.EmailField()
    phone_num = models.IntegerField()
    organization = models.CharField(max_length=30)
    request_through = models.CharField(max_length=20,choices=req_through)
    request_proof = models.ImageField()
    auth_by = models.CharField(max_length=20)
    auth_proof = models.CharField(max_length=20)
    num_of_vm = models.IntegerField()
    ram = models.IntegerField()
    vcpu = models.IntegerField()
    storage = models.IntegerField()
    os = models.CharField(max_length=30)
    dept_person_name = models.CharField(max_length=30)
    dept_desig = models.CharField(max_length=20)
    dept_mail_id = models.EmailField()
    dept_phone = models.IntegerField()
    dev_person_name = models.CharField(max_length=30)
    dev_desig = models.CharField(max_length=20)
    dev_mail_id = models.EmailField()
    dev_phone = models.IntegerField()
    dev_org = models.CharField(max_length=30)
    approval_cdac = models.CharField(max_length=20,choices=approval_choice)
    remarks_support_eng = models.CharField(max_length=100)
    remarks_cdac_off = models.CharField(max_length=100)


class VmReservation(models.Model):
    reservation_id = models.IntegerField()
    dept_name = models.CharField(max_length=30)
    no_of_vm = models.IntegerField(default=1)
    ram = models.IntegerField()
    vcpu = models.IntegerField()
    storage = models.IntegerField()
    operating_system = models.CharField(max_length=20)


class PhysicalServerDetails(models.Model):
    server_id = models.CharField(max_length=30)
    server_make_model = models.CharField(max_length=30)
    ip_address = models.GenericIPAddressField()
    host_name = models.CharField(max_length=30)
    irdac_ip = models.GenericIPAddressField()
    serial_number = models.CharField(max_length=30)
    amc_end_date = models.DateField()
    location = models.CharField(max_length=30)
    remarks = models.CharField(max_length=100)
    cloud_purpose = models.CharField(max_length=50)

class PhysicalServerCapacity(models.Model):
    Server_IP = models.GenericIPAddressField()
    Host_name = models.CharField(max_length=20)
    Total_VM = models.IntegerField()
    Total_RAM = models.IntegerField()
    Used_RAM = models.IntegerField()
    Available_RAM = models.IntegerField()
    Total_vCPU = models.IntegerField()
    Used_vCPU = models.IntegerField()
    Available_vCPU = models.IntegerField()
    Total_local_storage = models.IntegerField()
    Used_local_storage = models.IntegerField()
    Available_local_storage = models.IntegerField()
    Remarks = models.CharField(max_length=100)

class Storage(models.Model):
    LUN_ID = models.IntegerField()
    Mounted_to_server_IP = models.GenericIPAddressField()
    Mount_point = models.CharField(max_length=30)
    Total_capacity = models.FloatField()
    Used = models.FloatField()
    Available = models.FloatField()
    Remarks = models.CharField(max_length=100)

class VmInventory(models.Model):

    app_db_choice=(
        ("APP","APP"),
        ("DB","DB")
    )
    VM_ID = models.IntegerField()
    Department_name = models.CharField(max_length=30)
    Application_name = models.CharField(max_length=30)
    Application_URL = models.URLField()
    App_or_DB_VM = models.CharField(max_length=10,choices=app_db_choice)
    Tenant_IP = models.GenericIPAddressField()
    Provider_IP = models.GenericIPAddressField()
    vCPU = models.IntegerField()
    RAM = models.IntegerField()
    Storage = models.FloatField()
    Physical_server_ID = models.CharField(max_length=30)
    Remarks = models.CharField(max_length=100)
    VM_creation_date = models.DateField()

class ApplicationInventory(models.Model):
    cho = (
        ("Payment gateway","Payment gateway"),
        ("SMS","SMS"),
        ("Email services","Email services")
    )
    Application_ID = models.CharField(max_length=30)
    Department_name = models.CharField(max_length=30)
    Application_URL = models.URLField()
    External_server_linked_to_the_application = models.CharField(max_length=30,choices=cho)
    SSL_expiry = models.DateField()
    SSL_Vendor = models.CharField(max_length=30)
    APP_VM_ID = models.CharField(max_length=30,null=True)
    DB_VM_ID = models.CharField(max_length=30,null=True)
    Public_IP = models.GenericIPAddressField()
    Live_Date = models.DateField()
    Contact_detail_id = models.IntegerField()
    Remarks = models.CharField(max_length=100)
    Current_status = models.CharField(max_length=30)

class ContactDetailsInventory(models.Model):
    Contact_ID = models.IntegerField()
    Department_ID = models.IntegerField()
    Application_ID = models.IntegerField()
    Department_Name = models.CharField(max_length=30)
    Department_mail = models.EmailField()
    Department_phone_number = models.IntegerField()
    Developer_Name = models.CharField(max_length=30)
    Developer_mail = models.EmailField()
    Developer_phone_number = models.IntegerField()
    Remarks = models.CharField(max_length=100)