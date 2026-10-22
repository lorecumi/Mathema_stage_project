from rest_framework import serializers

# questo serializer valida solo se il file in arrivo è valido, non svolge i controlli su tutti i required darta
class RecordSerializer(serializers.Serializer): 
    id = serializers.CharField(
        error_messages={
            "required": "Il campo 'id' è obbligatorio.",
            "blank": "Il campo 'id' non può essere vuoto.",
            "null": "Il campo 'id' non può essere null.",
        }
    )
    title = serializers.CharField(
        error_messages={
            "required": "Il campo 'title' è obbligatorio.",
            "blank": "Il campo 'title' non può essere vuoto.",
            "null": "Il campo 'title' non può essere null.",
        }
    )

