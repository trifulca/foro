iniciar:
	pipenv install
	pipenv run python manage.py migrate
	pipenv run python manage.py createcachetable
	pipenv run python manage.py collectstatic

ejecutar:
	pipenv run python manage.py runserver


deploy:
	@echo "Agregando remoto para dokku y realizando push"
	git remote add dokku dokku@trifulca.space:foro 2>/dev/null; git push dokku master -f
