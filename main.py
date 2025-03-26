from pickle import FALSE

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import data
from selenium import webdriver
import UrbanRoutesPage as urban_routes_pom
import time  # Importar el módulo time


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

    def test_set_route(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.driver.get(data.urban_routes_url)
        time.sleep(2)
        test_driver.set_route(data.address_from, data.address_to)
        time.sleep(2)
        assert test_driver.get_from() == data.address_from
        assert test_driver.get_to() == data.address_to

    def test_select_plan(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.request_comfort_cab()
        time.sleep(2)
        assert test_driver.get_selected_tariff() == "Comfort"

    def test_fill_phone_number(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.set_phone_number(data.phone_number)
        time.sleep(3)
        assert test_driver.get_phone_in_field() == data.phone_number

    def test_fill_card(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.set_credit_card_number(data.card_number, data.card_code)
        time.sleep(3)
        assert test_driver.get_card_optn() != None

    def test_comment_for_driver(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.fill_extra_option(data.message_for_driver)
        time.sleep(2)
        assert test_driver.get_comment_for_driver_in_field() == data.message_for_driver

    def test_order_blanket_and_handkerchiefs(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.fill_extra_option(data.message_for_driver)
        time.sleep(2)
        assert test_driver.is_blanket_and_handkerchief_checkbox_selected() == False

    def test_order_2_ice_creams(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.fill_extra_option(data.message_for_driver)
        time.sleep(2)
        assert test_driver.get_current_icecream_count_value() == "2"

    def test_car_search_model_appears(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.book_trip()
        time.sleep(5)
        assert test_driver.get_order_screen_title() == "Buscar automóvil"

    def test_driver_info_appears(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.book_trip()
        test_driver.wait_confirmation()
        time.sleep(5)
        assert "El conductor llegará en" in test_driver.get_order_screen_title()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()