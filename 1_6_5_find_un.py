from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
   
    # elements = [
    #    browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']"),
    #    browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']"),
    #    browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
    # ]
   
    elements = [
       browser.find_element_by_css_selector(".first_block .first"),
       browser.find_element_by_css_selector(".first_block .second"),
       browser.find_element_by_css_selector(".first_block .third")
    ]

    for element in elements:
        element.send_keys("a")

     # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла