import sys, os

import data.webscraping as scrape

apppath = "projects\healthapp"
srcpath = os.path.join(apppath, "src")
datapath = os.path.join(apppath, "data")
dataprocpath = os.path.join(datapath, "processed")
databasepath = os.path.join(datapath, "external")
modelspath = os.path.join(apppath, "models")
visualizationpath = os.path.join(srcpath, "visualization")
featurespath = os.path.join(apppath, "src", "features")
sys.path.extend([datapath, modelspath, visualizationpath, featurespath])
