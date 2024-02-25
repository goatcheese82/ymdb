# Overview

This application was created using Django and PostgreSQL to keep track of members of the Young Men's organization in our stake. It has an admin section to add, edit, and delete stakes, wards, users, etc.

To test the application on your machine:

* Clone the repository to a directory on your computer
* cd into directory ymdb
* Be sure you have installed Python 3.8.10
* Install Django
* run `python manage.py runserver`

This software was written to organize the youth assignments and events for our stake.



[Software Demo Video](https://youtu.be/V1f9oXVZ5dI)

# Web Pages

The functioning pages are as follows:
Stake Detail page - This page produces a list of links to all the wards in the stake. This list is dynamically created, and is filtered to only display the proper wards.
Ward Detail page - This page produces a list of links to all the members in the ward, which is dynamically created and displayed.
User Detail page - This page produces information about a user.

Admin pages are also created, which are based on each object (class) in the application. All CRUD functions are accounted for in this section.

# Development Environment

To develop this software I used VSCode and the terminal in WSL2 using Ubuntu.

# Programming Language and Libraries

* Python 3.8.10
* Django 4.2.10

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Django Tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
* [Python Docs](https://docs.python.org/3.8/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Beautify the site
* Add events
* Add additional information to each page