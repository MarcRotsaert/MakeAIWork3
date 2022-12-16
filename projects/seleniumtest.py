#  webscraping met selenium
# import matplotlib
# import tensorflow
# import selenium
import pprint
from selenium import webdriver as wd
import bs4

# from selenium import webdriver as wd
# from selenium import webdriver as wd
from selenium.webdriver.common.by import By

wd_inst = wd.Edge()

wd_inst.get("https://medisch-centrum-randstad.netlify.app")
dump = wd_inst.page_source  #
# xx
# print(wd_inst.title)
# print(dir(wd_inst))
x2 = bs4.BeautifulSoup(dump)
x3 = x2.find_all("tr")
x4 = x3[0].find_all("td")

x = wd_inst.find_element(By.CLASS_NAME, "td")
# x = wd_inst.find_element(By.TAG_NAME, "<td>")

print(x)
print(len(x.value_of_css_property("h1")))
# dir(By)
# wd_inst.find_element_by_xpath
