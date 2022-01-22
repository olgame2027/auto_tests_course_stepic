





from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
   
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


# from selenium import webdriver
# import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form")
   
#     elements = browser.find_elements_by_tag_name("input")
#     for element in elements:
#         element.send_keys("Мой ответ")

#     button = browser.find_element_by_xpath("//button[@type='submit']") #browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла





# from selenium import webdriver
# import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name("input")
#     # elements = browser.find_elements_by_xpath("//input[@type='text']")
#     for element in elements:
#         element.send_keys("Мой ответ")

#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла



# --------------- с поиском в google и заполнением корзины в ozon - проверка количества
# -не работает
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from time import sleep

# browser = webdriver.Chrome()
# url = 'https://google.com'
# try:
#     # open google.com
#     browser.get(url)
#     search = browser.find_element_by_tag_name('input')

#     # search request for OZON.ru
#     search.send_keys('ozon.ru')
#     search.send_keys(Keys.RETURN)

#     # locate by partial link and open ozon.ru
#     browser.find_element_by_partial_link_text('OZON — интернет-магазин').click()
#     # sleep(5)
#     wait = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR, "div[type='addToCartButton']"))

#     prod_1 = browser.find_element_by_css_selector(
#         "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(3) div[type='addToCartButton']").click()

#     prod_2 = browser.find_element_by_css_selector(
#         "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(4) div[type='addToCartButton']").click()

#     prod_3 = browser.find_element_by_css_selector(
#         "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(5) div[type='addToCartButton']").click()

#     cart = browser.find_element_by_css_selector("a[href='/cart/']").click()
#     wait1 = WebDriverWait(browser, 20).until(EC.element_to_be_selected(By.CSS_SELECTOR, '.container:nth-child(3) .a7m4'))
#     goods = browser.find_elements_by_css_selector('.container:nth-child(3) .a7m4')

#     print(goods)
#     print(len(goods))

#     assert len(goods) == 3, 'в корзине не 3 вещи'
# finally:
#     sleep(2)
#     browser.close()
#     browser.quit()


# # --------------1.6(2) - поиск ссылки
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time 
# import math

# link = "http://suninjuly.github.io/find_link_text"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     link1 = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     link1.click()

#     input1 = input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # # не забываем оставить пустую строку в конце файла




# --------------1.6(1) - поиск и заполнение в форме
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time 

# link = "http://suninjuly.github.io/simple_form_find_task.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла




# with webdriver.Chrome() as browser:
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit")
#     button.click()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# ---------------------------------------
    # By.ID – поиск по уникальному атрибуту id элемента;
    # By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
    # By.XPATH – поиск элементов с помощью языка запросов XPath;
    # By.NAME – поиск по атрибуту name элемента;
    # By.TAG_NAME – поиск по названию тега;
    # By.CLASS_NAME – поиск по атрибуту class элемента;
    # By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
    # By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.

# from selenium import webdriver

# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit_button")
# # закрываем браузер после всех манипуляций
# browser.quit()



# ---------------------------------------
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element_by_id("submit_button")
# # закрываем браузер после всех манипуляций
# browser.quit()