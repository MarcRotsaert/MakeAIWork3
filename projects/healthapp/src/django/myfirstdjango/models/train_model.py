# from __init__ import *
from scipy import stats
import os, sys
import numpy as np
import pandas as pd
import sklearn.model_selection as modsel
from sklearn.svm import SVR
import sklearn.metrics as metrics
import sklearn.tree as tree
import sklearn.linear_model as linmod

# import data.database as db
import time

# from __init__ import *


class Modeltrainer:
    def __init__(self, xparam=["mass", "sugar", "alcohol"], yparam="lifespan"):
        self.xparam = xparam
        self.yparam = yparam

    def linearregr(self, df: pd.DataFrame):
        linregr = linmod.LinearRegression(
            fit_intercept=True,
        )
        result = linregr.fit(df[self.xparam], df[self.yparam])
        return result

    def automl_test(self):
        pass

    def decisiontree(self, df, printmetrics=False):
        dtree = tree.DecisionTreeRegressor(max_depth=12).fit(
            df.get(self.xparam),
            df["lifespan"],
        )
        if printmetrics == True:
            self.print_dtreemetrics(dtree, df)
        return dtree

    def print_dtreemetrics(self, dtree, df):
        trueval = df[self.yparam]
        predval = dtree.predict(df.get(self.xparam))
        r2 = metrics.r2_score(trueval, predval)
        print("r^2 score: " + str(r2))


def explore_relation(df: pd.DataFrame, xcol: str, ycol: str):
    return stats.linregress(
        np.array(df[xcol], dtype=np.float16), np.array(df[ycol], dtype=np.float16)
    )


# def make_appmodel():
#     df = db.dbdata2df()
#     model = Modeltrainer().linearregr(df)
#     return model


if __name__ == "__main__":

    os.chdir("projects/healthapp/src")
    sys.path.append(os.getcwd())
    from __init__ import *

    # print(datapath)
    import data.make_dataset as md
    import data.webscraping as ws
    import data.database as db
    import visualization.visualize as vs

    #
    if False:
        df = md.open_basistraindf("../data")
        pp_data = md.Preprocess(df)
        bmi_data = pp_data.set_bmi()
        df = pp_data.df
    if True:

        databasepath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\data\external"
        colnames = ["bmi", "exercise", "smoking", "alcohol", "sugar", "lifespan"]
        dfstat = db.dbdata2df(databasepath, "healthapp", "health")
        yparam = colnames.pop(-1)
        xparam = colnames
        fitresult = Modeltrainer(xparam=xparam, yparam=yparam).linearregr(dfstat)
        dfstat["pred"] = fitresult.predict(dfstat[xparam])

        vs.Descrstats().plot_xygraph(dfstat, "lifespan", "pred")
        # time.sleep(2)
        # vs.Descrstats().plot_xygraph(dfstat, "", "lifespan")

        # result = Modeltrainer().decisiontree(df, ["bmi", "alcohol", "sugar"])

        # os.chdir(r"C:\Users\marcr\MakeAIWork3\projects\\src")
        # import data.webscraping as ws

        # try:
        k = "bmi"
        # x = explore_relation(dfstat, k, "lifespan");print(x)
        # except:
        # df = ws.webscrape()
        datapath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\data\external"
        g = open(os.path.join(datapath, "linregression.txt"), "w")
        for k in dfstat.keys():
            g.write(k + "\n")
            res = explore_relation(dfstat, k, "lifespan")
            g.write(str(res) + "\n")
            g.write("___________________________\n")
        g.close()

    # model = make_appmodel()
