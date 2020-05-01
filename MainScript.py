from selenium import webdriver
from ClickHelper import ClickHelper
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
import time
import json
#display = Display(visible=0, size=(800, 600))
#display.start()
start_time = time.time()
driver = webdriver.Chrome()
driver.get("https://www.cardmarket.com/en/Pokemon")

clickHelper = ClickHelper(driver)

clickHelper.click_singles_button()
clickHelper.search_expansion('Fossil')
list_of_pokemons = clickHelper.list_of_pokemons_from_expansion()
list_of_pokemons = clickHelper.remove_spaces_and_brackets_from_names(list_of_pokemons)
seller_pokemon_price_dict = clickHelper.seller_pokemons_price_dict(list_of_pokemons)

print("dupa")
print("dupa")

driver.close()
print("--- %s seconds ---" % (time.time() - start_time))

# Serialize data into file:
json.dump( seller_pokemon_price_dict, open( "dict.txt", 'w' ) )
#display.stop()
