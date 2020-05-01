from selenium import webdriver
import time
import json

from selenium.common.exceptions import ElementNotInteractableException
# driver = webdriver.Chrome()
# pokemon_list = ['Dragonite-Holo', 'Ekans', 'Grimer']
# #pokemon_list = ['Dragonite-Holo']
# base_url = "https://www.cardmarket.com/en/Pokemon/Products/Singles/Fossil/"
dict = json.load(open( "dict.txt", 'r' ) )
# dict_dodatek = {'ditto': '2'}
# super_dict = {'maciek': [{'dragonite': '2,72'}], 'karol': {'ditto': '2'}, 'Natalka': {'Czarizard': '100'}}
# imie1 = 'maciek'
# imie2 = 'karol'
# imie3 = 'Bogus'
# imie4 = 'Natalka'
# imie5 = 'Natalka1'
# pokemon1 = 'dragonite'
# pokemon2 = 'ditto'
# pokemon3 = 'Czarizard'
# price1 = '2,72'
# price2 = '2'
# price3 = '100'
#super_dict.setdefault(imie1, []).append(dict_dodatek)
# print(super_dict)
# print(super_dict.setdefault(imie5, []).append(dict_dodatek))
# print(super_dict)
print(dict)
print("dupa")
#super_dict[imie4].append(dict_dodatek)

# super_dict.update({'maciek': dict_dodatek})
# print(super_dict)
# seller_pokemon_price_dict = {}
# for pokemon in pokemon_list:
#     driver.get(base_url + pokemon)
#     load_more_button = driver.find_element_by_xpath("//button[@id='loadMoreButton']")
#     while True:
#         try:
#             load_more_button.click()
#             time.sleep(1)
#         except(ElementNotInteractableException):
#             break
#     table_of_offers = driver.find_elements_by_xpath("//div[@class='table-body']/div")
#     for offer in table_of_offers:
#         language = offer.find_element_by_xpath("div/div/div[2]/div/div/span").get_attribute('data-original-title')
#         if language == 'English':
#             seller = offer.find_element_by_xpath(".//span[@class='seller-name d-flex']/span[3]/a").text
#             price = offer.find_element_by_xpath(".//div[@class='price-container d-none d-md-flex justify-content-end']/div/div/span").text
#             pokemon_price_dict = {pokemon: price}
#             seller_pokemon_price_dict[seller] = pokemon_price_dict
#             # print(seller)
#             # print(price)
#             #print(price)
# #/html/body/main/div[3]/section[5]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div/div/span
# print("Natalka")
# print (seller_pokemon_price_dict)
#driver.close()
