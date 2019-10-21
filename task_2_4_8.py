from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_css_selector("#book")
    button.click()

    x_element = browser.find_element_by_id("input_value").text
    x = calc(x_element)
    browser.find_element_by_id("answer").send_keys(x)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(20)
    browser.quit()