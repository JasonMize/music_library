from django.shortcuts import render, get_object_or_404

# from .models import Artist

def index(request):

    # music = music.objects.all()

    # context = {
    #     "music" = music
    # }

    return render (request, "music/index.html")


# def Artists (request, id):
#     artists = get_object_or_404(Student, pk=id)

#     context = {
#         "students":students
#     }

#     return render (request, "students/student.html", context)





