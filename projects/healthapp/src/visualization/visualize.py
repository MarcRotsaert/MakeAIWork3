import os
from matplotlib import pyplot as pp
import time

# import database as dbase


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

    def plot_distribution(self, df, colname, width):
        fig, ax = pp.subplots()
        # print(df[colname])
        print(df[colname].shape)
        pp.hist(df[colname], bins=width, axes=ax)
        pp.title(colname)


if __name__ == "__main__":
    os.chdir(r"C:\Users\marcr\MakeAIWork3\projects\healthapp\src")
    import data.webscraping as ws
    import visualization.visualize as vs

    # from  .... import data.webscraping as scrape
    df = ws.webscrape()
    Descrstats().plot_xygraph(df, "exercise", "lifespan")
