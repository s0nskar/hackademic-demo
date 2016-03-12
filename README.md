# hackademic-demo

a mini demo version of hackademic for testing purpose written using Django framework and Lettuce.

1. git clone https://github.com/sanskar-modi/hackademic-demo.git
2. virtualenv venv
3. source venv/bin/activate/
4. pip install -r requirements.txt
5. ./manage.py migrate
6. python populate_db.py
7. ./manage.py runserver

Credentials for login:
			username    password
Student:  		a 		1234
Teacher:		b 		1234
Admin:			c 		1234

For Testing purposes: (Under construction)

run ./manage.py harvest --test-server

Last two test cases are not working properly will be fixing them asap!! :)
Suggestions are welcome!!