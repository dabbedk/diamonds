from selenium import webdriver
import time
import re
import csv

csv_file = open('lab_diamonds.csv', 'w')
writer = csv.writer(csv_file)

driver = webdriver.Chrome(r'C:\Users\David\chromedriver.exe')

driver.get('https://www.cleanorigin.com/diamonds/')

time.sleep(10)

#exit pop-up ad
ad_button = driver.find_element_by_xpath('//div[@title="Close"]')
ad_button.click()

# # Scoll out of view to hide auto-load menu
# time.sleep(1)
# driver.execute_script("window.scrollTo(0, 1500)")
# driver.execute_script("window.scrollTo(0, 200)")
# time.sleep(1)
# driver.execute_script("window.scrollTo(0, 0)")

# select round-cut diamonds
# roundcut_button = driver.find_element_by_id('diamond_shapeFilter_option_1')
# roundcut_button.click()
# time.sleep(5)

diamonds = driver.find_elements_by_xpath('//tr[@class="listing-row"]')

for diamond in diamonds:

    diamond_dict = {}

    try:
        carat = diamond.find_element_by_xpath('.//td[@data-attr="diamond_weight"]').text
        
        color = diamond.find_element_by_xpath('.//td[@data-attr="diamond_color"]').text

        clarity = diamond.find_element_by_xpath('.//td[@data-attr="diamond_clarity"]').text

        cut = diamond.find_element_by_xpath('.//td[@data-attr="diamond_cut_grade"]').text

        price = diamond.find_element_by_xpath('.//*[@class="price-wrapper "]').text
    except:
        print('Problem getting variable(s)!')
        print(f'{driver.current_url}')
        continue

    diamond_dict['carat'] = carat
    diamond_dict['color'] = color
    diamond_dict['clarity'] = clarity
    diamond_dict['cut'] = cut
    diamond_dict['price'] = price

# scroll down to next button
driver.execute_script("window.scrollTo(0, 5250)")

# select next page
time.sleep(2)
next_button = driver.find_element_by_xpath('//*[@class="toolbar toolbar-products bottom"]//li[@class="item pages-item-next"]/a')
next_button.click()

