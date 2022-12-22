# -*- coding: utf-8 -*-
import os

# import click
# import logging
# from pathlib import Path
# from dotenv import find_dotenv, load_dotenv
import sklearn.model_selection as modsel
import data.webscraping as ws
import pickle
import pandas as pd

from __init__ import *


# print(ws)
# xx


def make_basistraindf(datapath):
    # Sla de gegevens van de website op in een dataframe.
    # Deze gegevens zijn onbewerkt
    df = ws.webscrape()
    df.to_pickle(os.path.join(datapath, "raw", "df_train_basis.pickle"))


def open_basistraindf(datapath):
    with open(os.path.join(datapath, "raw", "df_train_basis.pickle"), "rb") as g:
        # df = pickle.load(os.path.join(datapath, "raw", "df_train_basis.pickle"))
        df = pickle.load(g)
    return df


class Preprocess:
    # Preprocesing van dataset voorafgaand aan training
    def __init__(self, data):
        if type(data) == pd.DataFrame:
            self.df = data
        else:
            try:
                df = pd.DataFrame(data)
            except:
                print("non-working!!!")

    def set_bmi(self):
        # voeg een extra kolom bmi toe aan het dataframe
        mass, length = [self.df["mass"], self.df["length"]]
        bmi = mass / (length / 100) ** 2

        self.df["bmi"] = bmi
        return self.df

    def split_data(self):
        train, test = modsel.train_test_split(self.df, test_size=0.1, random_state=123)
        return test, train
        # pass


# @click.command()
# @click.argument("input_filepath", type=click.Path(exists=True))
# @click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")


if __name__ == "__main__":
    """
    #log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
    """

    df = open_basistraindf()
    pp_data = Preprocess(df)
    bmi_data = pp_data.make_bmi()
    xx
