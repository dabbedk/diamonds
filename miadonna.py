from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv

driver = webdriver.Chrome(r'C:\Users\David\chromedriver.exe')

driver.get('https://www.miadonna.com/collections/lab-created-diamonds')

# Exit pop-up ad
wait_button = WebDriverWait(driver, 30)
ad_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//div[@title="Close"]')))
ad_button.click()

# create .csv file
csv_file = open('miadonna_diamonds.csv', 'w', newline = '')
writer = csv.writer(csv_file)

# Loop scoll-to-view of auto-loader to view all diamonds
while True:

    print('Scrolling to access more diamonds.')

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, -1450)")
    time.sleep(10)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        # try again (can be removed)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, -1450)")
        time.sleep(10)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # check if the page height has remained the same
        if new_height == last_height:
            break
        else:

            last_height = new_height
            continue

print('Scroll complete. All diamonds accessed.')
print('Scraping diamond data...')

diamonds = driver.find_elements_by_xpath('//*[@class="results-grid ui-table headers-align-left"]/tbody/tr')

for diamond in diamonds:

    try:

        diamond_dict = {}

        carat = diamond.find_element_by_xpath('./td[2]').text
        
        color = diamond.find_element_by_xpath('./td[4]').text

        clarity = diamond.find_element_by_xpath('./td[5]').text

        cut = diamond.find_element_by_xpath('./td[3]').text

        price = diamond.find_element_by_xpath('./td[6]').text

        print([carat, color, clarity, cut, price])

    except:
        print('Problem getting variable(s)!')
        continue

    diamond_dict['carat'] = carat
    diamond_dict['color'] = color
    diamond_dict['clarity'] = clarity
    diamond_dict['cut'] = cut
    diamond_dict['price'] = price

    writer.writerow(diamond_dict.values())

csv_file.close()
print('Scrape complete. Data written onto csv file.')
