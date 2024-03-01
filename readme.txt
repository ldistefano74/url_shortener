To run the service (in a windows environment):
	create a virtual environment (python -m venv venv)
	install the required libraries requirements.txt (pip install -r requirements.txt)
	run the server (python shortener\manage.py runserver)

From Postman or browser use the following calls 
http://127.0.0.1:8000/store/?url=https://www.yahoo.com	-> to input information (will return the id)
http://127.0.0.1:8000/redirect/?id=a					-> to redirect to a specific id
http://127.0.0.1:8000/statistics						-> to get the statistics



Decisions I made:
 - In order to get code runing faster, I decided to store in site. This means that every time the server is restarted, new information must be placed
 - The central class Storage is an abstraction of the way to store. If a db is needed that class may be used as a virtual and implement a new one with proper db access
 - Some validations in the incoming requests (like valid url and id) where not included due to lack of time as well as the title retrievement from the stored url
 
 



