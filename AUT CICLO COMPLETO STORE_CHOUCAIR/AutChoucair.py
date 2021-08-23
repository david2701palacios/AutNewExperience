import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

excel_productos = r'C:\Users\David\Desktop\AUT CICLO COMPLETO STORE_CHOUCAIR\Productos.xlsx'

df = pandas.read_excel(excel_productos, engine='openpyxl', sheet_name='Productos')

url = 'http://automationpractice.com/index.php'

excel_credenciales = r'C:\Users\David\Desktop\AUT CICLO COMPLETO STORE_CHOUCAIR\Productos.xlsx'
dc = pandas.read_excel(excel_credenciales, engine='openpyxl', sheet_name='Credenciales')
user = dc['Correo'][0]
psw = dc['Credenciales'][0]

#Selectores:
B_Login = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
S_user = '//*[@id="email"]'
S_pasword ='//*[@id="passwd"]'
B_Validate = '//*[@id="SubmitLogin"]'
P_search = '//*[@id="search_query_top"]'
B_search = '//*[@id="searchbox"]/button'
P_result = '//*[@id="center_column"]/ul/li[1]'
B_add = '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[1]/span'
B_list = '//*[@id="list"]/a'
B_order='//*[@id="header"]/div[3]/div/div/div[3]/div/a'
#Abrir navegador
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
#maximiZa pantalla
driver.maximize_window()

driver.get(url)

#iniciar sesión
driver.find_element_by_xpath(B_Login).click()
driver.find_element_by_xpath(S_user).send_keys(user)
driver.find_element_by_xpath(S_pasword).send_keys(psw)
driver.find_element_by_xpath(B_Validate).click()
#recorrer excel
for i in df.index:
    producto = str(df['Producto'][i])
    #Tipear producto
    driver.find_element_by_xpath(P_search).send_keys(producto)
    #Click en el botón buscar
    driver.find_element_by_xpath(B_search).click()
    #Esperar a que carguen los productos
    wait = WebDriverWait(driver,10)
    wait.until(ec.visibility_of_element_located((By.XPATH,P_result)))
    #Cambiar vista a "lista"
    print(df.index)
    driver.find_element_by_xpath(B_list).click()
    #Agregar producto
    driver.find_element_by_xpath(B_add).click()
    #Borrar la busqueda actual
    driver.find_element_by_xpath(P_search).clear()
driver.find_element_by_xpath(B_order).click()
for i in df.index:
    cod_prod = str(df['NombreCampo'][i])
    quanty = str(df['Cantidad'][i])
    print(quanty)
    S_Quanty = '//*[@id="'+cod_prod+'"]/td[5]/input[2]'
    print(S_Quanty)
    driver.find_element_by_xpath(S_Quanty).clear()
    driver.find_element_by_xpath(S_Quanty).send_keys(quanty)
B_step1='//*[@id="center_column"]/p[2]/a[1]'
B_step2='//*[@id="center_column"]/form/p/button'
B_terms='//*[@id="cgv"]'
B_step3='//*[@id="form"]/p/button'
B_pay='//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'
B_confirm='//*[@id="cart_navigation"]/button'
B_Usorder='//*[@id="center_column"]/p/a'
B_pdf='//*[@id="order-list"]/tbody/tr[1]/td[6]/a'
driver.find_element_by_xpath(B_step1).click()
driver.find_element_by_xpath(B_step2).click()
driver.find_element_by_xpath(B_terms).click()
driver.find_element_by_xpath(B_step3).click()
driver.find_element_by_xpath(B_pay).click()
driver.find_element_by_xpath(B_confirm).click()
driver.find_element_by_xpath(B_Usorder).click()
driver.find_element_by_xpath(B_pdf).click()
#Cerrar


