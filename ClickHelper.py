import time
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException


SINGLES_BUTTON_PATH = "//a[@href='/en/Pokemon/Products/Singles']/div/button"
BASE_URL = "https://www.cardmarket.com/en/Pokemon/Products/Singles/"


class ClickHelper:
    def __init__(self, driver):
        self.driver = driver

    def click_singles_button(self):
        self.driver.find_element_by_xpath(SINGLES_BUTTON_PATH).click()

    def search_expansion(self, generation_name):
        self.generation_name = generation_name
        time.sleep(2)
        self.driver.find_element_by_name('idExpansion').send_keys(generation_name)
        self.driver.find_element_by_xpath("//input[@value='Search']").click()

    def list_of_pokemons_from_expansion(self):
        number_of_cards = int(self.driver.find_element_by_xpath("/html/body/main/section/div[2]/div[1]").text[:-5])
        print(number_of_cards)
        final_pokemon_list = []
        while True:
            temp_pokemon_list = [pokemon.text for pokemon in self.driver.find_elements_by_xpath(
                "//div[@class='table-body']/div/div[4]/div[1]/div[1]/a")]
            final_pokemon_list.extend(temp_pokemon_list)
            if len(final_pokemon_list) != number_of_cards:
                self.driver.find_element_by_xpath("//a[@aria-label='Next page']").click()
            else:
                break
        return final_pokemon_list

    def remove_spaces_and_brackets_from_names(self, final_pokemon_list):
        pokemon_temp_list = []
        for pokemon in final_pokemon_list:
            if ' ' in pokemon:
                pokemon = pokemon.replace(' ', '-')
                if '(' in pokemon:
                    pokemon = pokemon.replace(')', '')
                    pokemon = pokemon.replace('(', '')
            pokemon_temp_list.append(pokemon)
        return final_pokemon_list

    def seller_pokemons_price_dict(self, final_pokemon_list):
        seller_pokemon_price_dict = {}
        for pokemon in final_pokemon_list:
            print("lecimy dla" + pokemon)
            self.driver.get(BASE_URL + '/' + self.generation_name + '/' + pokemon)
            load_more_button = self.driver.find_element_by_xpath("//button[@id='loadMoreButton']")
            while True:
                try:
                    load_more_button.click()
                    time.sleep(1)
                except(ElementNotInteractableException, ElementClickInterceptedException):
                    break

            table_of_offers = self.driver.find_elements_by_xpath("//div[@class='table-body']/div")

            for offer in table_of_offers:
                language = offer.find_element_by_xpath("div/div/div[2]/div/div/span").get_attribute(
                    'data-original-title')
                if language == 'English':
                    seller = offer.find_element_by_xpath(".//span[@class='seller-name d-flex']/span[3]/a").text
                    price = offer.find_element_by_xpath(
                        ".//div[@class='price-container d-none d-md-flex justify-content-end']/div/div/span").text
                    pokemon_price_dict = {pokemon: price}
                    seller_pokemon_price_dict.setdefault(seller, []).append(pokemon_price_dict)

        return seller_pokemon_price_dict

