from selenium import webdriver
import time
import re
import json
from AlgoHelper import AlgoHelper

dicfossil = json.load(open("fossil.txt", 'r'))
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