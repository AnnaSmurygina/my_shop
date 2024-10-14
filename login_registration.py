# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
#
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_css_selector('#menu-item-50 > a')
# My_Account.click()
# email = driver.find_element_by_id('reg_email')
# email.send_keys('TRtester24@mail.ru')
# time.sleep(3)
# Password = driver.find_element_by_id('reg_password')
# Password.send_keys('458ASEwcvA')
# Register = driver.find_element_by_css_selector('.form-row:nth-child(4) .button')
# Register.click()
# driver.quit()


# Логин в систему
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_css_selector('#menu-item-50 > a')
# My_Account.click()
# Email = driver.find_element_by_id('username')
# Email.send_keys('TRtester24@mail.ru')
# Password = driver.find_element_by_id('password')
# Password.send_keys('458ASEwcvA')
# Login_but = driver.find_element_by_css_selector('.form-row:nth-child(3) .button')
# Login_but.click()
# Element = driver.find_element_by_link_text('Logout')
# Element_get_text = Element.text
# assert Element_get_text == 'Logout'
# driver.quit()

