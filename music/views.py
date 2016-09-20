from django.shortcuts import render, get_object_or_404

from .models import Artist

def index(request):

    # artists = Artist.objects.all()

    context = {
        # "artists" = artists
    }

    return render (request, "music/index.html", context)


# def Artists (request, id):
#     artists = get_object_or_404(Artist, pk=id)

#     context = {
#         "artists":artists
#     }

#     return render (request, "music/artist.html", context)





