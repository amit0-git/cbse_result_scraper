# Author :-Amit Verma
# Phone:- +91 7505574391

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
# chromedriver version :- 92 change if creates problem
driver = webdriver.Chrome('chromedriver.exe')

start = 21707730  # initial roll no.
end = 21707811  # final roll no.
for i in range(start, end+1):
    driver.get('https://cbseresults.nic.in/class12/Class12th21.htm')
    driver.find_element_by_name('regno').send_keys(i)
    driver.find_element_by_name('sch').send_keys(60128)
    driver.find_element_by_css_selector(".btn[value='Submit']").click()
    time.sleep(1)
    roll = driver.find_element_by_xpath(
        '/html/body/div/table[1]/tbody/tr[1]/td[2]/font').text
    name = driver.find_element_by_xpath(
        '/html/body/div/table[1]/tbody/tr[2]/td[2]/font').text

    m1 = driver.find_element_by_xpath(
        '/html/body/div/div/center/table/tbody/tr[2]/td[5]/font').text  # marks of subject 1

    m2 = driver.find_element_by_xpath(
        '/html/body/div/div/center/table/tbody/tr[3]/td[5]/font').text  # marks of subject 2

    m3 = driver.find_element_by_xpath(
        '/html/body/div/div/center/table/tbody/tr[4]/td[5]/font').text  # marks of subject 3

    m4 = driver.find_element_by_xpath(
        '/html/body/div/div/center/table/tbody/tr[5]/td[5]/font').text  # marks of subject 4

    m5 = driver.find_element_by_xpath(
        '/html/body/div/div/center/table/tbody/tr[6]/td[5]/font').text  # marks of subject 5
    with open('result.txt', 'a+') as f:
        """File for appending data"""
        roll1 = 'Roll No:-'+str(roll)
        name1 = 'Name:-'+str(name)
        total = 'Total:-' + \
            str((int(m1)+int(m2)+int(m3)+int(m4)+int(m5)))  # total marks
        percent = 'Percent:-' + \
            str(((int(m1)+int(m2)+int(m3)+int(m4)+int(m5))/500)*100)
        data = roll1+"  "+name1+"  "+total+"  "+percent

        f.write(data)
        f.write('\n')
    time.sleep(1)


driver.close()
