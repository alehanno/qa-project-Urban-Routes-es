from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import UrbanRoutesPage as urban_routes_pom

class TestUrbanRoutes:
    driver = None

    # se cambio el uso de time.sleep for webdriverwait, para mejorar el rendimiento, por recomendacion del revisor
    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.driver.get(data.urban_routes_url)

        # Espera a que los campos de dirección estén presentes
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "from"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "to"))
        )

        test_driver.set_route(data.address_from, data.address_to)

        # Espera a que los valores de los campos de dirección se actualicen
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value((By.ID, "from"), data.address_from)
        )
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value((By.ID, "to"), data.address_to)
        )

        assert test_driver.get_from() == data.address_from
        assert test_driver.get_to() == data.address_to

    def test_select_plan(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.request_comfort_cab()

        # Espera a que el plan Comfort esté seleccionado
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//*[contains(text(),'Comfort')]"), "Comfort"
            )
        )

        assert test_driver.get_selected_tariff() == "Comfort"

    def test_fill_phone_number(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.set_phone_number(data.phone_number)

        # Espera a que el número de teléfono esté en el campo
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value(
                (By.ID, "phone"), data.phone_number
            )
        )

        assert test_driver.get_phone_in_field() == data.phone_number

    def test_fill_card(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.set_credit_card_number(data.card_number, data.card_code)

        # Espera a que la opción de tarjeta esté presente
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='pp-button filled']//img[@alt='card']"))
        )

        assert test_driver.get_card_optn() is not None

    def test_comment_for_driver(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.fill_extra_options(data.message_for_driver)

        # Espera a que el comentario esté en el campo
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value(
                (By.ID, "comment"), data.message_for_driver
            )
        )

        assert test_driver.get_comment_for_driver_in_field() == data.message_for_driver

    def test_order_blanket_and_handkerchiefs(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.fill_extra_options(data.message_for_driver)

        # No se necesita esperar algo específico aquí, ya que solo se verifica el estado inicial.
        assert test_driver.is_blanket_and_handkerchief_checkbox_selected() is False

    def test_order_2_ice_creams(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.fill_extra_options(data.message_for_driver)

        # Espera a que el valor del contador de helados sea "2"
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[contains(text(),'Helado')]/..//div[@class='counter-value']"), "2"
            )
        )

        assert test_driver.get_current_icecream_count_value() == "2"

    def test_car_search_model_appears(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.book_trip()

        # Espera a que aparezca el título de la pantalla de búsqueda de automóvil
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@class='order shown']//div[@class='order-body']//div[@class='order-header']//div[@class='order-header-title']"), "Buscar automóvil"
            )
        )

        assert test_driver.get_order_screen_title() == "Buscar automóvil"

    def test_driver_info_appears(self):
        test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
        test_driver.book_trip()
        test_driver.wait_confirmation()
        # Espera a que el título de la pantalla de orden contenga "El conductor llegará en"
        WebDriverWait(self.driver, 20).until(
            lambda driver: "El conductor llegará en" in test_driver.get_order_screen_title()
        )
        assert "El conductor llegará en" in test_driver.get_order_screen_title()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()