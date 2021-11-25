import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from reuse_func import GetData


class tpd_content_usage_piechart():

    def __init__(self,driver):
        self.driver = driver
        self.data = GetData()

    def check_navigation_to_content_usage_report(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        time.sleep(1)
        self.data.navigate_to_tpd_content_usage_piechart_report()
        if 'content-usage-pie-chart' not in self.driver.current_url:
            print('Content Usage Pie Chart Report is not displayed')
            count = count + 1
        else:
             print("Content Usage Pie Chart Report is displayed")
        return count

    def check_hyperlink_functionality(self):
        count = 0
        self.data.click_on_state(self.driver)
        districts = Select(self.driver.find_element(By.ID,Data.dist_dropdown))
        districts.select_by_index(2)
        print(districts.options[2].text,'is selected')
        time.sleep(1)
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        if districts.first_selected_option.text == districts.options[2].text:
            print("Hyperlink is not working ")
            count = count + 1
        else:
             print("Hyper link is working as expected ")
        return count

    def check_dropdown_options(self):
        self.data.click_on_state(self.driver)
        districts = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        options = len(districts.options) - 1
        return options

    def check_selection_of_options(self):
        self.data.click_on_state(self.driver)
        district = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        spents = len(district.options) - 1
        for i in range(1,spents):
            district.select_by_index(i)
            time.sleep(2)
            print(district.options[i].text,'is selected and chart also displayed...')
        return spents

    def check_piechart_in_screen(self):
        self.data.click_on_state(self.driver)
        self.driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")

    def check_logout_to_report(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element(By.ID,Data.logout).click()
        time.sleep(3)
        if 'cQube' not in self.driver.page_source:
            print("Logout button is not working ")
            count = count + 1
        else:
             print("Logout button is working as expected ")
             self.data.login_cqube(self.driver)
             self.data.navigate_to_tpd_content_usage_piechart_report()
             if 'content-usage-pie-chart' in self.driver.current_url:
                 print(" content-usage-pie-chart  report home page is displayed ")
             else:
                 print("Navigation to content-usage-pie-chart Report is failed !")
                 count = count + 1
        return count