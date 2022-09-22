The difference between Json, Xml, and HTMl
HTML(Hyper Text Markup Language) would wrap content in tags, but the rules regarding which tags could be used when and where were much less strict. HTML is great for developers but the lack of structure provided by SGML was missing. This led to the creation of XML. XML could maintain the structure of information without worrying about formatting at all. Json is more popular due to it's advancement of web application development and also because Json use languages such as javascript not only markup languages which just display stuff so it is more easy to interact.

Why we need data delivery when implementing on a platform?
Data delivery allows organizations to use evidence-based data to make decisions and plan carefully to pursue business objectives because it allows the computer to interact with users by delivering the data.

How do I complete this assignment?
1. First I open my terminal and go to my assignment 2 folder directory
2. I create new app name mywatchlist by typing 'python manage.py startapp mywatchlist' which I knew from the Lab 1
3. in INSTALLED_APPS in the settings.py file inside project_django folder, I add mywatchlist
4. I also add mywatchlist URL path by going to urls.py in project_django and add path('mywatchlist/', include('mywatchlist.urls'))
5. Create a model in models.py in mywatchlist and it's attribute
6. I create 10 random movies in a new file initial_mywatchlist_data.json in new fixture folder in mywatchlist
7. To implement a feature to show the data in HTML, XML, and Json format, I make each of them their own function just like the one in lab 2
8. Add the show_watchlist, XML,Json, and HTML in urls.py in the mywatchlist with 
urlpatterns = [
    path('',show_mywatchlist, name='mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/',show_html, name='show_html')

]