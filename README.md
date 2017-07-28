# wwcw7
Testing Workshop for Women Who Code 2017/7/29

To start, you will need these if you haven't installed them already:

You might need libmysqlclient-dev if you're stuck. 

linux>> sudo apt-get install libmysqlclient-dev

The Windows equivalent can be downloaded at: https://dev.mysql.com/downloads/connector/c/

You'll also need sqlite3 installed:

linux>> sudo apt-get install sqlite3

Windows & Mac: https://www.sqlite.org/download.html

----------------------------------------

Run these commands in the same project directory:

>> python bootstrap.py

>> bin/buildout

>> bin/manage migrate

To run the web server:

>> bin/manage runserver

To view in your browser:

localhost:8000/

To look into your database:

>> bin/manage dbshell
