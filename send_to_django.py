import requests

import main

DJANGO_URL = "http://127.0.0.1:8000/api/records/"


def send_records(records, url=DJANGO_URL):
    risultati = {"creati": 0, "duplicati": 0, "errori": 0}

    for record in records:
        try:
            response = requests.post(url, json=record, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Connessione fallita per '{record.get('id')}': {e}")
            risultati["errori"] += 1
            continue

        if response.status_code == 201:
            risultati["creati"] += 1
        elif response.status_code == 409:
            risultati["duplicati"] += 1
        else:
            risultati["errori"] += 1
            print(f"Record '{record.get('id')}' rifiutato ({response.status_code}): {response.text}")

    return risultati


if __name__ == "__main__":
    risultati = send_records(main.dataset_unico)
    print(risultati)