from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class Pos(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    kota = models.CharField(max_length=100, blank=True)
    kelurahan = models.CharField(max_length=100, blank=True)
    kecamatan = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tipe = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Reading(models.Model):
    id = models.AutoField(primary_key=True)
    pos_id = models.ForeignKey(Pos, on_delete=models.CASCADE)
    reading_value = models.FloatField()
    tipe = models.CharField(max_length=100)
    reading_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Predict(models.Model):
    id = models.AutoField(primary_key=True)
    pos_id = models.ForeignKey(Pos, on_delete=models.CASCADE)
    predict_value = models.FloatField()
    predict_for = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

