## Harfang Video Game server

This is a technical test for Harfang. It is a Flask server exposing endpoint to handle video Games in a Mongo DB.

#### How to Run


#### Tools to install

- Pyenv & python3.8
- poetry
- docker
- httpie (optionnal for making http requests)


#### RUN

- MongoDB : `docker run --name some-mongo -d mongo:4`
- Flask Server : `cd backend && poetry run flask run`
- Make a request : `http POST localhost:5000/games name=pablo2 release_date=01-01-2022 studio=pabStudio ratings=42 platforms=One platforms=Switch`


## Missing

- Unit testing of Usecase
- End to End testing of endpoints
