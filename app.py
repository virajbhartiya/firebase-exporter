import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("SERVICE.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def export_collection(collection_name):

    collection_ref = db.collection(collection_name)

    docs = collection_ref.stream()

    data = {}

    for doc in docs:
        data[doc.id] = doc.to_dict()

    return data


def export_firestore_data():
    collections = ["Collection1"]

    all_data = {}

    for collection in collections:
        all_data[collection] = export_collection(collection)

    with open("firestore_export.json", "w") as f:
        json.dump(all_data, f, indent=4)

    print("Data exported to firestore_export.json")


if __name__ == "__main__":
    export_firestore_data()
