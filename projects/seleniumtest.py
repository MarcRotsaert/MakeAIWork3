#  webscraping met selenium
import matplotlib
import selenium
from selenium import webdriver as wd

wd_inst = wd.Edge()
wd_inst.get("http://www.knmi.nl")
print(wd_inst.title)
