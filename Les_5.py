from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

# расчет по формуле, для него обязательна библиотека math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Используем webdriver.Chrome для управления браузером Chrome
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html") # ссылка на тестируемый ресурс

# находим поле ввода и вводим значение
name = browser.find_element(By.CSS_SELECTOR, '.form-group .btn.btn-primary').click()

# находим всплывающее окно, переключаемся на него и нажимаем кнопку Ок
alert = browser.switch_to.alert
alert.accept()

# находим в тексте искомое число и автоматически оно передается в формулу
x = browser.find_element(By.ID, 'input_value').text
y = calc(x)

# находим поле ввода инф
input_field = browser.find_element(By.ID, 'answer')
input_field.send_keys(y)

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)

# закрываем браузер после всех манипуляций
browser.quit()
