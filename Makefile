#make run	-	команда терминал
run:
	./manage.py runserver

#make migrate
migrate:
	./manage.py makemigrations 
	./manage.py migrate

superuser:
	./manage.py createsuperuser