from pyrebase import pyrebase 
config = {
          "apiKey": "AIzaSyBH4q0c3Uygge--a8zNYS432wd_1DOxMD4",
          "authDomain": "courtsharing.firebaseapp.com",
          "databaseURL": "https://courtsharing.firebaseio.com",
          "projectId": "courtsharing",
          "storageBucket": "courtsharing.appspot.com",
          "messagingSenderId": "596174788055",
          "appId": "1:596174788055:web:072710db71f12870a2a792",
          "measurementId": "G-JX3QQ63MEL"
         }
firebase = pyrebase.initialize_app(config) 
auth = firebase.auth() 

