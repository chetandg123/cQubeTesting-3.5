from selenium import webdriver

from get_dir import pwd

p = pwd()

driver = webdriver.Chrome(executable_path= p.get_driver_path())
str1 = driver.capabilities['browserVersion']
str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
print(str1)
print(str2)
print(str1[0:2])
print(str2[0:2])
if str1[0:2] != str2[0:2]:
  print("please download correct chromedriver version")