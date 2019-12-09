from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=14)
    bidang = models.CharField(max_length=50)
    jadwal_praktek = models.CharField(max_length=100)
    def __str__(self):
        return "Dokter %s" %(self.nama)

class Pasien(models.Model):
    nama = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=14)
    alamat = models.CharField(max_length=100)
    keluhan = models.CharField(max_length=100)
    def __str__(self):
        return "Pasien %s" %(self.nama)

class Obat(models.Model):
    nama = models.CharField(max_length=50)
    kandungan = models.CharField(max_length=100)
    khasiat = models.CharField(max_length=100)
    def __str__(self):
        return "Obat %s" %(self.nama)

class Resep(models.Model):
    nama = models.CharField(max_length=50)
    total_harga = models.CharField(max_length=10)
    kumpulan_obat = models.ManyToManyField(Obat)
    def __str__(self):
        return "Resep %s" %(self.nama)