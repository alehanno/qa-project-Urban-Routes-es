import Helpers
import data
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Localizador del boton pedir un taxi
    ask_taxi_button = (By.CLASS_NAME, 'button round')

    # Localizador del boton confort
    comfort_button_title = (By.CSS_SELECTOR, '.tcard-title')

    # Localizador del campo del telefono
    number_field_module = (By.CLASS_NAME, 'np-text')

    # Localizador del campo para escribir el telefono
    add_phone = (By.ID, 'phone')

    # Localizador del boton siguiente
    phone_next_button = (By.CLASS_NAME, 'button full')

    # Localizador de texto del telefono
    phone_text = (By.CSS_SELECTOR, '.np-text')

    # Localizador del campo codigo
    phone_code_field = (By.ID, 'code')

    # Localizador para confirmar el codigo
    code_confirm_button = (By.XPATH, "//button[@class='button full']")

    # Localizador campo de pago
    payment_field = (By.CLASS_NAME, 'pp-button filled')

    # Localizador para campo de tarjeta
    add_card_button = (By.CLASS_NAME, 'pp-row disabled')

    # Localizador para agregar los datos de la tarjeta
    card_number = (By.ID, 'number')

    # Localizador para codigo de tarjeta
    code_card = (By.ID, 'code')

    # Localizador para presionar en la ventana de agregar tarjeta
    enable_add_button = (By.CLASS_NAME, 'pp-separator')

    # Localizador para el boton de tarjeta agregada
    added_card_button = (By.CLASS_NAME, 'button full')

    # Localizador para cerrar ventana
    close_window_button = (By.CLASS_NAME, 'close-button section-close')

    # Localizador de seleccion del pago
    payment_choice = (By.CSS_SELECTOR, '.pp-value-text')

    # Localizador para el mensaje al conductor
    driver_message_field = (By.ID, 'comment')

    # Localizador para verificar Mantas y panuelos
    Mantas_slider = (By.XPATH, "//span[@class='slider round']")

    # Localizador para el contador de helado
    ice_cream_counter = (By.CLASS_NAME, 'counter-plus')

    # Localizadorpara la cantidad de helados
    ice_cream_chosen = (By.CSS_SELECTOR, '.counter-value')

    # Localizador para enviar la solicitud de taxi
    send_taxi_request = (By.CLASS_NAME, 'smart-button-main')

    # Localizador con informacion del conductor
    diver_information = (By.CLASS_NAME, 'order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, from_address, to_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def ask_taxi_option(self):
        return self.driver.find_element(*self.ask_taxi_button).click()

    def comfort_rate_button(self):
        return self.driver.find_element(*self.comfort_button_title).click()

    def add_phone_number_method(self, phone_number):
        self.driver.find_element(*self.number_field_module).click()
        self.driver.find_element(*self.add_phone).send_keys(data.phone_number)
        self.driver.find_element(*self.phone_next_button).click()
        self.driver.find_element(*self.phone_code_field).send_keys(Helpers.retrieve_phone_code)

    def confirm_phone_code(self):
        self.driver.find_element(*self.code_confirm_button).click()

    def add_payment_method(self, card_number, card_code):
        self.driver.find_element(*self.payment_field).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number).send_keys(data.card_number)
        self.driver.find_element(*self.code_card).send_keys(data.card_code)
        self.driver.find_element(*self.enable_add_button).click()
        self.driver.find_element(*self.added_card_button).click()

    def driver_message(self, driver_comment):
        self.driver.find_element(*self.driver_message_field).send_keys(data.message_for_driver)

    def manta_requirements(self):
        self.driver.find_element(*self.Mantas_slider).click()

    def ice_cream_choice(self):
        self.driver.find_element(*self.ice_cream_counter).click()
        self.driver.find_element(*self.ice_cream_counter).click()

    def is_manta_selected(self):
        return self.driver.find_element(*self.Mantas_slider).is_selected()

    def end_request(self):
        self.driver.find_element(*self.send_taxi_request).click()

    def is_send_request_button_is_displayed(self):
        return self.driver.find_element(*self.send_taxi_request).is_displayed()