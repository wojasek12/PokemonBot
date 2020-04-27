from selenium import webdriver
import time
from selenium.common.exceptions import ElementNotInteractableException
driver = webdriver.Chrome()
pokemon_list = ['Dragonite-Holo', 'Ekans', 'Grimer']
base_url = "https://www.cardmarket.com/en/Pokemon/Products/Singles/Fossil/"
for elm in pokemon_list:
    driver.get(base_url + elm)
    load_more_button = driver.find_element_by_xpath("//button[@id='loadMoreButton']")
    while True:
        try:
            load_more_button.click()
            time.sleep(1)
        except(ElementNotInteractableException):

    table_of_offers = driver.find_elements_by_xpath("//div[@class='table-body']")
    print(table_of_offers)
driver.close()
