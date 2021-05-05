from itertools import combinations

class AlgoHelper:
    def sort_users_from_dict(self, users_pokemon_price_dict):
        """
        Returns list of sorted users starting with one who has the highest number of cards.
        :param users_pokemon_price_dict: Dict with user:[list with pokemon:price dicts]
        :return: list of sorted user
        """
        users = list(users_pokemon_price_dict.keys())
        sorted_list_of_users = []
        for iteration in users:
            biggest_amount_of_cards_user = users[0]
            for user in users:
                if len(users_pokemon_price_dict[user]) > len(users_pokemon_price_dict[biggest_amount_of_cards_user]):
                    biggest_amount_of_cards_user = user
            users.remove(biggest_amount_of_cards_user)
            sorted_list_of_users.append(biggest_amount_of_cards_user)

        return sorted_list_of_users

    def change_list_of_tuples_to_dict_of_dicts(self, seller_pokemon_price_dict):
        """
        Change format of seller_pokemon_price_dict from {'user':[{'Pokemon1' :'0,02e'}, .... to {'user':{'pok1':0,2
        , 'pok2}
        :param seller_pokemon_price_dict: dict, seller_pokemon_price_dict
        :return: dict, adjusted pokemon price dict
        """
        seller_pokemon_price_dict2 = {}
        for elm in seller_pokemon_price_dict:
            for elm2 in seller_pokemon_price_dict[elm]:
                if elm not in seller_pokemon_price_dict2.keys():
                    seller_pokemon_price_dict2[elm] = elm2
                else:
                    seller_pokemon_price_dict2[elm].update(elm2)
        self._adjust_prices_format(seller_pokemon_price_dict2)
        seller_pokemon_price_dict2 = self._remove_obsolete_users(seller_pokemon_price_dict2)
        return seller_pokemon_price_dict2

    def prepare_data_for_problem_solving(self, pokemon_to_user, seller_pokemon_price_dict):
        """
        The most important function. For every Pokemon create sets of all pokemon's combinations from users
        :param pokemon_to_user:
        :param seller_pokemon_price_dict:
        :return:
        """
        weight = 15
        userdict5 = {}
        weight_helper = 0
        helper_weight_helper = 0
        for pokemon in pokemon_to_user:
            print(pokemon)
            userdict5[pokemon] = {}
            for user in pokemon_to_user[pokemon]:
                print(user)
                userdict5[pokemon][user] = {}
                # for elm in combinations((userdict3)[user], 12):
                #     weight_helper = weight_helper + 1
                #     print(weight_helper)
                for L in range(1, len(seller_pokemon_price_dict[user])):
                    print("iteracja" + str(L))
                    for subset in combinations(seller_pokemon_price_dict[user], L):
                        # helper_weight_helper = helper_weight_helper + 1
                        # print("subset numer: " + str(helper_weight_helper))
                        for elm in subset:
                            weight = weight + seller_pokemon_price_dict[user][elm]

                        if str(weight) not in userdict5[pokemon][user].keys():
                            userdict5[pokemon][user].update({str(weight): list(subset)})
                        elif str(weight) in userdict5[pokemon][user].keys():
                            for K in range(0, len(userdict5[pokemon][user].keys())):
                                if str(weight) + K * "#" in userdict5[pokemon][user].keys():
                                    weight_helper = weight_helper + 1
                            # if str(weight) + weight_helper*'#' not in userdict5[pokemon][user].keys():
                            #     userdict5[pokemon][user] = {str(weight) + weight_helper*'#': list(subset)}
                            # else:
                            userdict5[pokemon][user].update({str(weight) + weight_helper * '#': list(subset)})
                            weight_helper = 0
                            # else:
                            #     for K in range(0, weight_helper):
                            #         if str(weight) + weight_helper*"#" in userdict5[pokemon][user].keys():
                            #             for elm in userdict5[pokemon][user].keys():
                            #                 if elm == str(weight) + weight_helper*"#":
                            #                     weight_helper = str(weight) + "#"
                            #     userdict5[pokemon][user] = {str(weight)+: list(subset)}
                        weight = 15
        return userdict5
    def create_list_of_pokemon_to_users(self, pokemon_to_url, seller_pokemon_price_dict):
        """
        Create list of pokemons and users who have them
        :param pokemon_to_url: dict, pokemon to url
        :param seller_pokemon_price_dict: dict
        :return: dict
        """
        pokemon_names_list = [list(pokemon)[0] for pokemon in pokemon_to_url]
        pokemon_to_users_list = {}
        for pokemon in pokemon_names_list:
            for user in seller_pokemon_price_dict:
                if pokemon in seller_pokemon_price_dict[user].keys():
                    # pokemon_to_users_list.setdefault(pokemon, []).append({user: userdict3[user][pokemon]})
                    if pokemon in pokemon_to_users_list.keys():
                        pokemon_to_users_list[pokemon].update({user: seller_pokemon_price_dict[user][pokemon]})
                    else:
                        pokemon_to_users_list[pokemon] = {user: seller_pokemon_price_dict[user][pokemon]}
        return pokemon_to_users_list

    def _adjust_prices_format(self, seller_pokemon_price_dict2):
        """
        change all prices from 0,02e to 0.02
        :param seller_pokemon_price_dict2: dict in chage_list_of_tuples_to_dict_of_dicts
        :return: dict, seller_pokemon_price_dict_2 with adjusted values
        """
        for user in seller_pokemon_price_dict2:
            for pokemon in seller_pokemon_price_dict2[user]:
                seller_pokemon_price_dict2[user][pokemon] = \
                    float(seller_pokemon_price_dict2[user][pokemon][:-2].replace(',', '.'))

    def _remove_obsolete_users(self, seller_pokemon_price_dict3):
        """
        Remove users that have pokemons covered by other users in worse prices.
        :param seller_pokemon_price_dict3: dict from _adjust_prices_format
        :return: dict without obsolete users
        """
        userdict3 = seller_pokemon_price_dict3.copy()
        cost_sum_user2 = 15
        cost_sum_user1 = 15
        for user1 in seller_pokemon_price_dict3:
            print(user1)
            for user2 in seller_pokemon_price_dict3:
                print(user2)
                if user1 != user2:
                    if len(seller_pokemon_price_dict3[user2]) < len(seller_pokemon_price_dict3[user1]):
                        if len([
                            item for item in list(seller_pokemon_price_dict3[user1].keys())
                            if item not in list(seller_pokemon_price_dict3[user2].keys())]) == \
                                (len(seller_pokemon_price_dict3[user1]) - len(seller_pokemon_price_dict3[user2])):
                            for key in list(seller_pokemon_price_dict3[user2].keys()):
                                cost_sum_user2 = cost_sum_user2 + seller_pokemon_price_dict3[user2][key]
                            for key in list(seller_pokemon_price_dict3[user1].keys()):
                                cost_sum_user1 = cost_sum_user1 + seller_pokemon_price_dict3[user1][key]
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
        return userdict3