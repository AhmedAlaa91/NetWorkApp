from django.shortcuts import render , redirect

from .models import ips, subnet ,vlan

from .forms import Subnetform , Vlanform , Ipform
import uuid

# Create your views here.
from django.http import HttpResponse

import numpy as np




from uuid import UUID
from netaddr import IPNetwork




#Generate IPs method to generate ipaddresses range , networkIp,SubnetMask based on input CIDR 
def GenerateIP(cidr,subnetid):
    network = IPNetwork(cidr)
    generator = network.iter_hosts()

    for i_ip in generator :
        newip = ips(IpAddress=i_ip,SubNetID=subnetid)
        newip.save()

    return network.network , network.netmask


#Home Method : to return all subnet data and redner it to index.html

def home(request):
    
    subnets_list = subnet.objects.all()
    context = {'subnet_list':subnets_list}

    return render(request , 'index.html',context)


#---------------------------------Subnet Methods

#CreateSubnet_v Method : create instance from subnet form (pre-defined in forms.py) and render the objects to createForm.html ,
#check validity of data entered  , call generate ips method ,  create records in the DB then redirect to home
def CreateSubnet_v(request):

    form = Subnetform()

    if (request.method == 'POST') :
        form = Subnetform(request.POST)
        if form.is_valid():
            
            mysaved_model = form.save()
            response = {}
            response['subnetid'] = mysaved_model.SubnetID

            data = form.cleaned_data
            CIRD_Field = data['CIDR']

            Generatedip=GenerateIP(CIRD_Field,response['subnetid'])
            mysaved_model.Networkip,mysaved_model.SubnetMask =Generatedip
            mysaved_model.save()
            return redirect('home')



    context={'form' : form}


 
    return render(request , 'createForm.html',context)



#allSubnets_v Method : to return all subnet data and redner it to index.html
def allSubnets_v(request):
    subnets_list = subnet.objects.all()
    
    context = {'subnet_list':subnets_list}

    return render(request , 'index.html',context)


#Asubnet_v Method : return single subnet details that already stored in db and linked the the provided pk 
#select all ips have the same subnet id as pk
#get number of all ips and reserved ones to calculate the utilization percentage 
#check if there is vlanID is related to this subnet , if yes it will be returned
#render all context to subnetDetails.html
def Asubnet_v(request,pk):
    subnetObj =subnet.objects.get(SubnetID=pk)
    ipsObj = ips.objects.all().filter(SubNetID=pk)
    ipsObjCount = ipsObj.count()
    ipsreserved =ipsObj.filter(ReserveName__exact='').count()
    utilization = round(((ipsreserved/ipsObjCount)*100),2)



    try :
        
        VlanObj = vlan.objects.get(SubnetID=pk)
    except :
        VlanObj = None


  

    if VlanObj :
        context ={'subnet_list':subnetObj,'ips_list':ipsObj , 'vlan_list':VlanObj,'utilization':utilization}

    else :
        context ={'subnet_list':subnetObj,'ips_list':ipsObj , 'utilization':utilization }

    
    
    return render(request , 'subnetDetails.html',context)

#DeleteSubnet_v Method : delete a subnted related to the provided pk and delete all ips related to this subnet
def DeleteSubnet_v(request,pk):
    subnetObj = subnet.objects.get(SubnetID=pk)
    ipsObj = ips.objects.all().filter(SubNetID=pk)

    if request.method == 'POST':
        subnetObj.delete()
        ipsObj.delete()
        return redirect('home')

        
    context={'object':subnetObj.SubnetName}
    return render(request , 'DeleteForm.html',context)    



#---------------------------------Vlan Methods

#method allVlans_v : return all vlans and render context to all allVlans.html
def allVlans_v(request):
    vlans_list = vlan.objects.all()
    
    context = {'vlans_list':vlans_list}

    return render(request , 'allVlans.html',context)


#method Avlan_v : return details of vlan related to the pk provided 
#check if subnet linked to VlanID and return subnet if yes
#render context to vlanDetails.html
def Avlan_v(request,pk):
    vlanObj =vlan.objects.get(VlanID=pk)
    

    try :
        VlanObjID =subnet.objects.get(SubnetName=vlanObj.SubnetID)
    except:
        VlanObjID = None
    

    if VlanObjID:
        SubnetObj = subnet.objects.get(SubnetID=UUID(str(VlanObjID.SubnetID)))
    else :
        SubnetObj = None
    

    context ={'vlan_list':vlanObj , 'subnet_list':SubnetObj}

    return render(request , 'vlanDetails.html',context)

#CreateSubnet_v Method : create instance from vlan form (pre-defined in forms.py) and render the objects to createForm.html ,
#check validity of data entered update records in the DB then redirect to all-vlans
def CreateVlan_v(request):

    form = Vlanform()

    if (request.method == 'POST') :
        form = Vlanform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('All-Vlans')



    context={'form' : form}


 
    return render(request , 'createForm.html',context)

#updateVlan_v Method : create instance from vlan form (pre-defined in forms.py) from objects of vlan related to the pk
# and render the objects to editForm.html ,
#check validity of data entered    create records in the DB then redirect to all-vlans

def updateVlan_v(request,pk):

    vlanObj =vlan.objects.get(VlanID=pk)
    form = Vlanform(instance=vlanObj)

    if request.method == 'POST':
        form=Vlanform(request.POST,instance=vlanObj)
        if form.is_valid():
            form.save()
            return redirect('All-Vlans')


    context ={'form':form}

    return render(request , 'editForm.html',context)


#DeleteSubnet_v Method : delete a vlanid related to the provided pk then redirect to home

def DeleteVlan_v(request,pk):
    VlanObj = vlan.objects.get(VlanID=pk)
  

    if request.method == 'POST':
        VlanObj.delete()
        return redirect('home')

        
    context={'object':VlanObj}
    return render(request , 'DeleteForm.html',context)    


#---------------------------------IP Methods

#updateIP_v Method : create instance from ip form (pre-defined in forms.py) from objects of ip related to the pk
# and render the objects to editForm.html ,
#check validity of data entered    create records in the DB then redirect to subnet related to this ip


def updateIP_v(request,pk):

    ipObj =ips.objects.get(IpID=pk)
    form = Ipform(instance=ipObj)

    if request.method == 'POST':
        form=Ipform(request.POST,instance=ipObj)
        if form.is_valid():
            form.save()
            return redirect('Subnet',ipObj.SubNetID)


    context ={'form':form}

    return render(request , 'editForm.html',context)



# SearchIP_v method : return all matching ip objects matching with "ipquery" with subnets and details about this ip
def SearchIP_v(request):
    ipsdict={}
    ipsdictorig={}
    if request.method == 'GET':
         if request.GET.get("ipquery"):
                search_query = request.GET.get("ipquery")
                
                ipsObjID = ips.objects.filter(IpAddress=search_query).values('IpAddress','ReserveName','SubNetID','IpID')

                Key_i =0
                

                for i in  ipsObjID :

                    subnetObj = subnet.objects.get(SubnetID=UUID(str(i['SubNetID'])))
                    ipsdict = {'IpID':i['IpID'],'IpAddress':i['IpAddress'],'ReserveName':i['ReserveName'],'SubNetID':i['SubNetID'],'SubnetName':str(subnetObj).replace('<','').replace('>','').replace('subnet','')}
                    
                    ipsdictorig[Key_i]=ipsdict
                    Key_i = Key_i +1 

                context ={'ipsdict':ipsdictorig,'IpAdd':search_query}
                
                

                return render(request , 'allips.html',context)

    
    context ={'form':ipsdict}
    

    return render(request , 'searchIPs.html',context)

    