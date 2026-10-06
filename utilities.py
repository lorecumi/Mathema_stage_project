#Conversione e controllo dei dati
def string_to_int(value):
    try:
        return int(value)
    except ValueError:
        return ValueError

def parse_type(source_rec: dict) -> dict:
    uri = source_rec.get("image_file")
    if uri and "." in uri:
        return uri.rsplit(".",1)[-1]

def raw_to_canon(source_rec: dict) -> dict:
    canonical = {
        "id": source_rec.get("inventory_id"),
        "title": source_rec.get("title"),
        "description": source_rec.get("description"),
        "classification": 
        {
            "object_type": source_rec.get("object_type"),
            "materials": source_rec.get("material"),
            "techniques": source_rec.get("technique"),
        },
        "temporal": {
            "period": source_rec.get("period"),
            "fromYear": string_to_int(source_rec.get("date_from")),
            "toYear": string_to_int(source_rec.get("date_to")),
        },
        "location":{
            "label": source_rec.get("place"),
        },
        "condition": source_rec.get("condition"),
        "digitalResources": {
            "type": parse_type(source_rec),
            "uri": source_rec.get("image_file")
        }  
    }
    return canonical

