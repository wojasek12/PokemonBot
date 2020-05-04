

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

