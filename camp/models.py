from django.db import models
from django.utils import timezone

class SolData(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
    	return self.title

class SolViewData(models.Model):
    camdate = models.CharField(max_length=200)
    cametc = models.CharField(max_length=200)
    asite = models.IntegerField()
    bsite = models.IntegerField()
    csite = models.IntegerField()
    dsite = models.IntegerField()
    esite = models.IntegerField()

    class Meta:
        managed = False
        db_table = "solcamp"

class Main(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
    	return self.title
