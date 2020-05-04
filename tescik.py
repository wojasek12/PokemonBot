from selenium import webdriver
import time
import re
import json
from AlgoHelper import AlgoHelper
from selenium.common.exceptions import ElementNotInteractableException
# driver = webdriver.Chrome()
# pokemon_list = ['Dragonite-Holo', 'Ekans', 'Grimer']
# #pokemon_list = ['Dragonite-Holo']
# base_url = "https://www.cardmarket.com/en/Pokemon/Products/Singles/Fossil/"
#dict = json.load(open("fossil.txt", 'r'))
#algoHelper = AlgoHelper()
pokemons = ['Abra [Vanish | Psyshock]']
for pokemon in pokemons:
    if '[' and ']' and '|' and 'V.' not in pokemon:
        pokemon = pokemon.replace('[', '')
        pokemon = pokemon.replace(']', '')
        pokemon = pokemon.replace('|', '')
        pokemon = pokemon.replace('  ', '-')
        pokemon = pokemon.replace(' ', '-')
    print(pokemon)
#result = re.match(".*\-", string)
#result = re.findall(re.compile(".*?\[(.*?)\]"), string)

#print(algoHelper.sort_users_from_dict(dict))

#print(list(dict.keys()))
#def find_three_users_with_biggest_amount_of_cards():
#keys_list = list(dict.keys())

#biggest_amount_of_card_user = keys_list[0]
#print("Na poczatku najwiecej ma " + biggest_amount_of_card_user)

#top_users_list = ['Cardlord-234', 'Alexlfernando', 'niorantes', 'CardsMania', 'Games-Island']

# for user in top_users_list:
#     print(user + ' ' + str(len(dict[user])))



# for username in keys_list:
#     if len(dict[username]) > len(dict[biggest_amount_of_card_user]):
#         biggest_amount_of_card_user = username
#         print("Teraz najwiecej ma: " + username)
#     elif len(dict[username]) == len(dict[biggest_amount_of_card_user]):
#         print("No tyle samo ma waraiat: " + username)







#print(next(iter(dict)))
#first_most_card_hold_user
# for elm in dict:
#     print(len(dict[elm]))

#print(dict)
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
