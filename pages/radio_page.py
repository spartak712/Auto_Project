# Страница вкладки Radio Button
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base


class RadioPage(Base):


    """"Локаторы"""
    radio_yes = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label'
    title_locator = '//*[@id="app"]/div/div/div[1]/div'
    success_message = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p'


    """"Геттеры"""
    def get_radio_yes(self):
        return self.browser.find_element(By.XPATH,self.radio_yes)


    def get_title_text(self):
        x = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, self.title_locator)))
        return self.browser.find_element(By.XPATH, self.title_locator)


    def get_success_message(self):
        x = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, self.success_message)))
        return self.browser.find_element(By.XPATH, self.success_message)


    """Действия"""
    def click_on_radio_yes(self):
        self.get_radio_yes().click()
        print("Chose the radio yes")


    def parsed_radio_title(self):
        title = self.get_title_text().text
        assert title == "Radio Button"
        print("You are in " + title + " page")


    def parsed_success_message(self):
        message = self.get_success_message().text
        print(message)
        assert message == "You have selected Yes"



