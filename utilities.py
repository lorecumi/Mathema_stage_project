#Conversione e controllo dei dati
def string_to_int(value, default: None):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def parse_type(source_rec: dict) -> dict:
    uri = source_rec.get("image_file")
    if uri and "." in uri:
        return uri.rsplit(".",1)[-1]

def raw_to_canon(source_rec: dict) -> dict:

    record_id = source_rec.get("inventory_id")
    record_title = source_rec.get("title")

    if not record_id:
        raise ValueError("ID not valid. Obligatory field")

    if not record_title:
        raise ValueError("Title not valid. Obligatory field")
    
    canonical = {
        "id": record_id,
        "title": record_title,
        "description": source_rec.get("description"),
        "classification": [
            {
            "object_type": source_rec.get("object_type"),
            "materials": source_rec.get("material"),
            "techniques": source_rec.get("technique"),
            }
        ],
        "temporal": [
            {
            "period": source_rec.get("period"),
            "fromYear": string_to_int(source_rec.get("date_from")),
            "toYear": string_to_int(source_rec.get("date_to")),
            }
        ],
        "location":{
            "label": source_rec.get("place"),
        },
        "condition": source_rec.get("condition"),
        "digitalResources": [
            {
            "type": parse_type(source_rec),
            "uri": source_rec.get("image_file")
            }
        ] 
    }
    return canonical

