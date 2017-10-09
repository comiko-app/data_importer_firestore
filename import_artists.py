import json
import uuid
from google.cloud import firestore

with open('artists.json') as data_file:
    artists = json.load(data_file)

db = firestore.Client()

for artist in artists:
    artist["id"] = str(uuid.uuid4())
    doc_ref = db.collection(u'artists').document(artist["id"])
    doc_ref.set(artist)

