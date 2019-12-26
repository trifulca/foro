NOMBRE=spider-backend
N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

comandos:
	@echo ""
	@echo "${B}Comandos disponibles para ${G}${NOMBRE}${N}"
	@echo ""
	@echo "    ${G}iniciar${N}               Instala todas las dependencias."
	@echo "    ${G}ejecutar${N}              Ejecuta la aplicación de forma local."
	@echo "    ${G}deploy${N}                Actualiza la versión en producción."
	@echo ""



iniciar:
	pipenv install
	pipenv run python manage.py migrate
	pipenv run python manage.py createcachetable
	pipenv run python manage.py collectstatic

ejecutar:
	pipenv run python manage.py runserver


deploy:
	@echo "Agregando remoto para dokku y realizando push"
	git remote add dokku dokku@trifulca.com.ar:foro 2>/dev/null; git push dokku master -f
