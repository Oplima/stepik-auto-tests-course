import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(30)
    try:
        button_add_to_basket = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button_add_to_basket
    except:
        print("Button for add to basket not found, plz check it!")