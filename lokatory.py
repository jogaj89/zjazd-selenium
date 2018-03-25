# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.keys import Keys

class WsbPlCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://www.wsb.pl/chorzow/")
        driver.maximize_window()

    def test_find_element_by_id(self):

        driver = self.driver
        search = driver.find_element_by_id("edit-search-block-form--2")
        search.send_keys("tester")
        search.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        #button = driver.find_element_by_id("edit-submit")
        #button.click()
        results = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/ol/li')

        print ("znalazlem " + str(len(results)) + " wynikow")
        for result in results:

            print (result.text + "\n")

        sleep(5)

    #def test_link(self):
        #link = self.driver.find_element_by_link_text(u"AKCEPTUJĘ")
        #link.click()
        #sleep(3)

    #def test_link2(self):
        #link2 = self.driver.find_element_by_partial_link_text("studia pod")
        #link2.click()
        #sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
