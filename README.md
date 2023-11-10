
This Django API is designed to handle store products. It is built using the Django web framework 

<!-- picture demo1.png -->
DEMO 1
![alt text](/demo1.png)
DEMO 2
![alt text](/demo2.png)
DEMO 3
![alt text](/demo3.png)


To get started, make sure you have Python and Django installed on your machine. Then, clone this repository and navigate to the project directory in your terminal.

**Learning objectives**
**Creating a serializer**
**Working with API views**
**Filtering back ends**
**Enabling pagination**
**Executing CRUD operations**
**Managing serializer fields**
**Testing API views**


When using python, it is recommended to use the virtual environment so that you can be able to know what versions of Python you are using.

Here is how you can create a virtual environment on mac or Windows
(assuming you have Python installed and version is > 3)



##### 1. run this command below to create a virtual environment:
(venvs will be your virtual environment name )
```bash
    python -m venv venvs
```
*if it doesn't work, try running the following command:*

```bash
 pip install virtualenv
 ```
*then run to creat your virtual enveroment*

```bash
 virtualenv venvs
 ```
 #### To activate the virtual environment, run the following command:
 (on Mac OS or Linux)
```bash
source venvs/bin/activate
 ```
On windows, the virtual environment can be activated by running:

```bash
source venvs/Script/activate
 ```

##### If you have successfully created the virtual environment, well done.


Run the following command to install the required packages:
```bash
    pip install -r requirements.txt
```

### Now that you have, install the required packages, generate django secret key:

```bash
python 
```

```python
from django.core.management.utils import get_random_secret_key  
```
```
get_random_secret_key() 
```
add to env file:

```python
DJANGO_SECRET_KEY="django-insecure-YOUR_SECRET_KEY"
````

<!-- create admin -->
### LET US CREAT THE ADMIN USER
Create admin user, you will be asked a name and Password
* Name: mwamuziscodev
* Password: mwamuziscode@

*(you can of course use any name and password you want)*
example:
 <!-- create admin  -->
Create admin user:

```bash
    python manage.py createsuperuser
```

```bash
python manage.py createsuperuser
Username (leave blank to use 'admin'):
Email address: admin@gmail.com
Password:
Password (again):
Superuser created successfully.
```

Finally run the server with the following command:

```bash
python manage.py runserver
```
- ###### if you want to specify the port number, you can use the following

```bash
python manage.py runserver 8000
```
if you want to specify the IP ADRESS, you can use the following

```bash
python manage.py runserver 127.0.0.1:8000
```

### Well done. Now go  to the url below and explore the API


<!-- website -->
This is a sample webiste showing product being added
You should now be able to access the API at http://localhost:8000/


VIEW ALL PRODUCT ON THE HOMEPAGE
```bash
http://127.0.0.1:8000
```

VIEW ALL PRODUCT IN JSON FORMAT IN THE DJANGO-RESTFRAMEWORK API
```bash
http://127.0.0.1:8000/api/v1/products/
```

GET ONE PRODUCT, HERE YOU CAN RUD (retrieve, update, delete)
```bash
http://127.0.0.1:8000/api/v1/products/1/
```

<!-- For more information on how to use this API, please refer to the documentation at [insert link to documentation].
""" -->

PICTURE CAN BE UPLOADED FROM PRODUCT FILE
