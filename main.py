import utilities
import json
import csv
from fastapi import FastAPI



#Lettura file json
with open("data/week1/sample_metadata.json", mode="r", encoding="utf-8") as file_json:
    dati_json = json.load(file_json)
#Lettura file csv
with open("data/week1/sample_metadata.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    dati_csv = list(reader)

#Elaborazine dati secondo il modello canonico
print("JSON TO CANON")
records_canonici_json = []

for r in dati_json["records"]:
    converted_json = utilities.raw_to_canon(r)
    records_canonici_json.append(converted_json)


print("CSV TO CANON")
records_canonici_csv = []

for r in dati_csv:
    converted_csv = utilities.raw_to_canon(r)
    records_canonici_csv.append(converted_csv)


#Merging dei dati e print
dataset_unico = records_canonici_json + records_canonici_csv
# print(json.dumps(dataset_unico, indent=4))

# LANCIARE IL SERVER: uvicorn main:app --reload
app=FastAPI()

@app.get("/")
def dataset():
    return {"status": "ok"}

@app.get("/records")
def show_all():
    return dataset_unico