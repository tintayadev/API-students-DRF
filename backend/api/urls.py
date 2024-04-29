from django.urls import path
from .views import index, import_students_from_excel


urlpatterns = [
    path("index/", index, name="Index"),
    path("import-data/", import_students_from_excel, name="Import data")
]
