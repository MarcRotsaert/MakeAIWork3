import os
from matplotlib import pyplot as pp
import time
from __init__ import *

# import data.webscraping as ws

# import data.database as db


class Descrstats:
    """
    Class voor beschrijvende statistiek
    """

    # def __init__(self,):
    #    self.dbase = dbname

    def plot_graph(self, df, colname):
        pp.plot(df[colname])
        ax = pp.gca()
        return ax
        # pass

    def plot_xygraph(self, df, xcol, ycol):

        fig, ax = pp.subplots()

        pp.plot(df[xcol], df[ycol], ".", axes=ax)
        # ax = pp.gca()
        ax.set_xlabel(xcol)
        ax.set_ylabel(ycol)
        pp.gcf().show()
        # time.sleep(5)

        return ax

    def plot_distribution(self, df, colname, width=1):
        fig, ax = pp.subplots()
        # print(df[colname])
        print(df[colname].shape)
        pp.hist(df[colname], bins=width, axes=ax)
        pp.xlabel("value")
        pp.ylabel("N")
        pp.title(colname)

    def descr_main(self):
        # import data.webscraping as ws
        import data.make_dataset as md
        import visualization.visualize as vs

        # datapath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\data\external"
        df = md.open_basistraindf()
        self.plot_xygraph(df, "exercise", "lifespan")
        pp.gcf().savefig(os.path.join(datapath, "xy_ex2ls.png"))
        for k in df.keys():
            Descrstats().plot_distribution(df, k, 7)
            pp.gcf().savefig(os.path.join(datapath, "distr_" + k + ".png"))


if __name__ == "__main__":
    import sys

    sys.path.append(r"C:\Users\marcr\MakeAIWork3\projects\healthapp\src")
    os.chdir(r"C:\Users\marcr\MakeAIWork3\projects\healthapp\src")

    import data.database as db

    # from  .... import data.webscraping as scrape
    # try:
    databasepath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\data\external"
    df = db.dbdata2df(databasepath, "healthapp", "health")

    # except ConnectionError:
    # pass
    datapath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\reports\figures"
    Descrstats().plot_xygraph(df, "smoking", "lifespan")
    pp.gcf().savefig(os.path.join(datapath, "xy_ex2ls.png"))
    for k in df.keys():
        Descrstats().plot_distribution(df, k, 7)
        pp.gcf().savefig(os.path.join(datapath, "distr_" + k + ".png"))
        pp.close()
