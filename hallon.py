import re

from selenium import webdriver

count = 0
browser = webdriver.Chrome('C:\\Users\\esnxnsh\\Downloads\\chromedriver_win32\\chromedriver')

browser.get('https://www.hallon.se/')

# elem = browser.find_element_by_partial_link_text('Våra mobilabonnemang')
# elem.click()
# elem2 = browser.find_element_by_partial_link_text('Beställ')
# elem2.click()

elem3 = browser.find_element_by_xpath('//a[@class="component-button product-hero__mobile-button-button js-hero-mobile-cta js-hero-cta"]')

link = elem3.get_attribute('href')

browser.get(link)

while count == 0:
    numbers_list = browser.find_elements_by_xpath('//option[@value]')
    for number in numbers_list:
        number = number.get_attribute('value')
        # for i in range (0,10):
        #     if number.count(str(i)) > 3:
        #         print(number)
        seq = re.findall(r'(.)\1\1',number)
        seq1 = re.findall(r'(.)\1',number)
        if len(seq)+len(seq1) > 2:
            print(number)
            count += 1

    if count == 0:
        browser.refresh()