# fetch_points

### Installation instructions
* install python (3.5 or greater)
* (optional) set up virtual environment
```bash
$ python3.9 -m venv fetch_points
$ . fetch_points/bin/activate
```
* install flask and sortedcontainers libraries
```bash
$ pip install Flask
$ pip install sortedcontainers
```
* run the server
```bash
$ export FLASK_APP=fetch_points_server
$ flask run
```