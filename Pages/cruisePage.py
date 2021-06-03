import time

from selenium.webdriver.support.select import Select


class cruisePage:
    destination_xpath = "//div[@data-code='destination' and @class='c197_group_item']"
    Alaska_xpath = "//li[@data-value='Alaska Cruises']"
    Dates_xpath = "//div[@data-code='dates' and @class ='c197_group_item']//div[@class='e1']"
    Month_xpath = "//div[@class='c197_block -dates']//li[@data-year='2021' and @data-month='9']"
    Apply_xpath="//*[@id='app']/section[1]/div/div/form/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/ul/li[2]/a"
    Find_xpath = "//a[contains(text(),'Find a Cruise')]"
    Popup_xpath="//a[@id='simplemodal-close-img']"


    def __init__(self,driver):
        self.driver = driver

    def clickDestination(self):
        self.driver.find_element_by_xpath(self.destination_xpath).click()
    def clickAlaska(self):
        self.driver.find_element_by_xpath(self.Alaska_xpath).click()
    def clickDates(self):
        self.driver.find_element_by_xpath(self.Dates_xpath).click()
    def clickMonth(self):
        self.driver.find_element_by_xpath(self.Month_xpath).click()

    def clickApply(self):
        self.driver.find_element_by_xpath(self.Apply_xpath).click()
    def clickCruise(self):
        self.driver.find_element_by_xpath(self.Find_xpath).click()
    def clickPopup(self):
        self.driver.find_element_by_xpath(self.Popup_xpath).click()
