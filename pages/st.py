import pyrebase

config = {
    "apiKey": "AIzaSyCUa2zKFNRLe_JPAHlIgqgWkmK3qlOVnaM",
    "authDomain": "webp-bf95a.firebaseapp.com",
    "databaseURL": "https://webp-bf95a.firebaseio.com",
    "projectId": "webp-bf95a",
    "storageBucket": "webp-bf95a.appspot.com",
    "messagingSenderId": "474834831443",
    "appId": "1:474834831443:web:a09b081d29b01fba27dea6"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()