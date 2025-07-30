from django.shortcuts import render

from .models import Movie
# Create your views here.


def movies(request):
    return render(request, "movies/index.html", {
        "movies": Movie.objects.all()
    })


