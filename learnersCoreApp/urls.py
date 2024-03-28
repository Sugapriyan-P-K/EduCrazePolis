from django.urls import path, include, re_path
from . import views

# app_name = "learnersCoreApp"hardwares
# print(category)
urlpatterns = [
    path('hardwares/', views.hardwares, name="hardwares"),
    path('softwares/', views.hardwares, name="softwares"),
    path('roadmaps/', views.hardwares, name="roadmaps"),
    re_path(r'^hardwares/(?P<subcategory>(ipsubnet|hardwareBasics|cpu|gpu|ram|motherboard|storageunit))/', include("learnersCoreApp.learningGame.urls")),
    re_path(r'^softwares/(?P<subcategory>(howCWorks|fundamentals|behindscenes|sorting))/', include("learnersCoreApp.learningGame.urls")),
    re_path(r'^roadmaps/(?P<subcategory>(frontendmap|backendmap|fullstackmap))/', include("learnersCoreApp.learningGame.urls")),
]
