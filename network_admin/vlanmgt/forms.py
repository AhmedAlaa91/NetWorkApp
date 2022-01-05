from django.forms import ModelForm
from .models import subnet ,vlan , ips

#Class Definition for making form from the subnet model , selecting 2 fields only ['SubnetName','CIDR']
class Subnetform(ModelForm):
    class Meta:
        model = subnet
        fields = ['SubnetName','CIDR']

#Class Definition for making form from the vlan model , selecting all fields 

class Vlanform(ModelForm):
    class Meta:
        model = vlan
        fields = '__all__'

        
#Class Definition for making form from the subnet model , selecting 2 fields only ['IpAddress','ReserveName']

class Ipform(ModelForm):
    # funtction to make field 'IpAddress' read only 
    def __init__(self, *args, **kwargs):
        super(Ipform, self).__init__(*args, **kwargs)
        self.fields['IpAddress'].disabled = True
        
    class Meta:
        model = ips
        fields = ['IpAddress','ReserveName']