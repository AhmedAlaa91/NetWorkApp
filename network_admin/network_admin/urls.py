"""network_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path


from vlanmgt.views import home , CreateSubnet_v , allSubnets_v , Asubnet_v , DeleteSubnet_v,CreateVlan_v,allVlans_v,Avlan_v,updateVlan_v,DeleteVlan_v,updateIP_v,SearchIP_v
# url patterns , first part is for the format of the url in your browser and the query paramter 
#second part , the view which will be triggered when this url called
# third part , the name of the url which will be used to call this url in the html template 
urlpatterns = [
    path('home/', home, name='home'),
    path('admin/', admin.site.urls),
    path('Create-Subnet/', CreateSubnet_v, name='Create-Subnet'),
    path('home/', allSubnets_v, name='home'),
    path('Subnet/<str:pk>/', Asubnet_v, name='Subnet'),
    path('Delete/<str:pk>/', DeleteSubnet_v, name='Delete'),
    path('All-Vlans/', allVlans_v, name='All-Vlans'),
    path('Create-Vlan/', CreateVlan_v, name='Create-Vlan'),
    path('Vlan/<str:pk>/', Avlan_v, name='Vlan'),
    path('Update-Vlan/<str:pk>/', updateVlan_v, name='Update-Vlan'),
    path('Delete-Vlan/<str:pk>/', DeleteVlan_v, name='Delete-Vlan'),
    path('Update-ip/<str:pk>/', updateIP_v, name='Update-ip'),
    path('Search-ip/', SearchIP_v, name='Search-ip'),
    path('all-ips/', SearchIP_v, name='all-ips'),
    
]
