from django.shortcuts import render
from .forms  import CloudForm,VmrequestForm,VmreservationForm,PhysicalServerDetailsForm,PhysicalServerCapacityForm,StorageForm,VmInventoryForm,ApplicationInventoryForm,ContactDetailsInventoryForm
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
app_name:'cloud'
def home(request):
    return render(request,'cloud/home.html')


def cloud_mod1(request):
    if request.method == 'POST':
        form = CloudForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))
    
    else:
        form=CloudForm()
    return render(request,'cloud/edit_cloud.html',context={'form':form})

def vmrequest(request):
    if request.method == 'POST':
        form = VmrequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))
    else:
        form = VmrequestForm()
    return render(request,'cloud/vm_request.html',context={'form':form})


def vm_reservation(request):
    if request.method == 'POST':
        form = VmreservationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))

    else:
        form = VmreservationForm()

    return render(request,'cloud/vm_reservation.html',context={'form':form})


def physical_server_details(request):
    if request.method == 'POST':
        form = PhysicalServerDetailsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))

    else:
        form = PhysicalServerDetailsForm()

    return render(request,'cloud/physical_server_details.html',context={'form':form})


def physical_server_capacity(request):
    if request.method == 'POST':
        form = PhysicalServerCapacityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))

    else:
        form = PhysicalServerCapacityForm()

    return render(request,'cloud/physical_server_capacity.html',context={'form':form})

def storage(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))

    else:
        form = StorageForm()

    return render(request,'cloud/storage.html',context={'form':form})



def vm_inventory(request):
    if request.method == 'POST':
        form = VmInventoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))

    else:
        form = VmInventoryForm()

    return render(request,'cloud/vm_inventory.html',context={'form':form})

def application_inventory(request):
    if request.method == 'POST':
        form = ApplicationInventoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))

    else:
        form = ApplicationInventoryForm()

    return render(request,'cloud/application_inventory.html',context={'form':form})

def contact_details_inventory(request):
    if request.method == 'POST':
        form = ContactDetailsInventoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))

    else:
        form = ContactDetailsInventoryForm()

    return render(request,'cloud/contact_details_inventory.html',context={'form':form})

