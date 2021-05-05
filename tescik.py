from selenium import webdriver
import time
import re
import json
from AlgoHelper import AlgoHelper
from collections import Counter, OrderedDict, ChainMap
from itertools import combinations


#wielki slownik sprzedawcow w formie {sprzedawca1:[{pokemon1: cena}, {pokemon2:cena},.....], sprzedawca2......}
userdict = json.load(open("urlsdict2.txt", 'r'))
#zmieniam na troche bardziej sympatyczny format
userdict2 = {}
#
for elm in userdict:
    for elm2 in userdict[elm]:
        if elm not in userdict2.keys():
            userdict2[elm] = elm2
        else:
            userdict2[elm].update(elm2)

for user in userdict2:
    for pokemon in userdict2[user]:
        userdict2[user][pokemon] = float(userdict2[user][pokemon][:-2].replace(',', '.'))
pokemon_to_url = json.load(open("pokemon_name_to_url.txt", 'r'))

#FINALNA FUNKCJA ODSIEWAJACA
userdict3 = userdict2.copy()
cost_sum_user2 = 15
cost_sum_user1 = 15
for user1 in userdict2:
    print(user1)
    for user2 in userdict2:
        print(user2)
        if user1 != user2:
            if len(userdict2[user2]) < len(userdict2[user1]):
                if len([
                    item for item in list(userdict2[user1].keys())
                    if item not in list(userdict2[user2].keys())]) == (len(userdict2[user1]) - len(
                    userdict2[user2])):
                    for key in list(userdict2[user2].keys()):
                        cost_sum_user2 = cost_sum_user2 + userdict2[user2][key]
                    for key in list(userdict2[user1].keys()):
                        cost_sum_user1 = cost_sum_user1 + userdict2[user1][key]
                        print(str(cost_sum_user2) + "+++++" + str(cost_sum_user1))
                    if cost_sum_user2 > cost_sum_user1:
                        print("Deleted" + user2)
                        try:
                            del userdict3[user2]
                        except KeyError:
                            pass
                    else:
                        cost_sum_user1 = 15
                        cost_sum_user2 = 15
print("hej")
# json.dump( userdict3, open("userdict3.txt", 'w'))

#userdict3 = json.load(open("userdict3.txt", 'r'))

pokemon_names_list = [list(pokemon)[0] for pokemon in pokemon_to_url]
pokemon_to_users_list = {}
for pokemon in pokemon_names_list:
    for user in userdict3:
        if pokemon in userdict3[user].keys():
            #pokemon_to_users_list.setdefault(pokemon, []).append({user: userdict3[user][pokemon]})
            if pokemon in pokemon_to_users_list.keys():
                pokemon_to_users_list[pokemon].update({user: userdict3[user][pokemon]})
            else:
                pokemon_to_users_list[pokemon] = {user: userdict3[user][pokemon]}

# json.dump( pokemon_to_users_list, open("userdict4.txt", 'w'))
weight = 15
userdict4 = json.load(open("userdict4.txt", 'r'))
userdict5 = {}
weight_helper = 0
helper_weight_helper = 0
for pokemon in userdict4:
    print(pokemon)
    userdict5[pokemon] = {}
    for user in userdict4[pokemon]:
        print(user)
        userdict5[pokemon][user] = {}
        # for elm in combinations((userdict3)[user], 12):
        #     weight_helper = weight_helper + 1
        #     print(weight_helper)
        for L in range(1, len(userdict3[user])):
            print("iteracja" + str(L))
            for subset in combinations(userdict3[user], L):
                # helper_weight_helper = helper_weight_helper + 1
                # print("subset numer: " + str(helper_weight_helper))
                for elm in subset:
                    weight = weight + userdict3[user][elm]

                if str(weight) not in userdict5[pokemon][user].keys():
                    userdict5[pokemon][user].update({str(weight): list(subset)})
                elif str(weight) in userdict5[pokemon][user].keys():
                    for K in range(0, len(userdict5[pokemon][user].keys())):
                        if str(weight) + K*"#" in userdict5[pokemon][user].keys():
                            weight_helper = weight_helper + 1
                    # if str(weight) + weight_helper*'#' not in userdict5[pokemon][user].keys():
                    #     userdict5[pokemon][user] = {str(weight) + weight_helper*'#': list(subset)}
                    # else:
                    userdict5[pokemon][user].update({str(weight) + weight_helper*'#': list(subset)})
                    weight_helper = 0
                    # else:
                    #     for K in range(0, weight_helper):
                    #         if str(weight) + weight_helper*"#" in userdict5[pokemon][user].keys():
                    #             for elm in userdict5[pokemon][user].keys():
                    #                 if elm == str(weight) + weight_helper*"#":
                    #                     weight_helper = str(weight) + "#"
                    #     userdict5[pokemon][user] = {str(weight)+: list(subset)}
                weight = 15
            #helper_weight_helper = 0

for elm in userdict3:
    print(str (len(list(set(userdict3[elm])))) + " +++ " +str(len(list(userdict3[elm]))) )
    # if len(list(set(userdict3[elm]))) < len(list(userdict3[elm])):
    #     print(elm)

#lista wszystkich pokemonow z danego setu
pokemon_names_list = [list(pokemon)[0] for pokemon in pokemon_to_url]
pokemon_to_users_list = {}

#i tutaj sobie ten poczatkowy userdict odwracam, tak ze zamiast sprzedawca:pokemony, mam pokemona i wszystkich sprzedawcow co go maja
for pokemon in pokemon_names_list:
    for user in userdict:
        if pokemon in userdict[user][0].keys():
            pokemon_to_users_list.setdefault(pokemon, []).append(user)



pokemons_names_list = [pokemon for pokemon in pokemon_to_users_list.keys()]
pokemon_to_best_price_user = {}
best_price = 10000
for pokemon in pokemon_names_list:
    for user in pokemon_to_users_list[pokemon]:
        if float(userdict2[user][pokemon][:-2].replace(',', '.')) < best_price:
            best_price = float(userdict2[user][pokemon][:-2].replace(',', '.'))
    pokemon_to_best_price_user[pokemon] = {user: best_price}
    best_price = 10000

#sumaryczna cena wszystkich kart
price = 0
for pokemon in pokemon_to_best_price_user:
    #price = price + pokemon_to_best_price_user[pokemon].values()
    for user in pokemon_to_best_price_user[pokemon]:
        #price = price + float(user[list(pokemon_to_best_price_user[pokemon])[0]])
        price = price + pokemon_to_best_price_user[pokemon][user]



# unique_user_list = [user for user in pokemon_to_best_price_user[pokemon] for pokemon in pokemon_to_best_price_user]
unique_user_list = []
for pokemon in pokemon_to_best_price_user:
    for user in pokemon_to_best_price_user[pokemon]:
        unique_user_list.append(user)
        unique_user_list = list(set(unique_user_list))

price = price + float(len(unique_user_list))*15
print(price)
#update pokemon names list, bo spadla ilosc kart z 87 do 85, bo sa dwie karty mające oprócz normalnej wersji, wersje promo, to trza olac!

print("hej")



# for elm in pokemon_names_list:
#     if elm not in pokemons_from_pokemon_to_user_list:
#         print(elm)
# c = Counter(pokemon_names_list)
# for pokemon in pokemon_names_list:
#     print(pokemon)
#     print(c[pokemon])
#disctfossil = AlgoHelper().sort_users_from_dict(dicfossil)



#print(userdict)
# dict = {'maciek': [{"Gyarados": 2}, {"Gyarados": 4}, {"Gyarados": 5}, {"Pikachu": 2}]}
# listofuniq = []
# for elm in dict:
#     print(elm)
#     for pokemon in dict[elm]:
#         for cos in pokemon:
#             listofuniq.append(cos)
#             print(listofuniq.count(cos))
#         print(pokemon)
        #print(dict[elm][pokemon])


dicrocket = json.load(open("teamrocket.txt", 'r'))
# tablefossil = ['Dragonite (Holo)', 'Muk (Holo)', 'Ditto']
# pricefossil = 11.27
# tablerocket = ['Dark-Vileplume-Holo', 'Dark-Weezing-Holo', 'Dark-Machamp']
# pricerocket = 3.39
# for fossil in dicfossil:

# algoHelper = AlgoHelper()
#
# sorted_from_fossil = algoHelper.sort_users_from_dict(dicfossil)[:10]
# sorted_from_rocket = algoHelper.sort_users_from_dict(dicrocket)[:10]
#
# print(sorted_from_fossil)
# print(sorted_from_rocket)
# sorted = []
# for elm in sorted_from_rocket:
#     if elm in sorted_from_fossil:
#         sorted.append(elm)
#
# for elm in sorted:
#     print(elm + " " + str(len(dicfossil[elm]) + len(dicrocket[elm])))
#
# print(sorted)