
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities     
import sys
import time
import os


def get_bb_slot(url):
   
   driver = webdriver.Chrome(executable_path = "/usr/local/lib/python3.7/site-packages/chromedriver_binary/chromedriver")#bring the chromedriver exec to the script path
   driver.get(url)
   print("Please login using OTP and then wait for a while.")
   time.sleep(180)


   while 1:
      driver.get(url)     
      time.sleep(2)
      print("Trying to find a slot!")
      try:
         driver.find_element_by_xpath("//button[@id = 'checkout']").click()
         time.sleep(3)  #driver take a few sec to update the new url
         if "checkout" in driver.current_url:
            print("Found the slots!")
            for i in range(60):
               notify("Slots Available!", "Please go and choose the slots!")
               os.system('say "Slots for delivery available!"')
               time.sleep(20)
      except:
         print("If this message pops up multiple times, please find the error and create a PR!")
         pass
      print("No Slots found. Will retry again.")
      time.sleep(120)

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
get_bb_slot('https://www.bigbasket.com/basket/?ver=1')


