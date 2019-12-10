from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Mentor, Mentee
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'ata/index.html')
def blog(request):
    blogs = Blog.objects.all()
    data_blog = {'blogs': blogs}
    return render(request, 'ata/blog.html', data_blog)
def addBlog(request):
    return render(request, 'ata/add-blog.html')
def postBlog(request):
    judul_blog = request.POST['judul_blog']
    isi_blog = request.POST['isi_blog']
    date_blog = request.POST['date_blog']
    img_blog = request.POST['img_blog']
    post = Blog(judul_blog=judul_blog, isi_blog=isi_blog, date_blog=date_blog, img_blog=img_blog)
    post.save()
    blogs = Blog.objects.all()
    return redirect('blog')
def mentee(request):
    mentees = Mentee.objects.all()
    data_mentee = {'mentees': mentees}
    return render(request, 'ata/mentee.html', data_mentee)
def mentor(request):
    mentors = Mentor.objects.all()
    data_mentor = {'mentors': mentors}
    return render(request, 'ata/mentor.html', data_mentor)
def author(request):
    return render(request, 'ata/author.html')