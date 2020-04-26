from selenium import webdriver
from ClickHelper import ClickHelper
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.cardmarket.com/en/Pokemon")

clickHelper = ClickHelper(driver)

clickHelper.click_singles_button()
clickHelper.search_expansion('Fossil')
list = clickHelper.list_of_pokemons_from_expansion()
print(list)
driver.close()