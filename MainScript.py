from selenium import webdriver
from ClickHelper import ClickHelper
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.cardmarket.com/en/Pokemon")

clickHelper = ClickHelper(driver)

clickHelper.click_singles_button()
clickHelper.search_expansion('Fossil')
# pokemon_list = driver.find_elements_by_xpath("//div[@class='table-body']/div/div[4]/div[1]/div[1]/a")
# for pokemon_name in pokemon_list:
#     print(pokemon_name.text)

# driver.find_element_by_xpath("/html/body/main/section/div[1]/form/div[6]/input").click()
# driver.close()
