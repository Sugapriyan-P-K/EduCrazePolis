from django.shortcuts import render
# from corsheaders import cors_allow_all, cors_allow_origin
# from corsheaders import cors_headers
# from django.utils import simplejson

# Create your views here.

# @corsheaders.middleware.cors_headers
def home(request):
    # js_data = simplejson.dumps(data)
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contributors(request):
    return render(request, "contributors.html")

def softwares(request):
    return render(request, "softwares.html")

def roadmaps(request):
    return render(request, "roadmaps.html")