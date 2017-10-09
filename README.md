# data_importer_firestore
Project to import json data into firestore storage

## Usage

    pip install virtualenv
    virtualenv env
    source env/bin/activate

    pip install --upgrade google-cloud-firestore

## Setup Credentials
Create a Service Account in Firebase "Users and permissions" section. Create a key and export to json.

    export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/keyfile.json"
    
    or add Environment variable in IntelliJ
