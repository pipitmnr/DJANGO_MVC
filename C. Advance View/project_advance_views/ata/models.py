from django.db import models

class Blog(models.Model):
    judul_blog = models.CharField(max_length=50)
    isi_blog = models.TextField()
    date_blog = models.DateField()
    img_blog = models.CharField(max_length=1000)
    def __str__(self):
        return "Blog %s" %(self.judul_blog)

class Mentor(models.Model):
    nama_mentor = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    quote_mentor = models.CharField(max_length=100)
    img_mentor = models.CharField(max_length=1000)
    def __str__(self):
        return "Mentor %s" %(self.nama_mentor)

class Mentee(models.Model):
    nama_mentee = models.CharField(max_length=50)
    quote_mentee = models.CharField(max_length=100)
    img_mentee = models.CharField(max_length=1000)
    def __str__(self):
        return "Mentee %s" %(self.nama_mentee)
