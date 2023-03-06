HTML,Django & How it's works

Basic requirements to build a website 
* Html 
* CSS
* Javascript 

Django helps us to platform to easily render a webpage and work with database and api

Role: Django is free and open source web application framework written in pyhton 

Django offers a big collection of modules which you cna use your own projcets 

Primarily, frameworks exist to asve developers a lot of wasted tome and headaces and djnago is not different
 
 ---

 Django has a data base connector 
 it has a url despenser. and ect ect



 --- 
 MVT architectuere of django 

 The M-V-T (Model view template ) is a sftwarre design pattern

 The view is used to execute the bussiness logic and interact with a model to carry data and renders a template.

 There is no separate controller and complete application is based on Model View and Template. 

Model --> creation of data base and how data will be stored in done in model.

View --> this is regarding the view of the webpage this will be associated with a template.

Template --> Html, css & js.

 --- 

 What is a projcet or an apps 
 every projcet requires an app so that means that every projcet will have at least onw app 
 app is liek a feature of the projcet or it helps with the feature of the app.

Django apps--> 


----

include --> used in url forwarding 
HttpResopnse --> used to show string in the on the page that views is pointing 

url despatching -->Done 
 
 ---- 

Template -->


---- 

`Python3 manage.py makemigration`--> which is responsible for creating new migrations based on the changes you have made to your models.

`Python3 manage.py migrate`--> which is responsible for applying and un applying migration.

`Python3 manage.py sqlmigrate` --> which displays the SQL Statemnets for a migration 


`Python3 manage.py showmigrations` --> lists a projcet's migration and their status

---
### Adding Admin details in the login page.
---
* `admin.site.site_header = "UMSRA Admin"`
* `admin.site.site_title = "UMSRA Admin Portal"`
* `admin.site.index_title = "Welcome to UMSRA Researcher Portal"`
---

Template Inheritance --> inheriting a template in all the sub templates can be acalled tempalte inheritance 
for example if we want the nav bar on every page.