import json, os, time
import requests
import firebase_admin
from firebase_admin import credentials, db

# Load Firebase key from Railway Secret
firebase_key = json.loads(os.getenv("FIREBASE_KEY"))
cred = credentials.Certificate(firebase_key)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://YOUR_PROJECT.firebaseio.com/'  # change to your Firebase DB URL
})

def fetch_live_data():
    # TODO: Replace with Pocket Option live fetch or screenshot analyzer
    return {"pair": "EURUSD", "price": 1.1050, "signal": "BUY"}

def push_to_firebase(data):
    ref = db.reference("signals")
    ref.push(data)

if __name__ == "__main__":
    while True:
        data = fetch_live_data()
        print("📊 Signal:", data)
        push_to_firebase(data)
        time.sleep(5)  # fetch every 5 seconds
