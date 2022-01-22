from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    
    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

     # Отправляем заполненную форму
    
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
