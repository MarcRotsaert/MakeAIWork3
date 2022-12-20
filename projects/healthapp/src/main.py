from __init__ import *
import data.webscraping as scrape

print(datapath)
print(srcpath)
print(modelspath)

if False:
    blob = scrape.scraping()
    tit, data = scrape.decode(blob)
    df = scrape.data2df(tit, data)
if True:
    df = scrape.webscrape()

print(df)
