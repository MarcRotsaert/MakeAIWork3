from django.shortcuts import render
from django.http import HttpResponse
# from models import Question
from django.template import loader
import json
import logging
import sys
import os
from models.predict_model import Modelpredictor
from .models import Question
import models.train_model as tm
import storage.database as db

logging.basicConfig(level="DEBUG")

# sys.path.append(r"/src")


logging.debug(f"current directory : {os.getcwd()}")
# os.chdir(r"/src ")
# from __init__ import *

# os.chdir(r"../../../")

# os.chdir(r"/src\src")
# import data.database


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def index2(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("templates/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def crazyfrog(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    print(latest_question_list)
    context = {"latest_question_list": latest_question_list}
    return render(request, r"index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def healthapp_intro(
    request,
):
    print("")
    context = {"linkactivate": "lala"}
    return render(request, r"healtapp.html", context)


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calc(request):
    # print(os.environ["PYTHONPATH"])
    print(databasepath)
    print(os.getcwd())

    json_body = json.loads(request.body)
    print(json_body)
    # print(type(request.body))
    # print(request.POST)
    # alc = json_body["alcohol"]
    # print(alc)
    # xx

    df = db.dbdata2df(databasepath, "healthapp", "health")
    inputparam = ["genetic", "exercise", "smoking", "alcohol", "sugar", "bmi"]
    outputparam = "lifespan"
    trainer = tm.Modeltrainer(inputparam, outputparam)

    appmodel = trainer.linearregr(df)
    predictor = Modelpredictor(appmodel)
    # inputparam = predictor.return_featuresin()
    input_val = []
    for par in inputparam:
        input_val.append(float(json_body[par]))
    # args = [6 * request.body]
    # args[0] =
    val = predictor.predict([input_val])

    val = "{:.3}".format(val[0])
    # print(val)
    # print(predictor.return_featuresin())
    # print(args)
    # val = int(predictor.predict(args))

    # print(db.databasepath)
    # print(request.body)
    # result = int(request.body) * 2
    # print(result)
    return HttpResponse(val)


# Create your views here.
