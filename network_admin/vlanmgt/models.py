from django.db import models

import uuid



from django.db.models.fields import NullBooleanField
# Create your models here.



# Class Definition for vlan attributes , vlanID , vlanName , SubnetID (foreign key with subnet class)
class vlan(models.Model):
    VlanID = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True ,editable=False)
    VlanName = models.CharField(max_length=200, unique=True)
    SubnetID =   models.ForeignKey("subnet", unique=True , on_delete=models.SET_NULL, blank=True,null=True ,to_field="SubnetID")
    # this definition to return vlanName By default when calling vlan class
    def __str__ (self):
       return self.VlanName



# Class Definition for ip attributes , ipID , IpAddress , SubnetID ,ReserveName
class ips(models.Model):
    IpID = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True ,editable=False)
    IpAddress = models.CharField(max_length=200)
    SubNetID = models.CharField(max_length=200,default='')
    ReserveName = models.CharField(max_length=200,default='')
    # this definition to return ipAddress By default when calling ip class
    def __str__ (self):
        return self.IpAddress



 



# Class Definition for subnet attributes , SubnetID , SubnetName , SubnetMask ,NetworkIP,vlan,CIDR
class subnet(models.Model):
    SubnetID = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True ,editable=False)
    SubnetName = models.CharField(max_length=200 ,unique=True)
    SubnetMask = models.CharField(max_length=200,blank=True,null=True )
    Networkip =models.CharField(max_length=200,blank=True,null=True )
    Vlan =  models.ForeignKey("vlan", unique=True , on_delete=models.SET_NULL, blank=True,null=True ,to_field="VlanID")
    CIDR= models.CharField(max_length=2000 , blank=False,null=False)
    # this definition to return SubnetName By default when calling subnet clas
    def __str__ (self):
        return self.SubnetName



   

   
    

    