import os
import pandas as pd

# print(os.path.realpath(os.getcwd()))
# print(os.getcwd())
# from ..__init__ import *

# print(os.getcwd())
# try:
# os.chdir("projects/healthapp/src")


# except:
#    import train_model as tm

#    from ..data import database as db


class Modelpredictor:
    def __init__(self, model):
        self.model = model

    def return_featuresin(self):
        return self.model.feature_names_in_

    def predict(self, valin):
        # assert len(valin[0]) == len(self.return_featuresin())

        # try:
        prediction = self.model.predict(valin)
        # except ValueError:
        # prediction = self.model.predict([valin])
        return prediction


if __name__ == "__main__":
    import sys

    sys.path.append(r"C:\Users\marcr\MakeAIWork3\projects\healthapp\src")
    import data.database as db
    import train_model as tm

    databasepath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\data\external"

    # inst_sql = db.Sqlite(databasepath, "healthapp", "health")
    # dbdata = inst_sql.get_data()
    # df = db.sqldata2df(dbdata[1], dbdata[0])
    df = db.dbdata2df(databasepath, "healthapp", "health")
    inputparam = ["genetic", "exercise", "smoking", "alcohol", "sugar", "bmi"]
    outputparam = "lifespan"
    trainer = tm.Modeltrainer(inputparam, outputparam)
    appmodel = trainer.linearregr(df)
    predictor = Modelpredictor(appmodel)
    args = [6 * [0]]
    print(predictor.return_featuresin())
    print(predictor.predict(args))
