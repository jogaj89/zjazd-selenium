# -*- coding: utf-8 -*-
# Zaimportowanie bibliotek
from selenium import webdriver
import time

#Stwórz nowy sterownik do chroma
driver = webdriver.Chrome()
#Maksymalizuj okno
driver.maximize_window()
driver.get("http://www.wsb.pl")

#po 5 sekundeach zniknie - zła metoda
time.sleep(5)
#zamknij sterownik
driver.quit()
