import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase

# Variável global para armazenar a instância do cliente do Firestore
db = None
auth = None
storage = None


def initialize_firebase_app():
    global db

    firebaseconfig2 = {
        "type": "service_account",
  "project_id": "iot2023-8c540",
  "private_key_id": "c6aff041306b200b913f84ac6b335f11b65d3b5b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDKSRK4esq8VQEq\ndhp8jJL1dlyNeBzdBaDDeHHzCpigrGMF07uuj11exkA4OLbJrzs1nQXlngl/jI0I\n+tM3YFpWHq5y845Umr7+xBUim2Yx15icV7BI0WwPrdacthigX1XrYX0YJrn9RthT\n5mm9toMLINr/P6iRVCa1cJz6rG1kdGB5WcJjZlbWzGuYQi2rxwldEsxlCoSVXrtX\ns+ybyzEV/aEnnJgHCLLVfVMGXjrBrm0yjKKI/6RtsNPzJ8RdBfuESn/NFsEWG3n0\nOEsHwnsP9WVpcU0gPrH95552Itb2jyZ3J9DIW4B+TRTcltiwnQjTK7Lg53NjuAlD\ng8YjjkIbAgMBAAECggEACwubaJRX3pm7oxBo2NUqLxoD6rucw9rLUPESM8Wn2Nog\n3BAYJutwGz0zA37hSDj3wDEvQb7z4NGRX+SmRNdPh3VMbD1tT6RVen7FcqrOlTki\n/aJyHz/EKUUCO3Nb++HIxL4BgSCYNkK4jDhAHNpK5IAqRRa6Qxk3td+MyslAfeQe\nB2Yq2zIpOJ74z7bsgPUYlnnDDA39j7Lc0YGfEztQtA3yOwFJVc39XsO2ZAlz7ZgL\nM+0qf4bOn0qkNODjN+x1XR9YxhY/LhjNGKuxEpaXbR/Zvt9dzTbX8hpMGbOxbTjs\nGemxX2iDjZbRlmsyF52HRa1BqBsLsypnhJDPQoyVMQKBgQDnvUSzJTk6vKvRNC2n\neTzFBPnvnRTTgVkgSEx1kXPgIUfy9qst3u1bk2GrsJFknEzo8fRpGxZQex1iWKhZ\nbG0dfcqgJ36KJz29Var2BDg/5kfe5BKvecJedX8DC2VsWfly77qdwZWwteB2MkaH\n9Z3rtC9Np1KdpUej59VlxPePsQKBgQDfdmz2P//L0Nu3bBNdLb1p5YoI03mHUnHO\nZfhJ39rqajyLrWsmC67N/mQcY8wNVaKz3PyiQUkSRK7g/L+5Sa99Fcss12tpl+mi\nVL1aSaLEiWmAdcQm7ToI2cQgOlvmharjpn0q73WVixbeUUOUq22mB+CB4sp3g0T1\ngpMY11tNiwKBgQDhyOGfndvlo5/QBAObUZ9o4lFWKXj6HeOldWuxfNcmf6anTbg4\nyCQA/lbCPhVaroKsz9jvcynJnjph8LmN7vtdKYt7gR9kIZmg2E/qxO+9KnPJ8fNW\nrs421Em8wKS/7eYCGxp6y/s5oeshnhhkLWYBGZyhDy6KVFe5lY6wSjld8QKBgQDD\niXoxRLFNpNYOO6j6GSMsvem6bWpjalYhmILaCeMiypFuW/JtmT1+DYOGgCE27d9w\nagg65svNC4LHZwNRXFQOLXrbIylffcm3/VSv481lEyTZfrOEqILm6b8/wDFYl1CA\n4deXMXB/yfTZ1tw/BH7vEOd4YH5wc9JszrRuwUuonwKBgQDHBN5FR6KVhNWZS8Vp\nhffIazqJe2NLzrquHj0If2HdIUVgkzly2c9Kct3AQmxbtpxxrKxqCXvgkdqPj+YA\nEb+tQM73ckuuFZISAgfb7K++x83/VGHvsddPJWIxuRZ/SzzH+F+VjYQWVIrbsUio\nBQypiPTEa1ZFi9bmLuL86gPadw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-44plm@iot2023-8c540.iam.gserviceaccount.com",
  "client_id": "112410492055437215857",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-44plm%40iot2023-8c540.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
    }


    if not firebase_admin._apps:

        cred = credentials.Certificate(firebaseconfig2)
        firebase_admin.initialize_app(cred)
        db = firestore.client()


def get_firestore_client():
    return db



def initialize_firebase_app_auth():
    global auth, storage

    firebaseconfig = {'apiKey': "AIzaSyAcVKENEblNpDqYTJ7B0E-v5Sxi39z2tTc",
                        'authDomain': "iot2023-8c540.firebaseapp.com",
                        'databaseURL': "https://iot2023-8c540-default-rtdb.firebaseio.com",
                        'projectId': "iot2023-8c540",
                        'storageBucket': "iot2023-8c540.appspot.com",
                        'messagingSenderId': "655471695383",
                        'appId': "1:655471695383:web:e13c3f5610a4b17c516e52",
                        'measurementId': "G-Q766ESNKHF"}

    firebase = pyrebase.initialize_app(firebaseconfig)
    auth = firebase.auth()
    storage =firebase.storage()


def get_firestore_client_auth():
    return auth

def get_firestore_client_storage():
    return storage




