iniciar:
	pipenv install
	pipenv run python manage.py migrate
	pipenv run python manage.py createcachetable
	pipenv run python manage.py collectstatic

ejecutar:
	pipenv run python manage.py runserver


deploy:
	git remote add dokku dokku@trifulca.space:foro
	git push dokku master -f
