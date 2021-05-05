from selenium import webdriver
import AlgoHelper
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
time.sleep(2)
clickHelper = ClickHelper(driver)
clickHelper.click_singles_button()
clickHelper.search_expansion('Team-Rocket')
list_of_pokemons_urls = clickHelper.get_urls_for_cards_from_given_expansion()

seller_pokemon_price_dict, pokemon_name_to_url = clickHelper.get_seller_pokemons_price_dict(list_of_pokemons_urls)
pokemon_to_users_list = AlgoHelper().create_list_of_pokemon_to_users(pokemon_name_to_url, seller_pokemon_price_dict)
print(pokemon_to_users_list)
print(seller_pokemon_price_dict)
print(pokemon_name_to_url)
print("")
#data_to_feed_algorithm = AlgoHelper().prepare_data_for_problem_solving(pokemon_to_users_list, seller_pokemon_price_dict)

# Serialize data into file:
# json.dump( seller_pokemon_price_dict, open( "urlsdict2.txt", 'w' ) )
# json.dump( pokemon_name_to_url, open("pokemon_name_to_url.txt", 'w'))

driver.close()
print("--- %s seconds ---" % (time.time() - start_time))



#display.stop()
