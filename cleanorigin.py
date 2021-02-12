from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv

driver = webdriver.Chrome(r'C:\Users\David\chromedriver.exe')

driver.get('https://www.cleanorigin.com/diamonds/')

# Exit pop-up ad
wait_button = WebDriverWait(driver, 15)
ad_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//div[@title="Close"]')))
ad_button.click()

# Scoll out of view to hide auto-load menu
time.sleep(.5)
driver.execute_script("window.scrollTo(0, 1200)")
time.sleep(.5)
driver.execute_script("window.scrollTo(0, 150)")

# select round-cut diamonds
roundcut_button = driver.find_element_by_xpath('//a[@datahref="https://www.cleanorigin.com/diamonds?diamond_shape=ROUND"]')
roundcut_button.click()

time.sleep(3)

# create .csv file
csv_file = open('lab_diamonds.csv', 'w', newline = '')
writer = csv.writer(csv_file)

# set page numbers
index = 1
while True:
    try:
        print(f'Scraping Page number {index}...')

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

            writer.writerow(diamond_dict.values())

        print(f'Page {index} scrape successful!')
        index += 1

        # scroll down to next button
        driver.execute_script("window.scrollTo(0, 5250)")

        # select next page
        time.sleep(1)
        next_button = driver.find_element_by_xpath('//*[@class="toolbar toolbar-products bottom"]//li[@class="item pages-item-next"]/a')
        next_button.click()
        time.sleep(3)        

    except Exception as e:
        print(e)
        csv_file.close()
        #driver.close()
        break

print('Full scraping complete!')
csv_file.close()