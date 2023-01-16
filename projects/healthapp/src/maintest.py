import os

print(os.getcwd())

from __init__ import *

import data.webscraping as scrape
import visualization.visualize as vi
import data.make_dataset as md
import data.database as db
import models.train_model as tm
import models.predict_model as pm
from matplotlib import pyplot as pp

# xx
# print(datapath)
# print(srcpath)
# print(modelspath)
print(os.getcwd())
import numpy as np


# def dbdata2df(colnames=None):
#     inst_sql = db.Sqlite(databasepath, "healthapp", "health")
#     temp = []
#     if colnames == None:
#         colnames = inst_sql.get_colnames()
#         if "index" in colnames:
#             colnames.remove("index")
#     for cname in colnames:
#         temp.append(inst_sql.get_datafromcolumn(cname))
#     df = db.sqldata2df(np.array(temp).T, colnames)
#     return df

if False:
    # WEBSCRAPING TESTS
    blob = scrape.scraping()
    tit, data = scrape.decode(blob)
    df = scrape.data2df(tit, data)

if False:
    # VAN WEBSITE, NAAR DATAFRAME, NAAR PICKLE BESTAND.
    md.make_basistraindf()


if True:
    df = db.dbdata2df("C:/temp", "healthapp", "health")
    inputparam = ["genetic", "exercise", "smoking", "alcohol", "sugar", "bmi"]
    outputparam = "lifespan"
    model = tm.Modeltrainer(inputparam, outputparam).linearregr(df)
    predictor = pm.Modelpredictor(model)

    # return model

    # model = tm.make_appmodel()
    # predictor = pm.Modelpredictor(model)

    res = predictor.predict(df[inputparam])
    diff = df["lifespan"] - res
    print(diff)


if False:
    # AANVULLEN VAN SQLDB MET KOLOM BMI,
    # EN DEZE VULLEN MET WAARDEN
    df = md.open_basistraindf()
    pp_data = md.Preprocess(df)
    df_new = pp_data.set_bmi()

    inst_sql = db.Sqlite("healthapp", "health")
    inst_sql.add_values2col("bmi", df_new["bmi"])


if False:
    # modelpredictor

    df = db.dbdata2df(databasepath, "healthapp", "health")
    inputparam = ["genetic", "exercise", "smoking", "alcohol", "sugar", "bmi"]
    outputparam = "lifespan"

    model = tm.Modeltrainer(inputparam, outputparam).linearregr(df)
    predictor = pm.Modelpredictor(model)

    # return model

    # model = tm.make_appmodel()
    # predictor = pm.Modelpredictor(model)

    res = predictor.predict(df[inputparam])
    diff = df["lifespan"] - res
    # x

if False:
    # WEBSCRAPING TESTS
    blob = scrape.scraping()
    tit, data = scrape.decode(blob)
    df = scrape.data2df(tit, data)

if False:
    # VAN WEBSITE, NAAR DATAFRAME, NAAR PICKLE BESTAND.
    md.make_basistraindf()

if False:
    # AANVULLEN VAN SQLDB MET KOLOM BMI,
    # EN DEZE VULLEN MET WAARDEN
    df = md.open_basistraindf()
    pp_data = md.Preprocess(df)
    df_new = pp_data.set_bmi()

    inst_sql = db.Sqlite("healthapp", "health")
    inst_sql.add_values2col("bmi", df_new["bmi"])

if False:
    df = md.open_basistraindf()
    print(df)

if False:
    # PREPROCESS VOOR MODEL
    # xparam = ["alcohol", "exercise", "bmi", "sugar", "smoking"]
    xparam = ["exercise", "bmi"]
    df = md.open_basistraindf()

    prepro = md.Preprocess(df)
    prepro.set_bmi()
    print(df.get(xparam).shape)
    test, train = prepro.split_data()
    dtree = tm.Modeltrainer(xparam=xparam).decisiontree(train, printmetrics=True)

    pred_train = pm.Modelpredictor(dtree).predictor(train, xparam)
    print(pred_train)

    vi.Descrstats().plot_xygraph(pred_train, "true", "pred")
    pp.gcf().savefig("C:/temp/proj3_res.png")
    # print(dir(dtree))

if False:
    # PLOTTEN PLOTS BESCHRIJVENDE STATISTIEK
    vi.Descrstats().descr_main()
