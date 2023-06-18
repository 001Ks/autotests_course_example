# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru'
contacts = 'https://fix-online.sbis.ru/page/dialogs'
my_login = 'лояльность'
my_password = 'лояльность123'
my_text = 'Несите новый мозг, этот больше не вывозит'

try:
    print('Открываем сайт, сравниваем ссылки')
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Неверный адрес ссылки'
    sleep(2)

    print('Авторизация')
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(my_login, Keys.ENTER)
    assert login.get_attribute('value') == my_login
    sleep(2)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(my_password, Keys.ENTER)
    sleep(5)

    print("Ищем и открываем контакты")
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] .NavigationPanels-Accordion__title')
    assert contacts_btn.is_displayed(), 'Нет пункта Контакты'
    contacts_btn.click()
    sleep(5)
    contacts_btn_panel = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    assert contacts_btn_panel.is_displayed(), 'Отсутствует пункт Контакты на панели'
    contacts_btn_panel.click()
    sleep(5)
    assert driver.current_url == contacts, 'Неверный адрес ссылки'

    print('Создание сообщения: Выбор получателя')
    new_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert new_message.is_displayed(), 'Кнопка не отображается'
    sleep(2)
    new_message.click()
    sleep(2)
    recipient = driver.find_element(By.CSS_SELECTOR, '.controls-Render__field .controls-Field')
    assert recipient.is_displayed(), 'Поле выбора получателя не найдено'
    sleep(2)
    recipient.click()
    recipient.send_keys('Иванов Иван', Keys.ENTER)
    sleep(2)
    choice_people = driver.find_element(By.CSS_SELECTOR, '.controls-ListView__item-leftPadding_l')
    assert choice_people.is_displayed(), 'Пользователь не отображается в таблице'
    choice_people.click()
    sleep(2)

    print('Создание сообщения: Пишем и отправляем')
    text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    assert text.is_displayed(), 'Поле ввода сообщения не отображается'
    text.click()
    text.send_keys(my_text)
    sleep(2)
    send_text = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    assert send_text.is_displayed(), 'Не отображается кнопка отправки'
    send_text.click()
    sleep(2)

    print('Поиск сообщения в реестре')
    search = driver.find_element(By.CSS_SELECTOR, '.controls-Search__nativeField_caretEmpty_theme_default')
    assert search.is_displayed(), 'Строка поиска не найдена'
    search.click()
    search.send_keys(my_text, Keys.ENTER)
    sleep(2)
    message_in_list = driver.find_element(By.CSS_SELECTOR, '.controls-ListView__itemContent_withCheckboxes')
    assert message_in_list.is_displayed(), 'Сообщение не найдено'
    sleep(2)

    print('Удаление сообщения')
    action_chains = ActionChains(driver)
    action_chains.context_click(message_in_list)
    action_chains.perform()
    sleep(2)
    delete = driver.find_element(By.CSS_SELECTOR, '.controls-icon_style-danger')
    assert delete.is_displayed(), 'Кнопка удаления не найдена'
    delete.click()
    sleep(2)

    print('Поиск после удаления')
    find_after_delete = driver.find_element(By.CSS_SELECTOR, '.hint-Template__text_message')
    assert find_after_delete.is_displayed(), 'Поиск не пустой'

    print("The happy end")

finally:
    driver.quit()

