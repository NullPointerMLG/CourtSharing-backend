# CourtSharing [Back-end]

# Information

This is a RESTful API service created with Flask, that is consumed by [this client](https://github.com/NullPointerMLG/CourtSharing-frontend).<br/>It gets data from a external service [Datos Abiertos de Málaga](https://datosabiertos.malaga.eu/), it parses it and returns the information to the client.
<br/>We also use it to store useful information such as user data.
<br/>
To get more information on how data is consumed, check out the [client](https://github.com/NullPointerMLG/CourtSharing-frontend).

# Where is it running?
It runs in a heroku repository, you can check it out [here](https://courtsharing-api.herokuapp.com/). However, as it uses firebase oauth in order to return information, you probably won't be able to get too much information from it.

# Installation:
1. Open a terminal
2. Create an environment:
```
#On linux
python3 -m venv venv

#On Windows
py -3 -m venv venv
```
3. Activate environment
```
#On linux
. venv/bin/activate

#On Windows
#If next command doesn't work run this on powershell: Set-ExecutionPolicy RemoteSigned
venv\Scripts\activate
```
4. Get dependencies
```
pip install -r requirements.txt
```
5. Export google credentials (Remeber to download it from firebase)
```
#On linux
export GOOGLE_APPLICATION_CREDENTIALS="/home/PATH/serviceAccountKey.json"

#On windows cmd
set GOOGLE_APPLICATION_CREDENTIALS="C:/PATH/serviceAccountKey.json"

#On windows powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="C:/PATH/serviceAccountKey.json"
```
6.Option1: Run Flask
```
python app.py
```
6.Option2: Run Flask with script
```
#On linux
./run.sh

#On windows
./run.ps1
```

Prerrequisites:
- Python 3.6.8


Dependencies:
 - Flask 1.1.1
 - Flask-RESTful 0.3.7
 - Flask-PyMongo 2.3.0
 - PyMongo 3.9.0
