#Здесь используются библиотеки pandas и selenium для сбора данных с таблицы, у которой много страниц и между ними нужно переключаться
#С помощью селеинума логинимся на сайт и забираем данные из headers и данные из тела таблицы, и с помощью pandas заносим их в csv
#Далее бесконечным циклом while переключаемся между всеми страницами и забираем данные из тела таблицы
#time.sleep чтобы успевали прогрузиться данные при переключении между страницами

import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

login_re = 'https://xn--e1afdcc4acfdaedaq9m.xn--p1acf/'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)
driver.get(login_re)

login_value = driver.find_element(By.ID, 'email')
login_value.clear()
login_value.send_keys('ПОЧТА@yandex.ru')

pass_value = driver.find_element(By.ID, 'password')
pass_value.clear()
pass_value.send_keys("ПАРОЛЬ")
pass_value.send_keys(Keys.RETURN)

time.sleep(5)

stats_body = driver.find_element(By.CLASS_NAME, 'ant-table-body')
stats_headers = driver.find_elements(By.CLASS_NAME, 'ant-table-thead')
stats_cells = stats_body.find_elements(By.CLASS_NAME, 'ant-table-cell')

test_headers = [i.text.split('\n') for i in stats_headers]

logical = [j.text for j in stats_cells]
new_cells = [i for i in logical if i]

test_cells = [new_cells[i : i + 19] for i in range(0 , len(new_cells), 19)]

df = pandas.DataFrame(data=test_cells, columns=test_headers)
df.to_csv('data.csv', index=None)

time.sleep(3)


arrow = driver.find_element(By.CLASS_NAME, 'ant-pagination-next').click()

time.sleep(2)

stats_body = driver.find_element(By.CLASS_NAME, 'ant-table-body')
stats_cells = stats_body.find_elements(By.CLASS_NAME, 'ant-table-cell')

logical = [j.text for j in stats_cells]
new_cells = [i for i in logical if i]
test_cells = [new_cells[i:i + 19] for i in range(0 , len(new_cells), 19)]

df = pandas.DataFrame(data=test_cells, columns=test_headers)
df.to_csv('data.csv', mode='a', index=None, header=False)

time.sleep(3)

while True:
    arrow = driver.find_element(By.CLASS_NAME, 'ant-pagination-next').click()

    time.sleep(2)

    stats_body = driver.find_element(By.CLASS_NAME, 'ant-table-body')
    stats_cells = stats_body.find_elements(By.CLASS_NAME, 'ant-table-cell')

    logical = [j.text for j in stats_cells]
    new_cells = [i for i in logical if i]
    test_cells = [new_cells[i:i + 19] for i in range(0, len(new_cells), 19)]

    df = pandas.DataFrame(data=test_cells, columns=test_headers)
    df.to_csv('data.csv', mode='a', index=None, header=False)
    time.sleep(3)
