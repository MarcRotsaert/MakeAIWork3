#  webscraping met selenium
# import matplotlib
# import tensorflow
# import selenium
import pprint
from selenium import webdriver as wd
import bs4
import pandas as pd
import requests

# inlezen van de tekst website met requests,werkt wel vaak.
req = requests.get(url="https://medisch-centrum-randstad.netlify.app/")
x2 = bs4.BeautifulSoup(req.content)

if False:
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
fun = lambda x, y: {x: y}

dump = x3.pop(0)
print(len(dump))
titles = [a.text for a in dump]

df = pd.DataFrame()
nonelist = len(x3) * [None]

dfinput = {tit: nonelist for tit in titles}
# print(dfinput[tit])
df = pd.DataFrame(dfinput)

i = 0
for line in x3:
    j = 0
    for num in line:
        df[titles[j]][i] = int(num.text)
        j += 1
    i += 1
print(df.head(10))
print(df.tail(10))


from selenium.webdriver.common.by import By

# nog wat selenium shit.
x = wd_inst.find_element(By.CLASS_NAME, "td")
# x = wd_inst.find_element(By.TAG_NAME, "<td>")
print(x)
print(len(x.value_of_css_property("h1")))
# dir(By)
# wd_inst.find_element_by_xpath
