import sqlite3 as sql

# import webscraping as ws
import os
import numpy as np
import pandas as pd
from __init__ import *

class Sqlite:
    def __init__(self, databasepath, dbname: str, tablename: str):
        self.dbpath = databasepath
        self.dbname = dbname
        self.tablename = tablename

        self.connection = None
        if not self.exists_db():
            print(os.getcwd())

    def exists_db(self) -> bool:
        # res = os.path.exists(os.path.join(databasepath, dbname + ".db"))
        return os.path.exists(os.path.join(self.dbpath, self.dbname + ".db"))

    def close_connection(self) -> None:
        if self.connection != None:
            self.connection.close()

    def copy_sqldb(self, dbname):
        self.connection = sql.connect(os.path.join(self.dbpath, dbname + ".db"))

    def make_newsqldb(self, df: pd.DataFrame, dbname: str) -> None:
        # Make sqlite database uit dataframe.
        # Dataframe is afkomstig uit
        self.connection = sql.connect(os.path.join(self.dbpath, dbname + ".db"))
        tablename = dbname
        df.to_sql(tablename, self.connection)
        # con.close()
        self.close_connection()

    def get_colnames(self) -> list:
        self.connection = sql.connect(os.path.join(self.dbpath, self.dbname + ".db"))
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
            self.connection = sql.connect(
                os.path.join(self.dbpath, self.dbname + ".db")
            )
            ex = self.connection.execute("select * from " + self.tablename + ";")
            print("query")
            data = np.array(ex.fetchall())
            colnames = self.get_colnames()

            self.close_connection()
            return colnames, data
        else:
            print("non-query")
            self.close_connection()
            pass

    def get_datafromcolumn(self, colname) -> np.ndarray:
        if self.exists_db():
            self.connection = sql.connect(
                os.path.join(self.dbpath, self.dbname + ".db")
            )
            ex = self.connection.execute(
                "select " + colname + " from " + self.tablename + ";"
            )
            # print("query")
            return np.array(ex.fetchall()).flatten()
            self.close_connection()
        else:
            print("non-query")
            # pass

    def add_patient2sql(self, df):

        if self.exists_db():
            self.connection = sql.connect(
                os.path.join(self.dbpath, self.dbname + ".db")
            )

            colstr = ""
            for col in df.columns:
                colstr += col + ", "
            print(colstr)

            for d in df.iloc:
                dstr = ""
                for colname in df.columns:
                    dstr += str(d[colname]) + ", "
                    # print(dstr)

                execstr = (
                    "INSERT INTO "
                    + self.tablename
                    + " ( "
                    + colstr[:-2]
                    + " ) VALUES ( "
                    + dstr[:-2]
                    + " );"
                )

                print(execstr)
                ex = self.connection.execute(execstr)
            self.connection.commit()
            self.close_connection()
        else:
            print("non-existant db")

        # pass
        # con = sql.connect(os.path.join(self.dbpath, dbname + '.db"))
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
        self.connection = sql.connect(os.path.join(self.dbpath, self.dbname + ".db"))
        ex = self.connection.execute(sql_statement1)
        self.close_connection()

        return sql_statement1  # , sql_statement2

    def set_values2col(self, colname, values):
        # add values, beginning at first row going down
        self.connection = sql.connect(os.path.join(self.dbpath, self.dbname + ".db"))

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


def dbdata2df(databasepath, dbname, tablename):
    inst_sql = Sqlite(databasepath, dbname, tablename)
    dbdata = inst_sql.get_data()
    df = sqldata2df(dbdata[1], dbdata[0])
    return df


def updatesql(databasepath, dbname, tablename, dfnew):
    # Update sql database met nieuwe data uit
    inst_sql = Sqlite(databasepath, dbname, tablename)

    if "index" in dfnew:
        dfnew.drop(columns="index")
    sql_coltest = inst_sql.get_colnames()
    sql_coltest.remove("index")
    assert sql_coltest == dfnew.columns.to_list()
    lendfnew = dfnew.shape[0]
    dbdata = inst_sql.get_data()
    lendb = dbdata[1].shape[0]
    newdata = dfnew.iloc[lendb:]
    # print(newdata)
    inst_sql.add_patient2sql(newdata)
    # print("yippieyajeeee")


if __name__ == "__main__":
    databasepath = r"C:\Users\marcr\MakeAIWork3\projects\healthapp\data\external"
    inst_sql = Sqlite(databasepath, "healthapp", "health")

    if False:
        colnames = inst_sql.get_colnames()
        data1 = inst_sql.get_datafromcolumn(colnames[1])
        data2 = inst_sql.get_data()
        print(inst_sql.get_datafromcolumn("bmi"))
        print(inst_sql.get_data())
        res_length = inst_sql.get_datafromcolumn("length")
        res_weight = inst_sql.get_datafromcolumn("mass")
        df = sqldata2df(np.array([res_weight, res_length]).T, ["weight", "length"])
        print(df)

    # conn = sql.connect("C:/temp/testdb.db")
    df = dbdata2df(databasepath, "healthapp", "health")
    df = df.drop(columns="index")
    dfnew = df.iloc[-3:]
    if False:
        df.to_sql("test", conn)
    inst_sql_test = Sqlite("C:/temp", "healthapp", "health")
    inst_sql_test.add_patient2sql(dfnew)
