from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import movieform

from .models import Movies


# Create your views here.
def index(request):
    movie = Movies.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        names = request.POST.get('name')
        descs = request.POST.get('desc')
        years = request.POST.get('year')
        more=request.POST.get('m_desc')
        image = request.FILES['img']
        movie = Movies(name=names, desc=descs, year=years, img=image,m_desc=more)
        movie.save()
    return render(request, 'add.html')


def update_movie(request, id):
    movie = Movies.objects.get(id=id)
    form = movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete_movie(request, id):
    if request.method=='POST':
         movie=Movies.objects.get(id=id)
         movie.delete()
         return redirect('/')
    return render(request,'delete.html')

