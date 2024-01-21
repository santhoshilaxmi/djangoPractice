<img width="554" alt="image" src="https://github.com/santhoshilaxmi/djangoPractice/assets/38223932/19ac6d27-280a-4df7-9518-f9e02dc6ff00">

Django is a framework which gives flexibility to built the backend of the web application in python.

it works based on the MVT model, M- Model V- View T Template

for different projects we might need different versions of Django, so lets create a virtual environment 

create virtual env wrappwe - >pip install virtualenvwrapper-win
app_data_dir=C:\Users\admin\Envs)

create virtual env - mkvirtualenv test
now install Django in the virtualenv(test) pip install django and this Django is available only to this virtualenv notto the entire computer

make a dir for project and start the djago project as - django-admin startproject sgouru

it creates urls, settings, wgi(useful for running on the server) 
it also had manage.py where django gives us lightweight server to run our project on 
and we can run ther server using python manage.py runserver
as there are no code in the project it just shows this page
 ![image](https://github.com/santhoshilaxmi/djangoPractice/assets/38223932/d455ba66-e432-4a18-a646-544e1de244df)



Now we opened the project in pycharm 
![image](https://github.com/santhoshilaxmi/djangoPractice/assets/38223932/d58a8350-9d1b-4f8f-81b4-194c4c40c4ef)

 
for us to switch to virtual envs run activate.bat file under the scripts in virtualenv located in Envs

Now, we create a first app called calc in the virtual env by python manage.py startapp calc 

**URL mapping :**
create a urls.py in the calc as the existing urls in the home project is for the entire project not just for calc

and in the urls.py 

urlpatterns =[

    path('',views.home, name='home')

]

**' '** - this is used for home page 


**view.home** - this is the defination which need to be called when loading the home page, basically view will have all the code/content which we see in the home page



now write a defination home in the views.py, this defination accepts the request as argument and it need to retyrn response in the HttpResponse format 

def home(request):

    return HttpResponse("Hello World")
    
    
now go to the main project urls and include this calc/urls.py as 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),
]

so whenever the home page is called it will go to calc.urls

**Django Template:(DT language)**






