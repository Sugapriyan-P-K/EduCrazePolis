from django.shortcuts import render

# Create your views here.

def hardwares(request, category=None):
    # print(remainder)
    print(category, "category")
    print(request.get_full_path().split('/'))
    learnerDivision = request.get_full_path().split('/')[-2]
    print(learnerDivision)
    return render(request, "allContent/index.html", { 'category' : learnerDivision })
