from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from .models import HeritageRecord


class RecordApiTests(APITestCase):
    url = "/api/records/"

    def valid_record(self):
        return {
            "id": "INV-T1",
            "title": "Anfora di prova",
            "classification": {"object_type": "anfora", "materials": ["terracotta"]},
        }

    def test_valid_record_is_saved(self):
        response = self.client.post(self.url, self.valid_record(), format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HeritageRecord.objects.count(), 1)
        saved = HeritageRecord.objects.get(record_id="INV-T1")
        self.assertEqual(saved.data, self.valid_record())

    def test_duplicate_record_is_not_inserted(self):
        self.client.post(self.url, self.valid_record(), format="json")
        response = self.client.post(self.url, self.valid_record(), format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(HeritageRecord.objects.count(), 1)

    def test_missing_required_fields_returns_400(self):
        response = self.client.post(self.url, {"id": "INV-T2"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertEqual(HeritageRecord.objects.count(), 0)

    def test_existing_record_can_be_retrieved(self):
        HeritageRecord.objects.create(
            record_id="INV-T3", title="Vaso", data={"id": "INV-T3", "title": "Vaso"}
        )
        response = self.client.get(self.url + "INV-T3/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"id": "INV-T3", "title": "Vaso"})

    def test_unknown_record_returns_404(self):
        response = self.client.get(self.url + "NON-ESISTE/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)