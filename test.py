#Md Sabbir Hossain
// Create Environment
conda create --name myDjango django

//View Conda Info
conda info --envs

//Environment Activation
$ conda activate myDjango

//Environment Deactivation
$ conda deactivate

//Create a Django Project
django-admin startproject first_project

//Run a Django Project
python manage.py runserver

//Create a Django application
python manage.py startapp first_app

//Python Library Installation
pip install Faker
pip install bcrypt #Using For Password Hashing
pip install django[argon2] #Using For Password Hashing

#Model Activity
python manage.py migrate
python manage.py makemigrations first_app
python manage.py migrate


python manage.py createsuperuser

MTV = Model Template View
