from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()

driver.get("https://www.grailed.com/sold/EP8S3v8V_w")

scroll_count = 5
for i in range(scroll_count):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

time.sleep(3)

titles = driver.find_elements_by_css_selector("p.listing-designer")
prices = driver.find_elements_by_css_selector("p.sub-title.sold-price")
sizes = driver.find_elements_by_css_selector("p.listing-size.sub-title")
sold = driver.find_elements_by_css_selector("div.-overlay")

data = [titles, prices, sizes, sold]

data = [list(map(lambda element: element.text, arr)) for arr in data]

with open('sold_shoes.csv', 'w') as file:
    writer = csv.writer(file)
    j = 0
    while j < len(titles):
        row = []
        for i in range(len(data)):
            row.append(data[i][j])
        writer.writerow(row)
        j += 1
