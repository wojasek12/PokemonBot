import time
import re
from AlgoHelper import AlgoHelper
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException,\
    NoSuchElementException


SINGLES_BUTTON_PATH = "//a[@href='/en/Pokemon/Products/Singles']/div/button"
BASE_URL = "https://www.cardmarket.com/en/Pokemon/Products/Singles/"


class ClickHelper:
    def __init__(self, driver):
        self.driver = driver

    def click_singles_button(self):
        """
        From main cardmarket's pokemon page navigate to "Singles" section and go into that section via clicking button.
        :return: None
        """
        self.driver.find_element_by_xpath(SINGLES_BUTTON_PATH).click()

    def search_expansion(self, generation_name):
        """
        Function to search cards from specified expansion in "Singles" page/
        :param generation_name: Name of Pokemon generation to be search. Eg: "Team-Rocket".
        :return: None
        """
        # self.generation_name = generation_name
        time.sleep(2)
        self.driver.find_element_by_name('idExpansion').send_keys(generation_name)
        self.driver.find_element_by_xpath("//input[@value='Search']").click()

    def get_urls_for_cards_from_given_expansion(self):
        """
        Get full urls of all card's pages from given expansion.
        :return: list, urls of card's pages. Below example of two hits:
        example_list = ['https://www.cardmarket.com/en/Pokemon/Products/Singles/Team-Rocket/Meowth-TR62',
        'https://www.cardmarket.com/en/Pokemon/Products/Singles/Team-Rocket/Eevee-TR55']
        """
        number_of_cards = int(self.driver.find_element_by_xpath("/html/body/main/section/div[2]/div[1]").text[:-5])
        print(number_of_cards)
        final_pokemon_url_list = []
        while True:
            temp_pokemon_url_list = [pokemon.get_attribute('href') for pokemon in self.driver.find_elements_by_xpath(
                "//div[@class='table-body']/div/div[4]/div[1]/div[1]/a")]
            final_pokemon_url_list.extend(temp_pokemon_url_list)
            print(len(temp_pokemon_url_list))
            time.sleep(1)
            # if len(final_pokemon_url_list) != number_of_cards:
            #     self.driver.find_element_by_xpath("//a[@aria-label='Next page']").click()
            # else:
            #     break
            break
        return final_pokemon_url_list

    def get_seller_pokemons_price_dict(self, final_pokemon_url_list):
        """
        Get dict of dicts with sellers, and all cards they have with corresponding prices/
        :param final_pokemon_url_list: list of all card's pages urls
        :return: seller_pokemon_price_dict: dict with dicts of such scheme:
                {"itsmeagain":
                    [{"Meowth": "0,02 \u20ac"}], [{"XXX": "0,02 \u20ac"}],
                "Daniele-M": [{"Meowth": "0,02 \u20ac"}]}

                pokemon_name_to_url_list: list with dicts with Pokemon and corresponding to it url:
                eg: [{'Meowth': 'https://www.cardmarket.com/en/Pokemon/Products/Singles/Team-Rocket/Meowth-TR62'}
                    {'pikaczu': 'https://www.cardmarket.com/pokemon/pikaczu'}]
        """
        seller_pokemon_price_dict = {}
        pokemon_name_to_url_list = []
        #below 2 lines added only for demo purpose
        final_pokemon_url_list = final_pokemon_url_list[15:]
        print(final_pokemon_url_list)
        for pokemon_url in final_pokemon_url_list:
            print(seller_pokemon_price_dict)
            self.driver.get(pokemon_url)
            pokemon_name = self.driver.find_element_by_xpath("//div[@class='flex-grow-1']").text.split("\n", 1)[0]
            pokemon_name_to_url_list.append({pokemon_name: pokemon_url})
            # load_more_button = self.driver.find_element_by_xpath("//button[@id='loadMoreButton']")
            # while True:
            #     try:
            #         load_more_button.click()
            #         time.sleep(1)
            #     except(ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException):
            #         break

            table_of_offers = self.driver.find_elements_by_xpath("//div[@class='table-body']/div")

            for offer in table_of_offers:
                language = offer.find_element_by_xpath("div/div/div[2]/div/div/span").get_attribute(
                    'data-original-title')
                if language == 'English':
                    seller = offer.find_element_by_xpath(".//span[@class='seller-name d-flex']/span[3]/a").text
                    price = offer.find_element_by_xpath(
                        ".//div[@class='price-container d-none d-md-flex justify-content-end']/div/div/span").text
                    pokemon_price_dict = {pokemon_name: price}
                    seller_pokemon_price_dict.setdefault(seller, []).append(pokemon_price_dict)

        seller_pokemon_price_dict = AlgoHelper().change_list_of_tuples_to_dict_of_dicts(seller_pokemon_price_dict)
        return seller_pokemon_price_dict, pokemon_name_to_url_list

    def list_of_pokemons_from_expansion(self):
        """
        RATHER OBSOLETE, NOT USED IN FINAL SCRIPT
        Returns a list of all Pokemon card names from given expansion.
        :return: list, strings with pokemon cards names. Below example of two hits:
        example_list = ['Meowth (TR 62)', 'Eevee (TR 55)']
        """
        number_of_cards = int(self.driver.find_element_by_xpath("/html/body/main/section/div[2]/div[1]").text[:-5])
        print(number_of_cards)
        final_pokemon_list = []
        while True:
            temp_pokemon_list = [pokemon.text for pokemon in self.driver.find_elements_by_xpath(
                "//div[@class='table-body']/div/div[4]/div[1]/div[1]/a")]
            final_pokemon_list.extend(temp_pokemon_list)
            time.sleep(1)
            if len(final_pokemon_list) != number_of_cards:
                self.driver.find_element_by_xpath("//a[@aria-label='Next page']").click()
            else:
                break
        return final_pokemon_list

    def adjust_names_to_put_them_into_url(self, final_pokemon_list):
        """
        OBSOLETE!!! Convention of creating urls has been changed
        :param final_pokemon_list: Not specified
        :return: Not specified
        """
        pokemon_temp_list = []
        for pokemon in final_pokemon_list:
            if ('[' and ']' and '|') in pokemon and 'V.' not in pokemon:
                pokemon = pokemon.replace('[', '')
                pokemon = pokemon.replace(']', '')
                pokemon = pokemon.replace('|', '')
                pokemon = pokemon.replace('  ', '-')
                pokemon = pokemon.replace(' ', '-')
            if 'V.' in pokemon:
                pokemon = pokemon.replace('.', '-')
            if '[' in pokemon:
                pokemon = re.sub("\s\[.*?\]", '', pokemon)
                if re.match(".*\-$", pokemon):
                    pokemon = pokemon[:-1]
            if '!' in pokemon:
                pokemon = pokemon.replace('!', '-')
            if "'" in pokemon:
                pokemon = pokemon.replace("'", '-')
            if ' ' in pokemon:
                pokemon = pokemon.replace(' ', '-')
            if '(' in pokemon:
                pokemon = pokemon.replace(')', '')
                pokemon = pokemon.replace('(', '')
            if pokemon == 'Dark-Blastoise-V-1':
                pokemon = 'Dark-Blastoise'
            if '♀' in pokemon:
                pokemon = pokemon.replace('♀', '')
            if '.' in pokemon:
                pokemon = pokemon.replace('.','')
            if '--' in pokemon:
                pokemon = pokemon.replace('--', '-')
            if pokemon == 'Rocket-s-Sneak-Attack-Holo':
                pokemon = 'Rockets-Sneak-Attack-Holo'


            pokemon_temp_list.append(pokemon)
        print(pokemon_temp_list)
        return pokemon_temp_list
