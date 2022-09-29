 1. What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element?
    >A CSRF Token is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources. The tokens are generated and submitted by the server-side application in a subsequent HTTP request made by the client. After the request is made, the server side application compares the two tokens found in the user session and in the request. If the token is missing or does not match the value within the user session, the request is rejected, the user session terminated and the event logged as a potential CSRF attack.
 2. Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.
    >The answer to that is yes you can. The other way to do it without using a generator is with HTML region. You create items in the region and create processes and branches
 3. Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.
    > After user interact with the create task button, the program will get the title and the description. Then, it creates a new object based on the data that user inputted. The data goes to the show_todolist function and go to the page to be shown to the user
 4. Explain how you implement the checklist above
    1. Open my terminal and go to the wanted directory
    2. Create a new app called todolist by 'python manage.py startapp todolits'
    3. in project_django/settings.py , add 'path('todolist/', include('todolist.urls'))' to add the path so users can access http://localhost:8000/todolist
    4. in todolist/models.py, add a class Task to create model
    5. To implement registration, login, and logout, I followed the tutorial in Lab 3. in todolist/views.py , I add a new function register, login_user, and logout user. I also create each of them their own html file
    6. in todolist/views.py , I create a new function show_todolist that accept request parameter and in todolist/templates , I create todolist.html
    7. in todolist/views.py , Create a new function create_task and in template add a new file create_task.html and in template/todolist , create the create_task button
    8. Go to todolist/urls.py and add the path of the todolist, register, login, logout, and create-task
    9. Pull, Add, Commit, and Push to git to deploy my project to Heroku
