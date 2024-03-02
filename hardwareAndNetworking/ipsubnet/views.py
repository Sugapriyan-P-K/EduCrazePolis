from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
quiz = [2]
def index(request, number):
    fullPath = request.get_full_path().split('/')
    if (number == 2):
        return render(request, "quiz/quiz.html",{"topic" : fullPath[len(fullPath) - 4]})
    htmlPage = fullPath[len(fullPath) - 3]  + str(number)
    print(htmlPage)
    try:
        return render(request, f"ipsubnet/{htmlPage}.html",{"topic" : fullPath[len(fullPath) - 4]})
    except Exception:
        print(Exception)
        return HttpResponse("No More Pages! heheheheh!!:) Moje moore")