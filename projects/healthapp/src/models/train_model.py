from scipy import stats
import os
import numpy as np


def explore_relation(df, xcol, ycol):
    print(
        stats.linregress(
            np.array(df[xcol], dtype=np.float16), np.array(df[ycol], dtype=np.float16)
        )
    )


def automl_test():
    pass


if __name__ == "__main__":
    os.chdir(r"C:\Users\marcr\MakeAIWork3\projects\healthapp\src")
    import data.webscraping as ws

    df = ws.webscrape()
    for k in df.keys():
        print(k)
        explore_relation(df, k, "lifespan")
        print("___________________________")
