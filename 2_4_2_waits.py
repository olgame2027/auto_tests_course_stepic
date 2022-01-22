# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
# browser.get(...

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait2.html")
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
# button.click()...

# Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода until_not:
# # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )

    # until
    # title_is
    # title_contains
    # presence_of_element_located
    # visibility_of_element_located
    # visibility_of
    # presence_of_all_elements_located
    # text_to_be_present_in_element
    # text_to_be_present_in_element_value
    # frame_to_be_available_and_switch_to_it
    # invisibility_of_element_located
    # element_to_be_clickable
    # staleness_of
    # element_to_be_selected
    # element_located_to_be_selected
    # element_selection_state_to_be
    # element_located_selection_state_to_be
    # alert_is_present


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = browser.find_element(By.ID, "price")
    price = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))

    browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    
    button = browser.find_element(By.ID, "solve")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

     # Отправляем заполненную форму
    
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
