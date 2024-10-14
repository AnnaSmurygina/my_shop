# Shop: отображение страницы товара
import time
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
# Shop = driver.find_element_by_id('menu-item-40')
# Shop.click()
# Book = driver.find_element_by_css_selector('.post-181 img')
# Book.click()
# Element = driver.find_element_by_class_name('entry-title')
# Element_get_text = Element.text
# assert Element_get_text == "HTML5 Forms"
# driver.quit()

# Shop: количество товаров в категории

from selenium import webdriver
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
# Shop = driver.find_element_by_id('menu-item-40')
# Shop.click()
# HTML = driver.find_element_by_css_selector('.cat-item-19 a')
# HTML.click()
# Products = driver.find_elements_by_css_selector('.masonry-done .wp-post-image')
# if len(Products) == 3:
#     print('На странице отображается 3 товара')
# else:
#     print('Ошибка. Количество товаров: ' + str(len('Products')))
# driver.quit()


# Shop: сортировка товаров

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
from selenium.webdriver.support.select import Select
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_css_selector('#menu-item-50 > a')
# My_Account.click()
# Email = driver.find_element_by_id('username')
# Email.send_keys('TRtester24@mail.ru')
# Password = driver.find_element_by_id('password')
# Password.send_keys('458ASEwcvA')
# Login_but = driver.find_element_by_css_selector('.form-row:nth-child(3) .button')
# Login_but.click()
# Shop = driver.find_element_by_id('menu-item-40')
# Shop.click()
# time.sleep(3)
# sorting = driver.find_element_by_name("orderby")
# sorting_value = sorting.get_attribute("value")
#
# if sorting_value == 'menu_order':
#     print("верно")
# else:
#     print("Ошибка")
#
# Price = driver.find_element_by_class_name("orderby")
# select = Select(Price)
# select.select_by_visible_text("Sort by price: high to low")
# Price = driver.find_element_by_class_name("orderby")
# Price_value = Price.get_attribute("value")
# if Price_value == 'price-desc':
#     print("верно")
# else:
#     print("Ошибка")



# Shop: отображение, скидка товара

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_css_selector('#menu-item-50 > a')
# My_Account.click()
# Email = driver.find_element_by_id('username')
# Email.send_keys('TRtester24@mail.ru')
# Password = driver.find_element_by_id('password')
# Password.send_keys('458ASEwcvA')
# Login_but = driver.find_element_by_css_selector('.form-row:nth-child(3) .button')
# Login_but.click()
# Shop = driver.find_element_by_id('menu-item-40')
# Shop.click()
# Book = driver.find_element_by_css_selector('.post-169 img')
# Book.click()
# Book_old_price = driver.find_element_by_css_selector(".price > del > span")
# Book_old_price_text = Book_old_price.text
# assert Book_old_price_text == "₹600.00"
# Book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# Book_new_price_text = Book_new_price.text
# assert Book_new_price_text == "₹450.00"
# Book_cover = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME , 'images')))
# Book_cover.click()
# Close = WebDriverWait(driver, 15).until(
# EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
# Close.click()
# driver.quit()

# Shop: проверка цены в корзине

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.get("https://practice.automationtesting.in/")
# Shop = driver.find_element_by_id('menu-item-40')
# Shop.click()
# Basket = driver.find_element_by_css_selector('.post-182 .product_type_simple')
# Basket.click()
# time.sleep(3)
# Number_books = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
# Number_books_text = Number_books.text
# assert Number_books_text == '1 Item'
# time.sleep(3)
# price = driver.find_element_by_css_selector('.wpmenucart-contents .amount')
# price_text = price.text
# assert price_text == "₹180.00"
# time.sleep(3)
# Basket_1 = driver.find_element_by_id('wpmenucartli')
# Basket_1.click()
# Subtotal = WebDriverWait(driver, 15).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal td  .woocommerce-Price-amount'),"₹180.00"))
# Total = WebDriverWait(driver, 15).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total .amount'),"₹183.60"))
# driver.quit()

# Shop: работа в корзине

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.get("https://practice.automationtesting.in/")
# Shop = driver.find_element_by_id('menu-item-40')
# Shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# picture = driver.find_element_by_css_selector('.post-182 .product_type_simple')
# picture.click()
# time.sleep(3)
# picture_2 = driver.find_element_by_css_selector('.post-180 .ajax_add_to_cart')
# picture_2.click()
# # Basket = driver.find_element_by_id('wpmenucartli')
# Basket.click()
# time.sleep(3)
# Delete = driver.find_element_by_xpath('//a[@title="Remove this item"]')
# Delete.click()
# time.sleep(3)
# Undo = driver.find_element_by_css_selector('.woocommerce-message > a')
# Undo.click()
# Quantity = driver.find_element_by_xpath('//input[@name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# Quantity.clear()
# Quantity.send_keys("3")
# Update_basket = driver.find_element_by_css_selector('.actions .button:nth-child(2)')
# Update_basket.click()
# time.sleep(3)
# value = driver.find_element_by_xpath('//input[@name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# element_value = value.get_attribute("value")
# assert element_value == "3"
# time.sleep(3)
# Apply_coupon = driver.find_element_by_css_selector('.actions .button:nth-child(3)')
# Apply_coupon.click()
# time.sleep(3)
# message = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error li"), "Please enter a coupon code."))
# driver.quit()


# Shop: покупка товара
#
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.get("https://practice.automationtesting.in/")
# Shop = driver.find_element_by_id('menu-item-40')
# Shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# picture = driver.find_element_by_css_selector('.post-182 .product_type_simple')
# picture.click()
# time.sleep(3)
# Basket = driver.find_element_by_id('wpmenucartli')
# Basket.click()
# time.sleep(3)
# checkout = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "wc-forward")))
# checkout.click()
# Name = WebDriverWait(driver, 10).until(
# EC. visibility_of_element_located((By.ID, "billing_first_name")))
# Name.send_keys("Anna")
# Last_Name = driver.find_element_by_id('billing_last_name')
# Last_Name.send_keys("Petrova")
# Email_Address = driver.find_element_by_id('billing_email')
# Email_Address.send_keys('testir78@mail.ru')
# Phone = driver.find_element_by_id('billing_phone')
# Phone.send_keys('89562158847')
# Country = driver.find_element_by_id("s2id_billing_country")
# Country.click()
# Selector = driver.find_element_by_id('s2id_autogen1_search')
# Selector.send_keys('Africa')
# time.sleep(3)
# Selector_1 = driver.find_element_by_css_selector('#select2-results-1 li:nth-child(1)')
# Selector_1.click()
#
# Address = driver.find_element_by_css_selector('#billing_address_1:nth-child(2)')
# Address.send_keys('Lermontova_15')
# time.sleep(3)
# City = driver.find_element_by_css_selector('#billing_city:nth-child(2)')
# City.send_keys('Kair')
# State = driver.find_element_by_css_selector('#billing_state:nth-child(2)')
# State.send_keys('Aljir')
# Postcode = driver.find_element_by_css_selector('#billing_postcode:nth-child(2)')
# Postcode.send_keys('589124')
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# option = driver.find_element_by_css_selector("[value='cheque']")
# option.click()
# Order = driver.find_element_by_id('place_order')
# Order.click()
# Thank = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received"))
# Method = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))
# driver.quit()
#
