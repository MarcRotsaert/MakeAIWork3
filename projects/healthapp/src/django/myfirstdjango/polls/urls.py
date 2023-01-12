from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index2/", views.index2, name="index2"),
    path("happ/", views.healthapp_intro, name="happ"),
    path("happ/linkactivate/", views.healthapp_intro, name="linkactivate"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("crazyfrog/", views.crazyfrog, name="cf"),
    path("calc", views.calc, name="calc"),
]
