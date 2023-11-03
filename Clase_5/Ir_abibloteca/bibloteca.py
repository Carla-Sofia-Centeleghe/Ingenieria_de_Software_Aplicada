from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def search_for_book():
    # Defino la URL del sitio web
    url = 'https://biblioteca.um.edu.ar/?_gl=1*13zexqr*_ga*NTQwODQwMS4xNjkyMzcwOTMx*_ga_S845M31WNT*MTY5ODc1NzU0OS45NC4w.LjA.'

    # Inicializo el controlador de Chrome
    driver = webdriver.Chrome()

    # Abrio la URL en el navegador
    driver.get(url)

    # Espero 1 segundo mientras la página carga
    time.sleep(1)

    # Encontro el campo de búsqueda y escribo el texto
    search_field = driver.find_element(By.ID, "translControl1")
    search_field.send_keys("Ingeniería de Software de Pressman")

    # Envio el formulario de búsqueda
    driver.find_element(By.ID, "searchsubmit").submit()

    # Espero 3 segundo para que cargaaparezcan los resultados
    time.sleep(3)

    # Leo la pagina y veo si esta el libro que busco
    if "Ingeniería de Software de Pressman" in driver.page_source:
        print("El libro existe")
    else:
        print("El libro no existe")

    # Cierro el navegador
    driver.quit()

if __name__ == "__main__":
    search_for_book()
