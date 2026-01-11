import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/irkutsk/category/svet"
driver.get(url)
time.sleep(3)

lights = driver.find_elements(By.CLASS_NAME, "CatalogContent_item__Zinr3")

parsed_data = []

for light in lights:
    try:
        name = light.find_element(By.CSS_SELECTOR, '.ProductName').text
    except:
        name = "Нет названия"
    try:
        price =  light.find_element(By.CSS_SELECTOR, 'span[class*="Price"]').text
    except:
        price = "Нет цены"
    try:
        url = light.find_element(By.CSS_SELECTOR, 'a[href]') .get_attribute('href')
    except:
        url = "Нет ссылки"

    # фильтрация мусора
    if not name or not price or not url:
        continue

    parsed_data.append([name, price, url])

driver.quit()
with open("divan.csv", "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Название светильника", "Цена", "Ссылка"])
    writer.writerows(parsed_data)