import time

SINGLES_BUTTON_PATH = "//a[@href='/en/Pokemon/Products/Singles']/div/button"

class ClickHelper:
    def __init__(self, driver):
        self.driver = driver

    def click_singles_button(self):
        self.driver.find_element_by_xpath(SINGLES_BUTTON_PATH).click()

    def search_expansion(self, generation_name):
        time.sleep(2)
        self.driver.find_element_by_name('idExpansion').send_keys(generation_name)
        self.driver.find_element_by_xpath("//input[@value='Search']").click()
        print("zmiana")

    def list_of_pokemons_from_expansion(self):
        number_of_cards = int(self.driver.find_element_by_xpath("/html/body/main/section/div[2]/div[1]").text[:-5])
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
