# SWGRAPH
## Idea

Original idea create api around star wars api belong to [phalt](https://github.com/phalt) ([live server](https://swapi.co/)).

I see it in 2018 and get idea about remix it used graphQL for queries to API([graphene-python](http://docs.graphene-python.org/projects/django/en/latest/) realization).


## Development

### Database
By default it use PostgreSQL database. 
If you would like use default settings, then you must create user `swgraph` with password `swgraph` and assign it 
as owner to `swgraph` database.   

### Server dependencies

This project tested on python 3.6, but maybe it will work in correct way version of python 3.4 and up.
Hightly recommended install requirements in virtual environment, you can create it used follow command: `python3 -m venv .venv`.

After this install requirements `pip install -r requirements.txt` inside backend folder.

### Order of installing fixtures
For installing all fixtures, you must next commands

`python manage.py loaddata planets.json`

`python manage.py loaddata people.json`

`python manage.py loaddata species.json`

`python manage.py loaddata transport.json`

`python manage.py loaddata starships.json`

`python manage.py loaddata vehicles.json`

`python manage.py loaddata films.json`
