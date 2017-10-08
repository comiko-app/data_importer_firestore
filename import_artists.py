import json
from google.cloud import firestore

with open('artists.json') as data_file:
    artists = json.load(data_file)

db = firestore.Client()

for artist in artists:
    doc_ref = db.collection(u'artists').document()
    doc_ref.set(artist)

