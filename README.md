# THE MOVIUM

THE MOVIUM is a python web app made using python3.6 and Flask framework. The app sources data from [TMDB API](https://developers.themoviedb.org) and displays movie information to the user. A user must have an account in the app to review a movie. Feel free to clone the project

# Installation
* Clone Project
* Navigate to the root folder of the app
* Activate a virtual environment
* Install all the dependencies needed.
* connect your database. [Read this](https://flask.palletsprojects.com/en/1.1.x/tutorial/database/)
* make executebe 'start.sh' and inside put the following lines:
```
export MOVIE_API_KEY=<your_movie_api_key>
export SECRET_KEY=<your_desired_secret_key>
python3.6 manage.py server
```
*  make the file executable.
* Access the live site at 127.0.0.1:5000 or the specified adress
* Or access the live site [here](https://themovium.herokuapp.com/)
```sh
$ git clone git@github.com:geoffrey45/Movium.git
$ cd Movium
$ . virtual/bin/activate
$ pip install -r requirements.txt
$ chmod a+x start.sh
$ ./start.sh
```
## Known Bugs

* No bugs

## Tools Used
* [Python3.6.9](https://www.python.org/downloads/release/python-369/)
* [Flask 1.12](https://flask.palletsprojects.com/en/)
* [HTML5](https://html5.org/)

## Support and contact details

geoffreymungai45@gmail.com

License
----
MIT free software! 