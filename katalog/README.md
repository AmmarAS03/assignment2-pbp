Diagram
![PBP-Diagram](https://user-images.githubusercontent.com/101089719/190298132-9ed50e0e-9008-4c9b-994a-edae616cea52.jpeg)

Why do we use virtual environment?

Because when we use virtual environment, otomatically virtual environment will install packages and dependencies. If we don't use virtual environment,
we are only able to access from the installed directory. Virtual environment also helps us if we wanted to use 2 library which have different version.
To understand this a little bit more, I'll set an example, imagine you're dealing with two clients. One client is comfortable using Django 2.1.3 and the other
one wants to use Django 4.0. Having a single virtual environment for both clients won't work and you can't have two different versions of the same package
in a single python environment. However, if you create a virtual environmenmt for each of your client's projects, then you can install a different version of
Django into each of them

How did I implement the steps on point 1-4
1. First, I made a function called catalog_display(request) that can do query. I get all the data and put them
   inside variable data_barang_katalog with CatalogItem.objects.all().
2. Then, I add path('', catalog_display, name='catalog_display') in the katalog folder and the urls.py file. In folder django, in the urls.py file,
   I also add path('katalog/',include('katalog.urls'))
3. Then, in katalog/template/katalog.html, I map the data that has been returned into HTML in list_barang using iteration
4. To deploy my assignment to Heroku, I open Heroku and create new app and import assignment2-pbp from the repository in github to heroku. Add repository secret with the apps name and API key. After I add, commit, and push, the the apps will be deployed.
