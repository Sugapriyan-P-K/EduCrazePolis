from django.shortcuts import render
# from corsheaders import cors_allow_all, cors_allow_origin
# from corsheaders import cors_headers
# from django.utils import simplejson
from users.forms import UpdateUserForm

# Create your views here.

# @corsheaders.middleware.cors_headers
def home(request):
    # js_data = simplejson.dumps(data)
    try:
        user_form = UpdateUserForm(instance=request.user)
    except:
        user_form = None
    print(user_form)
    return render(request, "home.html", {'user_form' : user_form })

def about(request):
    return render(request, "about.html")

def contributors(request):
    return render(request, "community.html")

# def softwares(request):
#     return render(request, "softwares/index.html")

def roadmaps(request):
    return render(request, "roadmaps/roadmaps.html")
