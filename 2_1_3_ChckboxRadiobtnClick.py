from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
   

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    browser.find_element(By.ID, "answer").send_keys(calc(x))
    
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

     # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла