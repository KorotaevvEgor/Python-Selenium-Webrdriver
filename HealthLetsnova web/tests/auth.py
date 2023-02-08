from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://health.letsnova.com/")

username = driver.find_element_by_id("input-24")
driver.find_element(By.ID, 'input-24').send_keys("testnovahealth@letsnova.ru")

password = driver.find_element_by_id("input-28")
driver.find_element(By.ID, 'input-28').send_keys("6K13R2Gmqm")

driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div/div/form/div[4]/button').click()

time.sleep(5)
page_source = driver.page_source

if "В настоящий момент у Вас нет данных для просмотра" not in page_source or "Чтобы сделать первый замер " \
                                                                             "воспользуйтесь мобильным приложением " \
                                                                             "Nova Health" not in page_source:
    print("Alert: Все гуд, измерения есть")
else:
    print("Alert: Проблемы на местах")
