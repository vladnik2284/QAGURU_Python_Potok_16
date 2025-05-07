import os

from selene import browser, be, have


def test_fill_form():
    file_path = os.path.abspath("../resources/image.jpg")

    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    browser.element('#firstName').should(be.blank).type('Анастасия')
    browser.element('#lastName').should(be.blank).type('З')
    browser.element('#userEmail').should(be.blank).type('test@mail.ru')
    browser.element('[value=Female]').double_click()
    browser.element('#userNumber').should(be.blank).type('7927000000')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('[value = "6"]').click()
    browser.element('.react-datepicker__year-select').element('[value = "1995"]').click()
    browser.element('.react-datepicker__month').element('.react-datepicker__day--020').click()
    browser.element('#subjectsInput').type('Arts').press_tab()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element("[placeholder='Current Address']").type("Samara")
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.element('.modal-content').element('table').all('td').even.should(
        have.exact_texts(
            'Анастасия З',
            'test@mail.ru',
            'Female',
            '7927000000',
            '20 July,1995',
            'Arts',
            'Music',
            'image.jpg',
            'Samara',
            'Haryana Karnal'))