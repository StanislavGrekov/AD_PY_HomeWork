from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent


def selenium_func(class_,xpat_):
    #Необходимо ввести свои учетные данные:
    login = '  '
    password = '  '

    useragent = UserAgent()
    option = webdriver.ChromeOptions()
    option.add_argument(f'user-agent={useragent.random}')
    s=Service('C:\\script\\testirovanie\\selenium\\chromedriver.exe')
    url = 'https://passport.yandex.ru/auth/add'
    driver = webdriver.Chrome(service=s, options=option)

    try:
        driver.get(url=url)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'Textinput-Control').send_keys(login)
        driver.find_element(By.ID, 'passp:sign-in').click()
        time.sleep(5)
        driver.find_element(By.ID, 'passp-field-passwd').send_keys(password)
        driver.find_element(By.ID, 'passp:sign-in').click()
        time.sleep(5)
        # Поиск по странице после входа
        title1 = driver.find_element(By.CLASS_NAME, class_)
        title2 = driver.find_element(By.XPATH, xpat_)
        time.sleep(2)
        return title1.text,title2.text

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

# Иногда при входе возникает ошибка 404 - не найдена страница, с чем это связанно так и не разобрался пока.
# МБ это связанно с тем, что нужно выйти перед повторным входом.