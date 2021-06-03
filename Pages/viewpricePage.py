import sys
import time
sys.setrecursionlimit(5000)
a=[]
class viewpricePage:
    offerprice_xpath = "//span[contains(@class,'headline-3 -variant-1')]"
    viewprice_link_text = "VIEW DATES & PRICES"
    allprices_xpath="//div[@class='c161_price_item']"



    def __init__(self,driver):
        self.driver = driver

    def clickviewprice(self):
        self.driver.find_element_by_link_text(self.viewprice_link_text).click()
    def clickofferPrice(self):
        pricevalue=self.driver.find_element_by_xpath(self.offerprice_xpath)
        a=print(pricevalue.text)

    def listallprices(self, allprices_xpath):
        time.sleep(3)
        prices=self.driver.find_elements_by_xpath(self.allprices_xpath)
        for rate in prices:
            c=[]
            b=rate.text
            c.append(b)
            print(c)







