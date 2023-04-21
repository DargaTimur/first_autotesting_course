from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# расчет по формуле, для него обязательна библиотека math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Используем webdriver.Chrome для управления браузером Chrome
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html") # ссылка на тестируемый ресурс

# находим поле ввода и вводим значение
btn_book = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
# находим поле ввода инф
btn_book = browser.find_element(By.ID, 'book').click()

# скролл вниз ищем кнопку с атрибутом button
button_1 = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button_1)
button_1.click()

# находим в тексте искомое число и автоматически оно передается в формулу
x = browser.find_element(By.ID, 'input_value').text
y = calc(x)

# находим поле ввода инф
input_field = browser.find_element(By.ID, 'answer').send_keys(y)

# Отправляем заполненную форму
button = browser.find_element(By.ID, "solve").click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)

# закрываем браузер после всех манипуляций
browser.quit()
