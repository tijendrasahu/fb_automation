from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.facebook.com/login'
driver = wb.Chrome()
driver.get(url)
mail = driver.find_element('id', 'email')
pas = driver.find_element('id', 'pass')
login = driver.find_element('id', 'loginbutton')
mail.send_keys('9754977606')
pas.send_keys(<password>)
login.click()

WebDriverWait(driver,60).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "x1lliihq x6ikm8r x10wlt62 x1n2onr6 x1j85h84"),
        "संपर्क"
    )
)

print("Complete")
