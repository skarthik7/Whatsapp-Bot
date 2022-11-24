from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

contact = input("contact name: ")
text = input("Message:")
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("hit enter after login")
print("Logged In")
times = int(input("How many times should the msg be sent?"))

click_chat = driver.find_element("xpath","//span[@title='"+contact+"']")
click_chat.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
input_box = driver.find_element("xpath",inp_xpath)
time.sleep(2)
for i in range(times):
    input_box.send_keys(text + Keys.ENTER)
time.sleep(10)
driver.quit()