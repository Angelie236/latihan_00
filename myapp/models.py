from django.db import models

class StatusModel(models.Model):
    nama = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.nama
