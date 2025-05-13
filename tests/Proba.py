import os

from selene import browser, be, have


def test_fill_form():

    browser.open('https://client.sandbox.gboteam.ru/mainpage')
    browser.element('//*[@data-name="login"]').type('testL69')
    browser.element('//*[@data-name="password"]').type('Ab1234567!')
    # browser.element('//*[@type="submit"]').click() #Нажимаем кнопку ПРОДОЛЖИТЬ
    # browser.element('//*[@class="css-j3d076"]').click() #Раскрываем список сертов
    # browser.element('//*[@class="css-12ee5qe"]').click() #Выбираем серт
    browser.element('//*[@class="css-1ifwkrp"]').click()  #Нажимаем кнопку ПРОДОЛЖИТЬ
    browser.element('//*[@data-action="open-user-menu"]').click()

