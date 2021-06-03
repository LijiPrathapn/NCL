import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Pages.cruisePage import cruisePage
from Pages.viewpricePage import viewpricePage
from Utilities.readProperties import ReadConfig
import sys
sys.setrecursionlimit(5000)


class Test_002_Main:
    baseURL = ReadConfig.getApplicationURL()


    def test_viewprice(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        print(self.baseURL.title())
        self.cp = cruisePage(self.driver)
        self.cp.clickDestination()
        time.sleep(3)
        self.cp.clickAlaska()
        self.cp.clickDates()
        time.sleep(3)
        self.cp.clickMonth()
        time.sleep(2)
        self.cp.clickApply()
        self.cp.clickCruise()
        time.sleep(2)
        self.cp.clickPopup()
        self.vp=viewpricePage(self.driver)
        time.sleep(2)
        self.vp.clickofferPrice()
        self.vp.clickviewprice()
        self.vp.listallprices(self)
        print("ok")

