from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=14)
    jabatan = models.CharField(max_length=50)
    def __str__(self):
        return "Direksi %s" %(self.nama)

class Mentee(models.Model):
    nama = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=14)
    no_absen = models.IntegerField(default=0)
    nilai = models.FloatField(default=0)
    def __str__(self):
        return "Mentee %s" %(self.nama)

class MataPelajaran(models.Model):
    nama = models.CharField(max_length=50)
    jadwal_mulai = models.DateTimeField('start')
    jadwal_berakhir = models.DateTimeField('finish')
    def __str__(self):
        return "Mata Pelajaran %s" %(self.nama)

class Mentor(models.Model):
    nama = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=14)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return "Mentor %s" %(self.nama)

class Challenge(models.Model):
    nama = models.CharField(max_length=50)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.FloatField(default=0)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return "Challenge %s" %(self.nama)

class LiveCode(models.Model):
    nama = models.CharField(max_length=50)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.FloatField(default=0)
    tgl_pelaksanaan = models.DateField(null=True)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return "Live Code %s" %(self.nama)