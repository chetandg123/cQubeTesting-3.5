import time

from selenium.webdriver.support.select import Select

from reuse_func import GetData

cal = GetData()
driver = cal.get_driver()
driver.implicitly_wait(100)
driver.get("https://uat-pds-billing-info.pdsnew.com/")

driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("admin")
driver.find_element_by_id("login").click()

# alert = Alert(driver)
# alert.dismiss()
time.sleep(20)
a = Select(driver.find_element_by_id("selectHospitalGroup"))
time.sleep(5)
a.select_by_visible_text("COLUMB")
year = Select(driver.find_element_by_id("selectYear"))
i = 0
for i in range(1,len(year.options)):
    year.select_by_index(i)
    print(year.options[i].text)
    time.sleep(8)
    z = "No Locators Found"
    value = "Overall Revenue v/s Transactions-" + "year.options[i].text"
    if z in driver.page_source:
        print(year.options[0].text, "is not having data")
        i = i + 1
    else:
        if a == value:
            assert True
            driver.refresh()

