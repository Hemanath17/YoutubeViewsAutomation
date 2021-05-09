#import library
from selenium import webdriver
import time
import random



#import driver
driver = webdriver.Chrome("C:\\Users\\Hemanath\\Desktop\\Programs\\chromedriver.exe")


#youtube video

video = ["https://youtu.be/vO3K-W7PLlI",
         "https://youtu.be/LPNv9FRaEWU"]


#play video in loop
for i in range(100):
    print("Running the video for {} time".format(i))
    random_video = random.randint(0,1)
    driver.get(video[random_video])
    sleep_time = random.randint(10, 100)
    time.sleep(sleep_time)

driver.quit()
