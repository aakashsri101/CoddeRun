from typing import Match
from selenium import webdriver	

# For using sleep function because selenium
# works only when the all the elements of the
# page is loaded.
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
match_dic={}
# Creating an instance webdriver
def matcher():
    browser = webdriver.Chrome()
    browser.get('https://www.cowin.gov.in')
    time.sleep(1)
    # user = browser.find_elements_by_xpath('//*[@id="name1"]')
    # user[0].send_keys('Aakash Srivastava')
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[1]'))
    # select.select_by_visible_text('17')
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[2]'))
    # select.select_by_visible_text('Aug')
    user = browser.find_element_by_xpath('//*[@id="mat-input-0"]')
    user.send_keys('226016')
    # user.send_keys('keys.ENTER')
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[3]'))
    # select.select_by_visible_text('23')
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[4]'))
    # select.select_by_visible_text('40')
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[5]'))
    # select.select_by_visible_text('0')
    
    # user = browser.find_element_by_xpath('//*[@id="place1"]')
    # user.send_keys('Shikohabad')



    # user = browser.find_elements_by_xpath('//*[@id="name2"]')
    # user[0].send_keys('Siddhi Khanna')
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[1]'))
    # select.select_by_visible_text('18')
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[2]'))
    # select.select_by_visible_text('Sept')
    # user = browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/input[2]')
    # user.send_keys('2000')
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[3]'))
    # select.select_by_visible_text(skhh)
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[4]'))
    # select.select_by_visible_text(skmm)
    # select = Select(browser.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[5]'))
    # select.select_by_visible_text('0')
    # user = browser.find_elements_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[1]')
    # user.send_keys('18')
    # user = browser.find_elements_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[2]')
    # user.send_keys('09')
    # user = browser.find_elements_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/input[2]')
    # user.send_keys('2000')
    # user = browser.find_elements_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[3]')
    # user.send_keys('10')
    # user = browser.find_elements_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[4]')
    # user.send_keys('00')
    # user = browser.find_elements_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[5]')
    # user.send_keys('00')
    # user = browser.find_element_by_xpath('//*[@id="place2"]')

    # user.send_keys('Lucknow')

    # LOG = browser.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/div[1]/div/div/button')
    # LOG.send_keys('keys.ENTER')



    # print("Login Successful")
    # conti=browser.find_element_by_xpath('//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[2]/div/div[2]')
    # conti.click()
    # conti.click()
    # print("Success")
#     matchh = browser.find_element_by_xpath('/html/body/div[2]/div/section/div/div[5]/div[1]/div[2]/div[3]/div[2]/div/div[1]/p')
#     # print(matchh.text)
#     if (matchh.text).split('/')[0] in match_dic.keys():
#         match_dic[(matchh.text).split('/')[0]].append(skhh+":"+skmm)
#     else:
#         match_dic[(matchh.text).split('/')[0]]=[skhh+":"+skmm]

#     # time.sleep(0)
#     browser.close()
# fio=open('kundlidata.txt','a')
# fio.write('\n')
matcher()
# for i in range(0,24):
#     for j in range(6,7):
#         matcher(str(i),str(j))
#         if(j==30):
#             print(i,j)
#             fio.write(str(match_dic)+'\n')
#         if(j==59):
#             print(i,j)
#             fio.write(str(match_dic)+'\n')
# # print(match_dic)
# fio.write(str(match_dic)+'\n')
# fio.close()