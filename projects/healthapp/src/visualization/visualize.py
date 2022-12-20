import os
from matplotlib import pyplot

os.chdir()

import database as dbase


class Descrstats:
    """
    Class voor beschrijvende statistiek
    """

    def __init__(self, dbname, tablename):
        self.dbase = dbname
        self.table = tablename

    def plot_graph(self):
        pass
