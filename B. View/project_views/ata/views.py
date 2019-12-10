from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'ata/index.html')
def blog(request):
    return render(request, 'ata/blog.html')
def mentee(request):
    return render(request, 'ata/mentee.html')
def mentor(request):
    return render(request, 'ata/mentor.html')
def author(request):
    return render(request, 'ata/author.html')