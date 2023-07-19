Meshmerize - Device Registration Task
==================

This is just Task project, provided by the Meshmerize.

Getting Started
***************

Used Tech Stack
-----------------------------------
    - Django Rest Framework
    - SQLite3 database
    - Javascript
    - Ajax
    - Twitter Bootstrap
    - HTML 5

API Documentation
-----------------------------------
    https://documenter.getpostman.com/view/25458535/2s946h9t2m


Installation
-----------------------------------
Install the all dependecies from the requirments.txt in the virtual environment::
    - Open a Project directory in command prompt
    - create a virtual environment
    
        >>> python -m venv venv # second venv stands for virtual environment name
        >>> .\venv\Scripts\activate # To activate the Virtual environment (in windows)


- After that simply install all the dependent packages::

        >>> pip install -r requirments.txt


PS: I have alredy given DB file here. So, you don't need to perform a migrations. You can directly run server.


Start the Project
--------------------------------------
To start the project we need to run the server, and for that::

    >>> python .\manage.py runserver
        
Now, just simply hit the ``http://127.0.0.1:8000/``. You'll redirected to the Homepage.

NOTE:
--------------------------------------

I haven't used any authentication, but as you mentioned in the task, I had to use API key (static). So, I have fixed a key same for all users, which only needed when some changes occured into the database. For example: ``/api/add-device`` and ``/api/delete-device/<str:pk>``

Future Updates
-----------------------------------

    + Authentication Can be possible
    + Auto Fetching MAC Address
    + User rights differentiations
    + Dynemic API Key/ Beaver Token
    + UI: Pagination / All Operation throught UI
    + Proper Structure for Whole Project
