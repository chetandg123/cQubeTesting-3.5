import time


from reuse_func import GetData

data = GetData()

driver = data.get_driver()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://cqube.tibilprojects.com")

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("Tibil@123")

driver.find_element_by_id("login").click()
time.sleep(3)

if "home" in driver.current_url:
    print("Login is successfull")
    print("************************passsed*************************************** ")
    driver.close()
else:
    print("Login is not working ")
    print("****************************failed*************************************")
    driver.close()




