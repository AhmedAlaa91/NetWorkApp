# NetWorkApp
1-	Make sure to install django  (python -m pip install django) , this command will install latest package .
2-	Get folders from repistory https://github.com/AhmedAlaa91/NetWorkApp
3-	Open Visual Studio Code , open new folder and select directory contains the clone
4-	You be able to see 2 main folder [‘.venv’,’network_admin’]
5-	Open power shell in VS code , navigate to : .venv\Scripts\ , then write  activate  , full command should be like this : .venv\Scripts\activate
6-	Now your virtual environment is now activated .
7-	.venv is a virtual environment that contains all modules and libraries used in the application
8-	Now navigate to directory ’network_admin’ and write “python manage.py runserver” to start the application on local host 
9-	Your full command should look like this :~ \VlanDjango\network_admin> python manage.py runserver
10-	Now your application is running on local host : http://127.0.0.1:8000/
11-	Use home link : http://127.0.0.1:8000/home/


Classes /*.py files 
The network_admin folder contains all py files and classes needed to implement and develop the application 
1-	network_admin/network_admin/settings.py , contains all settings to register your application in our case (vlanmgt) , although other files like using databases like sql server or oracle or if needed to use external html templates for gui .
2-	network_admin/network_admin/urls.py , contains urlpatterns , all urls that will be used in the application are defines with the methods that will be triggered and name of the url that will be called with in the html template .
3-	network_admin/vlanmgt/admin.py , this file where you register your created models so to be recognized by the application
4-	network_admin/vlanmgt/forms.py , this file contains the forms definition needed for creating a new instance of a model or updating existing one , you need state the name of the model , give a name a form name , then state the fields that you wanted to be seen by the user for this form
5-	network_admin/vlanmgt/models.py , this file contains the attributes and fields for each model and their types and primary key , for example model for Subnet , has its own attributes like name , id , ips 
6-	network_admin/vlanmgt/views.py , this file contain all views used by the applications like “createSubnet” , custom methods like “generateIps” , all modules needed to imported like “import numpy , network” , methods are defined by request that is triggered when a url is called which assigned to this method or view , method may pass parameters provided by the url , make some procedures like creating or deleting records , then render the data to html template defined at the end of each view 
7-	network_admin/vlanmgt/templates , contains all html files that are used to render data from the views.

