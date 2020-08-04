[![Build Status](https://travis-ci.org/stormtrooper88/issue-tracker-milestone-project.svg?branch=master)](https://travis-ci.org/stormtrooper88/issue-tracker-milestone-project)

<h2><a href="https://tcb-issue-tracker-app.herokuapp.com/">Tracker</a> Full Stack Frameworks with Django-Milestone project</h2>

This project aims to show my work using the skills I have learnt during my undertaking of the course. In particular, the skills learnt whilst undertaking Django. I have created an issue tracker website in which users must register to use the following functions. The first function they will be able to use is to create, edit, and post a bug without paying for it. The second function the user will be able to do is request a feature which users will be able to create, edit, and request a feature which they will be required to pay for. This can be paid for by multiple users. The developer will decide the pricing for this feature. Finally, a checkout where the user can pay a sum for the feature they have requested. 
The aim is for users to post bugs they wish the developer to fix and features which the user will pay the developer to create. 

<h2>Why this Project?</h2>

I have created this project for the Full Stack Frameworks with Django Milestone Project of <a href="https://codeinstitute.net/">Code Institute’s</a> Full Stack Software Development course. The project was to create an online issue tracker. This would need to include a method for users to store and manipulate data records about bugs and features. The project is composed of multiple apps: accounts, bugs, cart, checkout, features, home, search finally tracker. There are several relationships between entities such as the user purchasing a feature. The project features several Django custom models There is also be an authentication mechanism which will require users to register and eventually log in. The reason for a user to sign up/ log in is they will not be able to post a bug or request a feature without having done so. There are several forms without a slight difference regarding whether the user wishes to post a bug or request a feature. The request a feature will require a payment whereas the report a bug will not. Stripe will be used for the checkout function as a means of payment for a feature, the user then will be told by the admin how a given date for the feature to be finished. The idea is if the user cannot pay in full, other users can contribute to this payment to reach the given price. For the main navigation menu and structure, Bootstrap has been used to accomplish this. The front end has JavaScript logic to enhance the user experience.  

The Front-End display and functionality use Bootstrap, CSS, HTML, Font Awesome and JavaScript. On the Back-End functionality I have used Postgres, Django, stripe, and Python. The final deployment will be done using Heroku. 

<h2>UX</h2>

User Stories:

•	As a user, I want to be able to register on the website. 

•	As a user, I want to be able to log in on the website.

•	As a user, once I have been logged in, I want to be able to post a bug on the website. 

•	As a user, once I have been logged in, I want to be able to edit my bug on the website.

•	As a user, I want to be able to search for bugs and features on the website. 

•	As a user, once I have logged in, I want to be able to request a feature on the website.

•	As a user, once I have logged in, I want to be able to edit my request of feature on the website.

•	As a user, once I have logged in, I want to be able to pay for the feature I have requested.


<h2>Wireframes</h2>

I worked on my wireframes before starting to create this project. I made several wireframes using Balsamiq focusing on the home page, sign up, log in, bug, bug edit, feature, feature edit, cart and checkout pages. You can find these wireframes <a href="https://github.com/stormtrooper88/issue-tracker-milestone-project/blob/master/Wireframes/issue%20tracker.pdf">here</a>. 

Features:

Existing Features:

Sign up:

Here the user can sign up. The user will be asked to create a new account with the following fields to be completed. They are as follows: email address, username, password, and password confirmation. The user then clicks on “create account” which will 

Log in:

Here the user can log in to their account. The user will be asked for their username and password. If these are incorrect, the user will be told so. The user can also request a new password if they have forgotten their password. 

Bug:

Here the user can describe a bug they are encountering. 

Edit a bug:

Here the user can edit a bug they are encountering. 

Feature:

Here the user can describe a feature they wish to have created. 

Edit a feature:

Here the user can edit a feature they wish to have created. 

Cart:

Here the user can view the feature they are about to pay for and input the number of features they wish to pay for.

Checkout:

Here the user can pay a fee for the feature so that it is created.  


Features Left to Implement:

•	A feature I would have liked to have had is to create a page that contains some graphs showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features. To enhance the user experience, use dc.js (or any other js approach) to create dynamic charts.

•	A feature I would have liked to include is to add pages describing my fictional UnicornAttractor application.

•	A feature I would have liked to have added is an email listing that would be sent out with new features that could be implemented with a pricing on how close they are to be paid for and so be created. 

•	A feature I would have liked to have added is an upvote for the bugs and features. 

	Technologies Used:
•	<a href="https://getbootstrap.com/">Bootstrap</a>
•	<a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets">CSS</a>
•	<a href="url">Django</a>
•	<a href="https://fontawesome.com/?from=io">Fontawesome</a>
•	<a href="https://www.w3schools.com/html/">HMTL</a>
•	<a href="https://www.javascript.com/">Javascript</a>
•	<a href="https://pypi.org/project/Pillow/2.2.1/">Pillow</a>
•	<a href="https://www.heroku.com/postgres">PostgresSQL</a>
•	<a href="https://www.python.org/">Python</a>
•	<a href="https://www.sqlite.org/index.html">SQLite</a>
•	<a href="https://stripe.com/">Stripe</a>


<h2>Testing:</h2>

1.	Sign up: 

i. I went to the "Register” in the top right-hand corner. Alternatively, the user can click on the blue highlighted “register” which will also take them to the register page”. 

ii.	I tried to submit the empty form which verified that an error message about the required fields appears.

iii. I tried to submit without completing each section of the form to verify that an error appears on the fields missed out. 

iv.	I tried to submit the form with all inputs valid and get sent to the accounts index were a “Success!” message is shown. Below that I am told the email I logged in as and the options of report a bug or feature.

2.	Log in: 

i.	I went to the "Log In” in the top right-hand corner. Alternatively, the user can click on the blue highlighted “log in” which will also take them to the register page”. 

ii.	I tried to submit the empty form which verified that an error message about the required fields appears.

iii. I tried to submit without completing each section of the form to verify that an error appears on the fields missed out. 

iv.	I tried to submit the with an incorrect password and I get the message “Your username or password are incorrect”.

v.	I tried to submit with the correct username and password and get the message “Success!”.  Below that I am told the email I logged in as and the options of report a bug or feature.

vi.	I clicked on “Log Out” and get the message “You have been successfully logged out”. 

3.	Adding a bug: 

i.	I went to the "Report a bug” in the top right-hand corner. Alternatively, the user can click on the blue highlighted “bug” on the profile page. 

ii.	Here I need to name, describe, and give a tag for the bug before clicking on the “Post your bug”. 

iii. I tested here by trying to submit the form, Test but I was told that name was missing. 

iv.	I then tried to give a name and submit but was told that description was missing.

v.	I tried to submit without posting a tag and this was accepted. 

4.	Edit a bug:

i.	I went to the "Bug” page. Alternatively, the user can click on the blue highlighted “bug” on the profile page. 

ii.	Here I can “Read more” on the bug posts made already. 

iii. Upon clicking on this, I am shown a brief description including “created on, expected to be fixed by and Tag”. Here I can click on “Edit a Bug” or “Back to Bugs”. 

iv.	Clicking on “Edit a Bug”, I am taken to the post where I can edit the name, description, and tag. 

5.	Adding a feature:

i.	I went to the "Request a feature” in the top right-hand corner. Alternatively, the user can click on the blue highlighted “feature” on the profile page. 

ii.	I am then taken to a page where I can name, describe, and give the tag a feature.

iii. I tried to submit without giving the feature a name and was told it needed to be filled out.

iv.	I tried to submit without the feature a description but having a name and was told the feature needed a description. 

v.	I tried to submit without the feature having a tag and this was successful. 

vi. Once I added the feature, I had the option either "return to features", "edit a feature" and finally "view my cart". 

6.	Editing a feature:

i.	I went to the "Feature” page. Alternatively, the user can click on the blue highlighted “feature” on the profile page. 

ii.	Here I can “Read more” on the feature posts made already.

iii.	Upon clicking on this, I am shown a brief description including “created on, expected to be fixed by and Tag”. Here I can click on “Edit a feature” or “Back to features”.

iv.	Clicking on “Edit a feature”, I am taken to the post where I can edit the name, description, and tag of that given feature. 

v.	Upon making the changes I need to make; I can post the feature with these changes. 

7.	Using the checkout:

i.	I went to the "Check your cart” page. Alternatively, the user can click on the blue highlighted “feature” on the profile page. 

ii.	Here I can see the feature I wish to buy and request the number of the feature i wish to buy. 

iii. I can then click on the “checkout” button. This then takes me to checkout page where I need to fill in the following: Full name, phone number, country, postcode, town or city, street address 1, street address 2, county, credit card number, security code, month and year. 

iv.	I tried to submit without filling out the form however I told to fill out full name. This is then repeated for every single column, bar Postcode, until they are all filled out. 

v.	Once this is paid, the user is informed of the payment bieng successful via a message and redirected to the features page. 

<h2>Database Schema</h2>

•	The database used is SQLite where all the data will be stored at the start. Once the project was moved to Heroku, the database used was PostgresSQL. 


<h2>Deployment:</h2>

Github : This project was started by downloading the Code Institute <a href="https://github.com/Code-Institute-Org/gitpod-full-template">full template</a>. This served as the starting point before being worked on and finally being deployed to Heroku.

Heroku : The difference between the development and deployed version is that in development I used SQLite as the database whereas for the deployed version I used PostgresSQL as the database. This was run using Python3. 


<h2>Github</h2>

To clone the code used in this project you can do as following: 

to run the code locally then you can clone my git repository and run it an editor such as Visual Studio Code. Simply past git clone https://github.com/stormtrooper88/issue-tracker-milestone-project into your terminal. Once you have done this you will want to stop the connection with the GitHub repository. You do this by typing into your terminal git remote rm origin. Alternatively, you can press the “clone or download” button on the link above that will allow you to clone the work. 

<h2>Credits</h2>

Content

•	All content is of my own work through the videos provided by Code Institute’s  E-commerce mini and Blog projects. 

Media

•	No photos or videos were used within this project.

Acknowledgements

•	I would like to acknowledge the tutor support that now extends to my time zone and their patience with my questions. Especially Michael, Miklos and Tim. 

•	I would also like to acknowledge my mentor, Dick, who has helped me throughout the course and the support system in place at code institute who regularly had calls to see how I was progressing with the course. 
