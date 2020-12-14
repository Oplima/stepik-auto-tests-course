from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    print(x)   
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)    
    print(y) 
    
    answer_fild = browser.find_element_by_id('answer')
    answer_fild.send_keys(y)
    
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    
    radiobox = browser.find_element_by_id('robotsRule')
    radiobox.click()
    
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()