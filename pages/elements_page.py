# Страница Вкладки Elements
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base


class ElementsPage(Base):


    """Локаторы"""
    radio_tab = '//*[@id="item-2"]'
    title_locator = '//*[@id="app"]/div/div/div[1]/div'
    dropdown = '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[1]/span/div'


    """Геттеры"""
    def get_radio_tab(self):
        return self.browser.find_element(By.XPATH, self.radio_tab)


    def get_title_text(self):
        x = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, self.title_locator)))
        return self.browser.find_element(By.XPATH, self.title_locator)


    def get_dropdown(self):
        return self.browser.find_element(By.XPATH, self.dropdown)


    """Действия"""
    def click_on_radio_tab(self):
        self.get_radio_tab().click()
        print("Clicked radio tab")


    def parsed_elements_title(self):
        title =  self.get_title_text().text
        assert title == "Elements"
        print("You are in " + title + " page")


    def click_on_dropdown(self):
        self.get_dropdown().click()
        print("The dropdown is open")

