# Pocket Bot 🚀

This bot fetches live/screenshot data (demo version just returns dummy data)  
and pushes trading signals into Firebase Realtime Database.

## 🔧 Setup
1. Create a Firebase project → enable Realtime Database.
2. Generate a service account key (JSON).
3. On Railway → add a secret:
   - Key: FIREBASE_KEY
   - Value: paste the entire JSON key.

## 🚀 Deploy
- Upload this project to GitHub.
- On Railway → New Project → Deploy from GitHub.
- Bot will run automatically as a worker.
