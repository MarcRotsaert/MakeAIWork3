import pandas as pd


class Modelpredictor:
    def __init__(self, model):
        self.model = model

    def predictor(self, df, xparam=None):

        xval = df.get(xparam)
        # yval = df['lifespan']

        pred = self.model.predict(xval)
        df_out = pd.DataFrame()
        df_out["pred"] = pred
        df_out["true"] = df["lifespan"]
        return df_out

    # def modeltester():
    #    testdata = {
    #        'bmi':
    #        'exercise':range(1,4),
    #    }
