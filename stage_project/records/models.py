from django.db import models

# Create your models here.
from django.db import models

# elabora i dati dei json in ingresso confrontando e validando gli id
class HeritageRecord(models.Model):
    record_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    data = models.JSONField()

    def __str__(self):
        return f"{self.record_id} - {self.title}"