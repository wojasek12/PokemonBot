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
clickHelper.search_expansion('Team-Rocket')
list_of_pokemons = clickHelper.get_urls_for_cards_from_given_expansion()
print(list_of_pokemons)
# list_of_pokemons = clickHelper.adjust_names_to_put_them_into_url(list_of_pokemons)
# seller_pokemon_price_dict = clickHelper.seller_pokemons_price_dict(list_of_pokemons)
# print(seller_pokemon_price_dict)


#driver.close()
print("--- %s seconds ---" % (time.time() - start_time))

# Serialize data into file:
#json.dump( seller_pokemon_price_dict, open( "jungle.txt", 'w' ) )

#display.stop()
