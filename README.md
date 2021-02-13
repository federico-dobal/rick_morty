# Rick and Morty web application

This is a light WebApp to search characters from Rick and Morty GraphQL API(https://rickandmortyapi.com/graphql)

## Features

It includes following features:

* List all characters
* Search partial characters names
* Search box with partial character names matching includes scroll bar
* The user can start the search from scratch by removing all the characters on the box


## Project set up

In order to set up the project the commands below should be executed:

       $ virtualenv venv_upload
       $ source venv_upload/bin/activate
       $ pip install -r requirements.txt

## How to start the WebApp?       
Simply by executing:

       $ cd rick_and_morty
       $ python manage.py runserver  

## How to access the service?
Open the browser on ip 127.0.0.1 or localhost and port 8000(http://127.0.0.1:8000/ or http://localhost:8000/)
