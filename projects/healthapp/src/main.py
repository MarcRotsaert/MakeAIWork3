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

if False:
    # webscraping tests
    blob = scrape.scraping()
    tit, data = scrape.decode(blob)
    df = scrape.data2df(tit, data)

if False:
    # van website, naar dataframe, naar pickle bestand.
    md.make_basistraindf()

if False:
    df = md.open_basistraindf()
    print(df)

if False:
    # plotten plots beschrijvende statistiek
    vi.Descrstats().descr_main()

if True:
    # preprocess voor model
    # xparam = ["alcohol", "exercise", "bmi", "sugar", "smoking"]
    xparam = ["exercise", "bmi"]
    df = md.open_basistraindf()

    prepro = md.Preprocess(df)
    prepro.set_bmi()
    print(df.get(xparam).shape)
    test, train = prepro.split_data()
    # dtree = tm.Modeltrainer(xparam=xparam).decisiontree(
    #    test, printmetrics=True
    # )

    dtree = tm.Modeltrainer(xparam=xparam).decisiontree(train, printmetrics=True)

    # res = dtree.decision_path(df)
    pred_train = pm.Modelpredictor(dtree).predictor(train, xparam)
    print(pred_train)
    # vi.Descrstats().plot_xygraph(pred,)

    vi.Descrstats().plot_xygraph(pred_train, "true", "pred")
    pp.gcf().savefig("C:/temp/proj3_res.png")
    # print(dir(dtree))

if False:
    db.dbdata2dfxparam = ["alcohol", "exercise", "bmi", "sugar", "smoking"])
    df = scrape.webscrape()
