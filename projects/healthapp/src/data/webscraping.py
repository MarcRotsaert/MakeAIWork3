#  webscraping met selenium
# import matplotlib
# import tensorflow
# import selenium
from __init__ import *

# xx
import pprint
from selenium import webdriver as wd
import bs4
import pandas as pd
import requests


def scraping():
    # inlezen van de tekst website met requests,werkt wel vaak.
    req = requests.get(url="https://medisch-centrum-randstad.netlify.app/")
    x2 = bs4.BeautifulSoup(req.content)
    return x2


def decode(blob):
    x3 = blob.find_all("tr")
    # fun = lambda x, y: {x: y}
    dump = x3.pop(0)
    print(len(dump))
    titles = [a.text for a in dump]
    i = 0

    data = []
    for line in x3:
        temp = []
        j = 0
        for num in line:
            temp.append(int(num.text))
            # df[titles[j]][i] =
        data.append(temp)
        # j += 1
        # i += 1
    return titles, data


def data2df(titles, data):
    df = pd.DataFrame()
    nonelist = len(data) * [None]
    dfinput = {tit: nonelist for tit in titles}
    df = pd.DataFrame(dfinput)

    # df[titles[j]][i] =
    # print(dfinput[tit])
    df = pd.DataFrame(dfinput)
    i = 0
    for line in data:
        j = 0
        for num in line:
            df[titles[j]][i] = num
            j += 1
        i += 1
    print(df.head(10))
    print(df.tail(10))
    return df


def seleniumtest():
    # inlezen van de tekst website met selenium.
    wd_inst = wd.Edge()  # Dit kan ook met andere webbrowsers, chrome of firefox.
    wd_inst.get("https://medisch-centrum-randstad.netlify.app")
    dump = wd_inst.page_source  #
    wd_inst.close()
    # xx
    # print(wd_inst.title)
    # print(dir(wd_inst))

    # decoderen van de website met beautifulsoup.
    x2 = bs4.BeautifulSoup(dump)
    x3 = x2.find_all("tr")

    # voorbeeld anonymous functie.

    from selenium.webdriver.common.by import By

    # nog wat selenium shit.
    x = wd_inst.find_element(By.CLASS_NAME, "td")
    # x = wd_inst.find_element(By.TAG_NAME, "<td>")
    print(x)
    print(len(x.value_of_css_property("h1")))
    # dir(By)
    # wd_inst.find_element_by_xpath


def webscrape():
    blob = scraping()
    tit, data = decode(blob)
    df = data2df(tit, data)
    # print(df)
    return df


def main():
    scrape_res = scraping()
    titles, data = decode(scrape_res)
    df = data2df(titles, data)
    return df


if __name__ == "__main__":
    df = main()
