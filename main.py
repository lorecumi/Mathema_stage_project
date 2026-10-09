import utilities
import json
import csv
from fastapi import FastAPI, HTTPException
import django



#Lettura file json
with open("data/week1/sample_metadata.json", mode="r", encoding="utf-8") as file_json:
    dati_json = json.load(file_json)
#Lettura file csv
with open("data/week1/sample_metadata.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    dati_csv = list(reader)

#Elaborazine dati secondo il modello canonico
# print("JSON TO CANON")
dataset_name = dati_json.get("dataset")
records_canonici_json = []

for r in dati_json["records"]:
    try:
        converted_json = utilities.raw_to_canon(r, dataset_name)
        records_canonici_json.append(converted_json)
    except ValueError as e:
        print(f"Error: Record {e} has been skipped.")


#print("CSV TO CANON")
records_canonici_csv = []

for r in dati_csv:
    try:
        converted_csv = utilities.raw_to_canon(r)
        records_canonici_csv.append(converted_csv)
    except ValueError as e:
        print(f"Error: Record {e} has been skipped.")





#Merging dei dati e print
dataset_unico = utilities.duplicates_check(records_canonici_json, records_canonici_csv)
# print(json.dumps(dataset_unico, indent=4))


app=FastAPI()

@app.get("/health")
def dataset():
    return {"status": "ok"}

@app.get("/records")
def show_all():
    return dataset_unico

@app.get("/records/{record_id}")
def show_id(record_id: str):
    for r in dataset_unico:
        if r["id"] == record_id:
            return r
    raise HTTPException(status_code=404, detail=f"ID '{record_id}' non trovato")