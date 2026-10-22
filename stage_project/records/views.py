from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import HeritageRecord
from .serializers import RecordSerializer


@api_view(["GET", "POST"])
def record_list(request):
    if request.method == "GET":
        records = HeritageRecord.objects.order_by("id")
        return Response([record.data for record in records])

    serializer = RecordSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    record_id = serializer.validated_data["id"]
    title = serializer.validated_data["title"]

    if HeritageRecord.objects.filter(record_id=record_id).exists():
        return Response(
            {"id": [f"Esiste già un record con id '{record_id}'."]},
            status=status.HTTP_409_CONFLICT,
        )

    HeritageRecord.objects.create(record_id=record_id, title=title, data=request.data)
    return Response(request.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def record_detail(request, record_id):
    try:
        record = HeritageRecord.objects.get(record_id=record_id)
    except HeritageRecord.DoesNotExist:
        return Response(
            {"detail": f"Record con id '{record_id}' non trovato."},
            status=status.HTTP_404_NOT_FOUND,
        )
    return Response(record.data)