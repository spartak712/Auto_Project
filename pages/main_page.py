# Главная страница сайта
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base import Base


class MainPage(Base):


    """Локаторы"""
    elements_tab = '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]'


    """Геттеры"""
    def get_elements_tab(self):
        return self.browser.find_element(By.XPATH, self.elements_tab)


    """Действия"""
    def click_on_elements_tab(self):
        self.get_elements_tab().click()
        print("Click on elements tab")


