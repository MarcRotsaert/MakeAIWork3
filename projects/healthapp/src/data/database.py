import sqlite3 as sql

# import webscraping as ws
import os
import numpy as np

# df = ws.webscrape()

datapath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\data\external"


class Sqlite:
    def __init__(self, dbname, tablename):
        self.dbname = dbname
        self.tablename = tablename
        self.exists_db()
        self.connection = None

    def exists_db(self):
        # res = os.path.exists(os.path.join(datapath, dbname + ".db"))
        return os.path.exists(os.path.join(datapath, self.dbname + ".db"))

    def close_connection(self):
        if self.connection != None:
            self.connection.close()

    def make_newsqldb(self, df, dbname):
        # Make sqlite database uit dataframe.
        # Dataframe is afkomstig uit
        self.connection = sql.connect(os.path.join(datapath, dbname + ".db"))
        tablename = dbname
        df.to_sql(tablename, self.connection)
        # con.close()
        self.close_connection()

    def get_data(self):
        if self.exists_db():
            self.connection = sql.connect(os.path.join(datapath, self.dbname + ".db"))
            ex = self.connection.execute("select * from " + self.tablename + ";")
            print("query")
            return ex.fetchall()
        else:
            print("non-query")
            pass
        self.close_connection()

    def get_datafromcolumn(self, colname):
        if self.exists_db():
            self.connection = sql.connect(os.path.join(datapath, self.dbname + ".db"))
            ex = self.connection.execute(
                "select " + colname + " from " + self.tablename + ";"
            )
            print("query")
            return ex.fetchall()
        else:
            print("non-query")
            pass
        self.close_connection()

    def add_patient2sql(self, data):
        pass
        # con = sql.connect(os.path.join(datapath, dbname + '.db"))
        # self.close_connection()

def sqldata2df(sqldata,colnames):



if __name__ == "__main__":
    inst_sql = Sqlite("healthapp", "health")
    res_length = inst_sql.get_datafromcolumn("length")
    res_weight = inst_sql.get_datafromcolumn("mass")
    arr_l = np.array(res_length).flatten() / 100
    arr_w = np.array(res_weight).flatten()
    arr_bmi = arr_w / (arr_l**2)
    print(arr_bmi)
