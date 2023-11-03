# Utilizo Unittets de python, porque cypress usa java y eso me cuesta programarlo
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Defino una clase de prueba que hereda de unittest.TestCase
class TestMyApp(unittest.TestCase):
    def setUp(self):
        # Inicializo el controlador de Chrome 
        self.driver = webdriver.Chrome()

    def test_login_and_submit_survey(self):
        driver = self.driver
        # Abro la página de inicio de sesión
        driver.get("https://virtual.um.edu.ar/login/index.php")

        # Encontro elementos de la página por su ID
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginbtn")

        # Datos login
        username.send_keys("")
        password.send_keys("")
        login_button.click()

        time.sleep(1)  # Espera 1 segundo

        # Navego hasta la pagina de encuesta
        driver.get("https://virtual.um.edu.ar/mod/questionnaire/complete.php?id=210589")
        time.sleep(1)

        # Encontrar y seleccionar elementos en la página
        selector_1 = driver.find_element(By.ID, 'auto-rb0001')
        if not selector_1.is_selected():
            selector_1.click()

        selector_2 = driver.find_element(By.ID, 'dropSelecciòn')
        selector_2.click()

        # Selecciono la una opción del menú desplegable
        select = Select(selector_2)
        select.select_by_index(3)

        # Envio la encuesta
        enviar_encuesta = driver.find_element(By.CSS_SELECTOR, '#phpesp_response > div > div > input.btn.btn-primary.control-button-submit')
        enviar_encuesta.click()
        time.sleep(1)

    def tearDown(self):
        # Cierro el controlador
        self.driver.quit()

# Si todo funcion OK, es decir el archivo se ejecuta y envia. Entoces hago correr el test 
if __name__ == '__main__':
    unittest.main()

