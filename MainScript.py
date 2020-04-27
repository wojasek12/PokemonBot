from selenium import webdriver
from ClickHelper import ClickHelper
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.cardmarket.com/en/Pokemon")

clickHelper = ClickHelper(driver)

clickHelper.click_singles_button()
clickHelper.search_expansion('Fossil')
list_of_pokemons = clickHelper.list_of_pokemons_from_expansion()
list_of_pokemons = clickHelper.remove_spaces_and_brackets_from_names(list_of_pokemons)
seller_pokemon_price_dict = clickHelper.seller_pokemons_price_dict()

driver.close()