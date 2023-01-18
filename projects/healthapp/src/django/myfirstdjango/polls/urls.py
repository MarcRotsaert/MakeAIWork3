from django.urls import path
from .views import index, index2, healthapp_intro, detail, results, vote, crazyfrog, calc
urlpatterns = [
    path("", index, name="index"),
    path("index2/", index2, name="index2"),
    path("happ/", healthapp_intro, name="happ"),
    path("happ/linkactivate/", healthapp_intro, name="linkactivate"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("crazyfrog/", crazyfrog, name="cf"),
    path("calc", calc, name="calc"),
]
