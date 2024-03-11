from django.shortcuts import render

# Create your views here.

def hardwares(request):
    print(request)
    return render(request, "hardwareAndNetworking/hardwares.html")
