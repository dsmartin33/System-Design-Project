REQUIREMENTS YOU NEED TO RUN THE CODE:

You must have MariaDB installed for the Database.

You must have Python 3.12 installed that can run Django.

You must have an IDE installed that can run Python and Django code. I used PyCharm.


HOW TO RUN THE CODE:

1) Move the Project folder under your IDE.

2) Start IDE and Open the Project.

3) Make sure Python can connect to MariaDB.
	Create a new Data Source for MariaDB.
	You may have to install the MariaDB connector so the IDE can connect.

4) Once the IDE has connected to MariaDB, run the following commands:
	python manage.py makemigrations
	python manage.py migrate

5) Python should create a new database called, SystemDesignProject. If you receive an error, you may have to manually create the database. If so, please call it SystemDesignProject and re-run python manage.py migrate.

6) After this is created simply run the following command:
	python manage.py runserver

7) Go to http://127.0.0.1:8000/login/ and login using the following login information:
	Username: admin
	Password: admin123

	


