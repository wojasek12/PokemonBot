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

    # def list_of_cards(self):
    #     number_of_cards = driver.
    #     pokemon_list = driver.find_elements_by_xpath("//div[@class='table-body']/div/div[4]/div[1]/div[1]/a")
