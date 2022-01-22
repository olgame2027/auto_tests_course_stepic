import os 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
   

   
    elements = [
       browser.find_element_by_css_selector("[name='firstname']"),
       browser.find_element_by_css_selector("[name='lastname']"),
       browser.find_element_by_css_selector("[name='email']")
    ]

    for element in elements:
        element.send_keys("a")

    with open("testfileload.txt", "w") as file:
        content = file.write("automationbypython")  # create file


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'testfileload.txt')           # добавляем к этому пути имя файла 
    
    browser.find_element(By.ID ,"file").send_keys(file_path)

     # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

