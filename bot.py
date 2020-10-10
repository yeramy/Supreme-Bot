from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from config import keys
from config import product
import time


def order():
    # wait for checkout button element to load
    time.sleep(.3)
    # fill out checkout screen fields
    driver.find_element_by_id('order_billing_name').send_keys(keys['name'])
    driver.find_element_by_id('order_email').send_keys(keys['email'])
    driver.find_element_by_id('order_tel').send_keys(keys['phone_number'])
    driver.find_element_by_id('bo').send_keys(keys['address'])
    driver.find_element_by_id('oba3').send_keys(keys['apt'])
    driver.find_element_by_id('order_billing_zip').send_keys(keys['zip'])
    driver.find_element_by_id('order_billing_city').send_keys(keys['city'])
    driver.find_element_by_id('orcer').send_keys(keys['cvv'])
    driver.find_element_by_id('rnsnckrn').send_keys(keys['cc'])
    driver.find_element_by_name('credit_card[month]').send_keys(keys['em'])
    driver.find_element_by_name('credit_card[year]').send_keys(keys['ey'])

    # Process payment click
    time.sleep(.5)
    driver.find_element_by_xpath("icheckbox_minimal").click()
    driver.find_element_by_name('commit').click()


if __name__ == '__main__':
    # load chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Goto Surpeme url
    driver.get('https://www.supremenewyork.com/shop/all')

    # Find items

    # Category selector
    category = driver.find_element_by_link_text(product['category'])
    category.click()
    time.sleep(1)

    # Item selector
    item = driver.find_element_by_partial_link_text(product['keyword'])
    item.click()
    time.sleep(1)

    # Color selector
    w = "//button[@data-style-name='" + product['color']+ "']"
    color = driver.find_element_by_xpath(w)
    color.click()
    time.sleep(.5)

    # Size selector option 3 is for large
    size = driver.find_element_by_xpath("//*[@id='s']/option[3]")
    size.click()

    # Add to cart
    add = driver.find_element_by_xpath("//input[@name='commit']")
    add.click()
    time.sleep(.5)

    # To cart
    checkout = driver.find_element_by_xpath("//a[@class='button checkout']")
    checkout.click()

    order()
