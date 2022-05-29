from selenium.webdriver.common.by import By

def test_check_basket_button(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    assert browser.find_element(By.CSS_SELECTOR, value='.btn-add-to-basket'), "Кнопки добавления в корзину не найдено"
