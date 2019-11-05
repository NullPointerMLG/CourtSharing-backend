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
. venv

#On Windows
venv\Scripts\activate
```
4. Get dependencies
```
pip install -r requirements.txt
```
5. Run Flask
```
#On linux
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

#On windows cmd
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Prerrequisites:
- Python 3.6.8


Dependencies:
 - Flask 1.1.1
