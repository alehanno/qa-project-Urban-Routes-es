import Helpers
import data
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from UrbanRoutesPage import UrbanRoutesPage



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(self.driver, 3)
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_conf_taxi_request(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        ask_taxi = routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_located_to_be_selected(ask_taxi))
        routes_page.comfort_rate_button()
        assert routes_page.comfort_button_title == 'Comfort'

    def test_add_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.add_phone_number_method(phone_number)
        Helpers.retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element(UrbanRoutesPage.phone_code_field, data.phone_number))
        routes_page.confirm_phone_code()
        assert UrbanRoutesPage.phone_text == data.phone_number

    def test_add_payment_method(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_payment_method(card_number, card_code)
        assert UrbanRoutesPage.payment_choice == 'Tarjeta'

    def test_driver_comment(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        driver_comment = data.message_for_driver
        routes_page.driver_message(driver_comment)
        assert data.message_for_driver == UrbanRoutesPage.driver_message_field

    def test_manta_request(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.manta_requirements()
        assert routes_page.is_manta_selected(), 'El campo de Manta y panuelos no esta seleccionada'

    def ice_cream_request(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.ice_cream_choice()
        assert UrbanRoutesPage.ice_cream_chosen == '2'

    def test_wait_for_taxi_modal(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.end_request()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.diver_information))
        assert routes_page.is_send_request_button_is_displayed(), 'El botón pedir taxi no está habilitado'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
