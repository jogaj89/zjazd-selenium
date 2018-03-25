# -*- coding: utf-8 -*-
# Zaimportowanie bibliotek
from selenium import webdriver
import unittest

#tworze klase wsbPlCheck dziedzicząca po klasie TestCase z modułu unittest
class WsbPlCheck(unittest.TestCase):
    # instrukche, ktore zaostaną wykonane przed kazdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()




    def test_wsb_pl(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        self.assertIn(u"Wyższe Szkoły Bankowe", driver.title)

    def test_wsb_search_box(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        driver.find_element_by_id("edit-search-block-form--2")



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
