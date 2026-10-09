#Conversione e controllo dei dati
def string_to_int(value, default = None):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def parse_type(source_rec: dict) -> dict:
    uri = source_rec.get("image_file")
    if uri and "." in uri:
        return uri.rsplit(".",1)[-1]

def required_check(value, name: str):
    if not value:
        raise ValueError(f"Error: '{name}' is an obligatory field!")

def raw_to_canon(source_rec: dict) -> dict:

    record_id = source_rec.get("inventory_id")
    record_type = source_rec.get("object_type")
    record_title = source_rec.get("title")
    record_materials = source_rec.get("material")
    record_techniques = source_rec.get("technique")
    record_source = parse_type(source_rec)
    record_uri = source_rec.get("image_file")
    
    required_check(record_id, "id")
    required_check(record_type, "type")
    required_check(record_title, "title")
    required_check(record_materials, "material")
    required_check(record_techniques, "technique")
    required_check(record_source, "source")
    required_check(record_uri, "uri")
    
    canonical = {
        "id": record_id,
        "title": record_title,
        "description": source_rec.get("description"),
        "classification":{
            "object_type": record_type,
            "materials": record_materials,
            "techniques": record_techniques,
            },
        "temporal":{
            "period": source_rec.get("period"),
            "fromYear": string_to_int(source_rec.get("date_from")),
            "toYear": string_to_int(source_rec.get("date_to")),
            },
        "location":{
            "label": source_rec.get("place"),
        },
        "condition": source_rec.get("condition"),
        "digitalResources": [
            {
            "type": record_source,
            "uri": record_uri
            }
        ] 
    }
    return canonical


def duplicates_check(list_1, list_2):
    controlled_id=set()
    clean_records=[]

    for i in list_1 + list_2:
        data_id=i["id"]
        if data_id not in controlled_id:
            controlled_id.add(data_id)
            clean_records.append(i)
    return clean_records