# Mathema Stage Project

Progetto composto da due servizi:
- **FastAPI** (cartella principale): legge i file JSON/CSV e li trasforma nel canonical model.
- **Django REST Framework** (`stage_project/`): riceve i record, li valida e li salva in SQLite.

## Requisiti
Due ambienti virtuali separati, uno per servizio.

- Django: `pip install django djangorestframework`
- FastAPI: `pip install fastapi uvicorn requests`

## Avvio di Django
```
cd stage_project
python manage.py migrate
python manage.py runserver
```
Il servizio risponde su http://127.0.0.1:8000/api/records/

## Avvio di FastAPI
```
uvicorn main:app --port 8001
```
Il servizio risponde su http://127.0.0.1:8001/records
(La porta 8001 evita il conflitto con Django.)

## Inviare i record a Django
Con Django acceso e dal venv di FastAPI:
```
python send_to_django.py
```
Stampa quanti record sono stati creati, quanti erano già presenti e quanti hanno dato errore.

## Endpoint Django

| Metodo | URL | Descrizione | Risposte |
|--------|-----|-------------|----------|
| POST | /api/records/ | Salva un record canonico | 201 salvato, 400 campi mancanti, 409 id duplicato |
| GET | /api/records/ | Elenca tutti i record | 200 |
| GET | /api/records/<id>/ | Restituisce un record | 200, 404 se non esiste |

## Test
```
cd stage_project
python manage.py test
```
Copre: record valido salvato, duplicato rifiutato, campi obbligatori mancanti (400), record inesistente (404).

Verifica manuale della persistenza: riavviare Django e controllare che i record siano ancora presenti con GET /api/records/.