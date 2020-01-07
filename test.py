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
