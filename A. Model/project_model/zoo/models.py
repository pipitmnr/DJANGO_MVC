from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    berat = models.IntegerField(default=0)
    umur = models.IntegerField(default=0)
    def __str__(self):
        return "Hewan %s" %(self.nama)

class Kandang(models.Model):
    nama = models.ForeignKey(Hewan, on_delete=models.CASCADE)
    isi_kandang = models.IntegerField(default=0)
    luas_kandang = models.IntegerField(default=0)
    def __str__(self):
        return "Kandang %s" %(self.nama)

class Penjaga(models.Model):
    nama = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=14)
    jadwal_jaga = models.CharField(max_length=100)
    def __str__(self):
        return "Penjaga %s" %(self.nama)

class Pengunjung(models.Model):
    nama = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=14)
    hari_berkunjung = models.DateField(null=True)
    def __str__(self):
        return "Pengunjung %s" %(self.nama)