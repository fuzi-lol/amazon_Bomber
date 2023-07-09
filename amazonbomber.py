
from selenium import webdriver 
import time 
browser = webdriver.Chrome("/home/student/Downloads/chromedriver_linux64/chromedriver")  
frequency = 10
   
mobile_number ="938983773932927"
  
for i in range(frequency): 
    browser.get('https://www.amazon.in/ap/signin?openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F_encoding%3DUTF8%26ref_%3Dnavm_em_hd_re_signin&ref_=nav_em_0_1_1_26_hd_clc_signin') 
  
    number = browser.find_element_by_id('ap_email')
    number.send_keys(mobile_number)
    cont=browser.find_element_by_id('continue')
    cont.click()
    time.sleep(2)
    otp=browser.find_element_by_id('continue')
    otp.click()
    time.sleep(3)
      
    
browser.quit() 

