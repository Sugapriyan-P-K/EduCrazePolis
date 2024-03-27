from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
quiz = [2]
def start(request, number, subcategory=None):
    fullPath = request.get_full_path().split('/')
    path = ""
    if subcategory:
        path = subcategory
    else:
        path = fullPath[len(fullPath) - 4]
    print(fullPath)
    print(path)
    if (number == 2):
        return render(request, "quiz/quiz.html",{"topic" : path})
    htmlPage = fullPath[len(fullPath) - 3]  + str(number)
    print(htmlPage, "kjhgkjdfhgfdkjg jsjhkjghkgfdjhkfgdjhk ")
    try:
        return render(request, f"{path}/{htmlPage}.html", {"topic": path})
    except Exception as e:
        print(e)
        return HttpResponse("No More Pages! heheheheh!!:) Moje moore")