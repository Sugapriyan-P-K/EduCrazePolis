from django.shortcuts import render
from users.forms import UpdateUserForm

# Create your views here.

def home(request):
    try:
        user_form = UpdateUserForm(instance=request.user)
    except Exception as e:
        user_form = None
    print(user_form)
    return render(request, "home.html", {'user_form' : user_form })

def about(request):
    return render(request, "about.html")

def contributors(request):
    return render(request, "community.html")


def roadmaps(request):
    return render(request, "roadmaps/roadmaps.html")
