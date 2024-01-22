#Базовый класс для общих  методов всех страниц
import datetime
from selenium import webdriver


class Base():


    base_url = "https://demoqa.com/"
    browser = webdriver.Chrome()


    """Метод получающий урл"""
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Current URL : " + get_url)


    """Метод делающий скриншот"""
    def get_screen(self, name_of_test):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot_" + name_of_test + "_" + now_date + ".png"
        self.browser.save_screenshot('..\\screens\\' + name_screenshot)
        print("Screen done!")