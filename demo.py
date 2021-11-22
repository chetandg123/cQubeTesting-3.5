import re
import time

from Locators.parameters import Data
from reuse_func import GetData

data = GetData()

driver = data.get_driver()
driver.get("https://cqube-release.tibilprojects.com/")
data.login_cqube(driver)
data.navigate_to_student_report()
data.click_on_state(driver)
data.page_loading(driver)
total_students = driver.find_element_by_id(Data.students).text
students = re.sub("\D", "", total_students)
student_count = students

no_schools = driver.find_element_by_id(Data.schoolcount).text
print(no_schools)
schools = re.sub("\D", "", no_schools)
school_count = schools


driver.find_element_by_id(Data.SAR_Blocks_btn).click()
data.page_loading(driver)
time.sleep(5)

block_stds = students
block_schs = schools

print(student_count,block_stds,school_count,block_schs)