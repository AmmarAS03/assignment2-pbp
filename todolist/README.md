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

 Assignment 5 (6 OCTOBER 2022)
 1. What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?
  a. Internal CSS
    > The internal CSS code is placed inside the <head> section of the page. Class and ID can be used to refer to CSS code, but will only be active on that page. CSS styles installed with this method will be downloaded every time the page is called, so this will increase the access speed. However, there are cases where using internal stylesheets is useful. One example is to send a page template to someone – since everything can be seen on one page, it's easier to preview. 
 CSS internal benefits:
     >Changes only occur on 1 page
     >Class and ID can be used by internal stylesheet
>There is no need to upload multiple files because HTML and CSS can be used in the same file.
Disadvantages of using Internal CSS:

>Increase website access time
> Changes only occur on one page
 > not efficient when you want to use the same CSS across multiple files.
 b. One of the most convenient ways to add CSS to your website is by linking it to an external .CSS file. That way, any changes you make to the CSS file will appear on your website as a whole. External CSS files are usually placed after the <head> section of the page
 Benefits of external CSS:

The HTML file size is smaller and the structure is neater
Faster loading speed
The same CSS file can be used on multiple pages.
Disadvantages of external CSS:

The page does not appear completely until the CSS file has been called.
 c. Inline CSS is used for certain HTML tags. The <style> attribute is used to style certain HTML tags. This method is not recommended, because each HTML tag must be styled in its own way. You will find it more difficult to set up your website if you only use inline CSS. However, in some situations inline CSS can be useful. For example, when you don't have access to a CSS file or have to change the style for only one element.
 2. Describe the HTML5 tags that you know.
 <a>	Defines a hyperlink.
 <body>	Defines the document's body.
 <br>	Produces a single line break.
 <button>	Creates a clickable button.
 <div>	Specifies a division or a section in a document.
 <form>	Defines an HTML form for user input.
 <head>	Defines the head portion of the document that contains information about the document such as title.
<img>	Represents an image.
<input>	Defines an input control.
<label>	Defines a label for an <input> control.
 <style>	Inserts style information (commonly CSS) into the head of a document.
  <table>	Defines a data table.
  <title>	Defines a title for the document.
   3. Describe the types of CSS selectors you know.
   The CSS element Selector
The element selector selects HTML elements based on the element name.

   The CSS id Selector
The id selector uses the id attribute of an HTML element to select a specific element. The id of an element is unique within a page, so the id selector is used to select one unique element! To select an element with a specific id, write a hash (#) character, followed by the id of the element.
   The CSS class Selector
The class selector selects HTML elements with a specific class attribute. To select elements with a specific class, write a period (.) character, followed by the class name.
   The CSS Universal Selector
The universal selector (*) selects all HTML elements on the page.
   4. Explain how you would implement the checklist above.
   1. First I create a new folder static for all the css file
   2. Look for a template I want online
   3. Implement it to the template I have
   Sources : login page : https://codepen.io/vlt_dev/pen/JjvpQNR
   register page : https://codepen.io/afirulaf/pen/ExgKpJ
