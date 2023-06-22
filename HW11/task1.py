# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
tensor_about_site = 'https://tensor.ru/about'

try:
    print('Открываем сайт, сравниваем ссылки')
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Неверный адрес ссылки'
    sleep(2)

    print("Ищем и открываем контакты")
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    assert contacts_btn.is_displayed()
    contacts_btn_txt = 'Контакты'
    assert contacts_btn.text == contacts_btn_txt
    contacts_btn.click()
    sleep(2)

    print("Ищем лого и открываем ссылку по нему, сравниваем ссылки")
    tensor_logo = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    assert tensor_logo.is_displayed(), 'Изображение логотипа не отобразилось'
    tensor_logo.click()
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_site, 'Неверный адрес ссылки'

    print("Ищем блок _Сила в людях_, открываем подробности")
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert news_block.is_displayed(), 'Сила не в людях'
    open_news_url = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link')
    assert open_news_url.is_displayed(), 'Ссылка не отобразилась'
    driver.execute_script("return arguments[0].scrollIntoView(true);", open_news_url)
    open_news_url.click()
    sleep(2)
    assert driver.current_url == tensor_about_site, 'Неверный адрес ссылки'


finally:
    driver.quit()

