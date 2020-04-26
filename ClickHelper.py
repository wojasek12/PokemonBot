import time

class ClickHelper:
    def search_expansion(self, driver, generation_name):
        time.sleep(2)
        driver.find_element_by_name('idExpansion').send_keys(generation_name)
        driver.find_element_by_xpath("//input[@value='Search']").click()
        print("zmiana")
    def list_of_cards(self, driver):
        number_of_cards = driver.
        pokemon_list = driver.find_elements_by_xpath("//div[@class='table-body']/div/div[4]/div[1]/div[1]/a")
