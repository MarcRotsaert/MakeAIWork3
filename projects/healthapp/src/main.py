import os

print(os.getcwd())

import sys
from __init__ import *

import data.webscraping as scrape
import visualization.visualize as vi
import data.make_dataset as md
import data.database as db
import models.train_model as tm
import models.predict_model as pm
from matplotlib import pyplot as pp
import pprint

# xx
# print(datapath)
# print(srcpath)
# print(modelspath)
print(os.getcwd())


def dbupdate():
    # Update db with newly scraped data.
    print(dbname)
    blob = scrape.scraping(url)
    tit, data = scrape.decode(blob)
    dfraw = scrape.data2df(tit, data)
    pp_data = md.Preprocess(dfraw)
    dfnew = pp_data.set_bmi()

    db.updatesql(databasepath, dbname, tablename, dfnew)


def make_prediction():
    # Make Prediction
    df = db.dbdata2df(databasepath, "healthapp", "health")
    inputparam = ["genetic", "exercise", "smoking", "alcohol", "sugar", "bmi"]
    outputparam = "lifespan"

    model = tm.Modeltrainer(inputparam, outputparam).linearregr(df)
    predictor = pm.Modelpredictor(model)
    res = predictor.predict(df[inputparam])
    pprint.pprint(res)
    diff = df["lifespan"] - res
    print(diff.max())
    print(diff.min())
    print(diff.mean())


if __name__ == "__main__":
    url = "https://medisch-centrum-randstad.netlify.app/"
    dbname = "healthapp"
    tablename = "health"

    # print(os.environ.keys())
    # dbupdate()
    if sys.argv[1] == "UPDATE":
        # path = os.environ["HOME"]
        os.chdir("../../..")
        print(os.getcwd())
        # xx
        dbupdate()
    # print("nodieno")
    if sys.argv[1] == "PREDICT":
        print("yes")
        # makedescrstats()

    make_prediction()
    # pass
