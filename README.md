# CourtSharing [Back-end]

Installation:
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
