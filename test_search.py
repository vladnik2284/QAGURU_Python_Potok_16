from selene import be, have

QUERY_PASS = 'yashaka/selene'
QUERY_FAIL = 'adfgvfhjbjnvjxdfgjbnjsxngjknsjnbvjhbsdjhszjgnjsbhfgahgvhfvaehrvfhzv'


def test_element_found(driver):
    driver.element('[role="search"] input').should(be.blank).type(QUERY_PASS).press_enter()
    driver.element('[data-cid="1"] .OrganicTitleContentSpan').should(have.text('User-oriented Web UI browser tests in Python'))

def test_element_not_found(driver):
    driver.element('[role="search"] input').should(be.blank).type(QUERY_FAIL).press_enter()
    driver.element('div.EmptySearchResults').should(be.present)


from selene import browser, be, have
browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))