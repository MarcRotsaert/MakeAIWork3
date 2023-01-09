import sqlite3 as sql

# import webscraping as ws
import os
import numpy as np
import pandas as pd

# df = ws.webscrape()

datapath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\data\external"


class Sqlite:
    def __init__(self, dbname: str, tablename: str):
        self.dbname = dbname
        self.tablename = tablename
        self.exists_db()
        self.connection = None

    def exists_db(self) -> bool:
        # res = os.path.exists(os.path.join(datapath, dbname + ".db"))
        return os.path.exists(os.path.join(datapath, self.dbname + ".db"))

    def close_connection(self) -> None:
        if self.connection != None:
            self.connection.close()

    def make_newsqldb(self, df: pd.DataFrame, dbname: str) -> None:
        # Make sqlite database uit dataframe.
        # Dataframe is afkomstig uit
        self.connection = sql.connect(os.path.join(datapath, dbname + ".db"))
        tablename = dbname
        df.to_sql(tablename, self.connection)
        # con.close()
        self.close_connection()

    def get_colnames(self) -> list:
        self.connection = sql.connect(os.path.join(datapath, self.dbname + ".db"))
        # ex = self.connection.execute("PRAGMA table_info(" + self.tablename + ");")
        # select name from pragma_table_info("health")
        ex = self.connection.execute(
            """select name from pragma_table_info(\"""" + self.tablename + """\")"""
        )
        temp = ex.fetchall()
        colnames = [t[0] for t in temp]
        self.close_connection()
        return colnames

    def get_data(self):
        if self.exists_db():
            self.connection = sql.connect(os.path.join(datapath, self.dbname + ".db"))
            ex = self.connection.execute("select * from " + self.tablename + ";")
            print("query")
            data = np.array(ex.fetchall()).flatten()
            return
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
            # print("query")
            return np.array(ex.fetchall()).flatten()
        else:
            print("non-query")
            # pass
        self.close_connection()

    def add_patient2sql(self, data):
        pass
        # con = sql.connect(os.path.join(datapath, dbname + '.db"))
        # self.close_connection()

    def add_column2sql(self, colname, coldata, datatype):
        # add column 2 table
        # datatype : str, example. DOUBLE, or TEXT  ]
        col_def = colname + " " + datatype
        sql_statement1 = (
            """ALTER TABLE """
            + self.tablename
            + """
        ADD """
            + colname
            + """ """
            + col_def
            + """;"""
        )
        self.connection = sql.connect(os.path.join(datapath, self.dbname + ".db"))
        ex = self.connection.execute(sql_statement1)
        self.close_connection()

        return sql_statement1  # , sql_statement2

    def set_values2col(self, colname, values):
        # add values, beginning at first row going down
        self.connection = sql.connect(os.path.join(datapath, self.dbname + ".db"))

        for ix, val in enumerate(values):
            valstring = str(round(val, 1))
            sql_statement2 = (
                """UPDATE """
                + self.tablename
                + """ SET """
                + colname
                + """ = """
                + valstring
                # + """3.0"""
                + """ WHERE rowid = """
                + str(ix + 1)
            )
            ex2 = self.connection.execute(sql_statement2)
        self.connection.commit()
        self.close_connection()


def sqldata2df(queriedata, colnames):
    try:
        df = pd.DataFrame(queriedata, columns=colnames)
    except ValueError:
        df = pd.DataFrame(queriedata, columns=colnames)

    # arr_l = np.array(res_length).flatten() / 100
    # arr_w = np.array(res_weight).flatten()
    return df


def dbdata2df(colnames):
    inst_sql = Sqlite("healthapp", "health")
    temp = []
    for cname in colnames:
        temp.append(inst_sql.get_datafromcolumn(cname))
    df = sqldata2df(np.array(temp).T, colnames)
    return df


if __name__ == "__main__":
    inst_sql = Sqlite("healthapp", "health")
    colnames = inst_sql.get_colnames()

    # xx
    # a = inst_sql.add_column2sql("bmi","DOUBLE")
    # a = inst_sql.set_values2col('bmi',[2,2,2]])
    print(inst_sql.get_datafromcolumn("bmi"))
    # print(b)
    # xx
    res_length = inst_sql.get_datafromcolumn("length")
    res_weight = inst_sql.get_datafromcolumn("mass")
    df = sqldata2df(np.array([res_weight, res_length]).T, ["weight", "length"])
    print(df)
    # arr_l = np.array(res_length).flatten() / 100
    # arr_w = np.array(res_weight).flatten()
    # arr_bmi = arr_w / (arr_l**2)
    # print(arr_bmi)
