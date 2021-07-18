After installing pipenv, do: pipenv shell.

Then do these four commands:
pipenv install flask
pipenv install psycopg2-binary
pipenv install flask-sqlalchemy
pipenv install gunicorn

IN CASE LOCKING FAILS:
then delete Pipfile.lock and retry the command you just did.
