from django.forms import ModelForm
from .models import Cloud,VmRequest,VmReservation,PhysicalServerDetails,PhysicalServerCapacity,Storage,VmInventory,ApplicationInventory,ContactDetailsInventory

class CloudForm(ModelForm):
    class Meta:
        model = Cloud 
        fields = "__all__"

        labels={
            'project_name':"Name of project",
            'project_id': "Project ID",
            'client_name': "Client name",
            "address":"Address",
            "contact_name_1":"Contact name 1",
            "contact_phone_1":"Contact phone 1",
            "contact_email_1":"Contact email 1",
            "contact_name_2":"Contact name 2",
            "contact_phone_2":"Contact phone 2",
            "contact_email_2":"Contact email 2",
            "contact_name_3":"Contact name 3",
            "contact_phone_3":"Contact phone 3",
            "contact_email_3":"Contact email 3",
            'work_order_valid':"Work order valid till",
            "scope":"Scope of work"



        }

class VmrequestForm(ModelForm):
    class Meta:
        model = VmRequest
        fields = "__all__"

        labels={    
                    'request_id': 'Request ID',
                'department_id ':'Department ID',
                'department_name': 'Department name',
                'request_recieved_detail':'Request received detail',
                'request_recieved_time':'Request recieved time',
                'request_from':'Request recieved from',
                'name_official':'Name of official',
               'mail_id':'Official mail id',
                'phone_num':'Official phone number',
                'organization':'Organization',
                'request_through':'Request recieved through', 
                'request_proof':'Request proof(Mail or letter) to be uploaded',
                'auth_by':'Authorization by (official)',
                'auth_proof' :'Authorization proof',
                'num_of_vm' : 'Number of VMs',
                'ram' :'RAM',
                'vcpu':'vCPU',
                'storage' :'Storage',
                'os':'Operating System',
                'dept_person_name':'Department contact person name',
                'dept_desig':'Department contact person designation',
                'dept_mail_id' :'Department contact person mail id',
                'dept_phone' :'Department contact person phone number',
                'dev_person_name' :'Developer contact person name',
                'dev_desig' :'Developer contact person designation',
                'dev_mail_id' :'Developer contact person mail id',
                'dev_phone' :'Developer contact person phone number',
                'dev_org' :'Developer contact person organization',
                'approval_cdac' :'Approval by C-DAC official',
                'remarks_support_eng' : 'Remarks by C-DAC support engineer',
                'remarks_cdac_off' :'Remarks by C-DAC official'
            

                }


class VmreservationForm(ModelForm):
    class Meta:
        model = VmReservation
        fields = "__all__"

        labels = {

                    'reservation_id':"Reservation ID",
                    'dept_name':"Department name",
                    'no_of_vm':"No of VM",
                    'ram':"RAM",
                    'vcpu':"vCPU",
                    'storage':"Storage",
                    'operating_system':"Operating System"
                 }

class PhysicalServerDetailsForm(ModelForm):
    class Meta:
        model = PhysicalServerDetails
        fields = "__all__"

        labels={
            'sl_no':"sl.no",
            'server_id':'Server ID',
        'server_make_model':'Server make & model',
        'ip_address':'IP Address',
        'host_name':'Host name',
        'idrac_ip':'IDRAC IP',
        'serial_number':'Serial number',
        'amc_end_date':'AMC end date',
        'location':'Location',
        'remarks':'Remarks',
        'cloud_purpose' :'Cloud purpose'
        }


class PhysicalServerCapacityForm(ModelForm):
    class Meta:
        model = PhysicalServerCapacity
        fields = "__all__"


class StorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = "__all__"

class VmInventoryForm(ModelForm):
    class Meta:
        model = VmInventory
        fields = "__all__"

class ApplicationInventoryForm(ModelForm):
    class Meta:
        model = ApplicationInventory
        fields = "__all__"


class ContactDetailsInventoryForm(ModelForm):
    class Meta:
        model = ContactDetailsInventory
        fields = "__all__"