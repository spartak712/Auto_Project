import time

from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from pages.radio_page import RadioPage
from base.base import Base


"""Открывает сайт, переходит в табу Элементы, далее открывает дропдаун, выбирает раздел радио баттонов
 нажимает на баттон да, проверяет появившееся сообщение и делает скрин."""
def test_choosing_yes_radio(setup):
    main = MainPage()
    main.click_on_elements_tab()
    elements = ElementsPage()
    elements.parsed_elements_title()
    elements.click_on_dropdown()
    elements.click_on_radio_tab()
    radio = RadioPage()
    radio.parsed_radio_title()
    radio.click_on_radio_yes()
    radio.parsed_success_message()
    base = Base()
    base.get_screen('test_choosing_yes_radio')

