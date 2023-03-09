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



---
Models--> 
Models defines your databases

After creating models we will migrate and after thayt we will run migration commnands

0. add the model specifications in models.py

1. register model in the admin.py 
2. register app 
from apps to settings.py 
in the foramt 
Home.apps.HomeConfig(App_name.apps.Class_name) as string 
3. run `python3 manage.py makemigrations` and you will see an migration file.
4. migration generates the file that will store this change in the db or creates changes adn store in a file
5. after this we run `python3 manage.py migrate` apply the pending chanes created by makemigrations.
6. this will create the table in the data base.
7. Now you can find the contact table in your admin 
8. Now you will write the Logic too add data to the database table IN VIEW

9. somewhat like this  `
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'Contact.html')`



    `python3 manage.py shell` ---> opens shell for the project