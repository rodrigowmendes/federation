# Federation

A REST API for United Federation Of Planets database, including known planets, species, languages, starships of the Starfleet, their classes and crewmen.

![Starfleet Model](https://github.com/rodrigowmendes/federation/blob/master/starfleet/static/images/starfleet_uml.png)

## Endpoints

Starship classes: starfleet/starshipclasses/

Starships: starfleet/starships/

Crewmen: starfleet/crewmen/

Languages: starfleet/languages/

Planets: starfleet/planets/

Species: starfleet/species/

## Usage

Install pip3:

`apt install python3-pip` 

Then run after clone the repository:

``` bash
cd federation

pip3 install requirements.txt`

python3 manage.py migrate # To migrate the database

python3 manage.py runserver
```



