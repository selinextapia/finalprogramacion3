from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pytest import mark
import time

# Abrir navegardor
driver = webdriver.Chrome()

# maximizar pantalla
driver.maximize_window()
#Pagina Para Abrir
driver.get('http://localhost:17195/Suplidor')
time.sleep(2)

driver.save_screenshot("results/introPage.png") # Capturo imagen



#Prueba HU1
@mark.ui
def test_HU1
    #loggear click
    driver.find_element(By.CSS_SELECTOR, 'home').click()
    driver.save_screenshot("resultado/loginComplete.png") # Capturo imagen
    time.sleep(3)
    assert True
    
    driver.save_screenshot("resultado/filledlogin.png") # Capturo imagen
    time.sleep(2)
    assert True
#Prueba HU2
@mark.ui
def test_HU2():
    # nav search-typeahead

  #home click
    driver.find_element(By.CSS_SELECTOR, 'href="/Home/Privacy"').click()
    driver.save_screenshot("resultado/privacy.png") # Capturo imagen
    time.sleep(3)
    assert True

    
    driver.save_screenshot("resultado/home.png") # Capturo imagen
    time.sleep(3)

    assert True

#Prueba HU3
@mark.ui
def test_HU3():

    driver.find_element(By.CSS_SELECTOR, 'Category').click() #nav  horario
    time.sleep(2)
    assert True
    driver.find_element(By.CSS_SELECTOR, 'Category').click() # inicio
    driver.save_screenshot("resultado/catgory.png") # Capturo imagen'
    time.sleep(5)
   

    assert True

#Prueba HU4
@mark.ui
def test_HU4():
    driver.find_element(By.CSS_SELECTOR, 'href="/Suplidor"').click() #nav  horario
    time.sleep(2)
    assert True
    driver.find_element(By.CSS_SELECTOR, 'suplidor').click() # inicio
    driver.save_screenshot("resultado/suplidor.png") # Capturo imagen'
    time.sleep(5)
   
    
#Prueba HU5
@mark.ui
def test_HU5():

    driver.find_element(By.CSS_SELECTOR, 'href="/Producto"').click() #nav  horario
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'producto').click() # inicio
    driver.save_screenshot("resultado/producto.png") # Capturo imagen'
    time.sleep(5)
    

    assert True


    #Prueba HU6
@mark.ui
def test_HU5():

    driver.find_element(By.CSS_SELECTOR, 'href="/Cliente"').click() #nav  horario
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'cliente').click() # inicio
    driver.save_screenshot("resultado/cliente.png") # Capturo imagen'
    time.sleep(5)



    #Prueba HU7
@mark.ui
def test_HU5():

    driver.find_element(By.CSS_SELECTOR, 'href="/Producto"').click() #nav  horario
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'producto').click() # inicio
    driver.save_screenshot("resultado/producto.png") # Capturo imagen'
    time.sleep(5)




    #Prueba HU8
@mark.ui
def test_HU5():

    driver.find_element(By.CSS_SELECTOR, 'href="/Orden"').click() #nav  horario
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'orden').click() # inicio
    driver.save_screenshot("resultado/orden.png") # Capturo imagen'
    time.sleep(5)




    #Prueba HU9
@mark.ui
def test_HU5():

    driver.find_element(By.CSS_SELECTOR, 'href="/home"').click() #nav  horario
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'home').click() # inicio
    driver.save_screenshot("resultado/home.png") # Capturo imagen'
    time.sleep(5)

    assert True


  

@mark.ui
def test_pruebafinal():
    time.sleep(4)
    driver.quit()
    assert True

    