import unittest

from Locators.parameters import Data
from cQube_Dashboard.Exception_List.sat_exception.Semester_Assessment_Test_Exception import \
    Semester_Assessment_Test_Exception

from reuse_func import GetData

'''Script perform the functionality test of blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class cQube_Semester_Exception_Report(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_exception()
        self.data.page_loading(self.driver)

    def test_DotsOnDistrictwise_map(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_dots_on_each_districts()
        self.assertEqual(0, res, msg='Markers are not present on districtwise map ')
        self.data.page_loading(self.driver)

    def test_Data_not_recieved(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res, r1, r2, r3 = b.test_total_not_recieved_data()
        self.assertEqual(res, r1, msg='Block level data not recieved count mismatch found')
        self.assertEqual(res, r2, msg='cluster level data not recieved count mismatch found')
        self.assertEqual(res, r3, msg='School level data not recieved count mismatch found')
        self.data.page_loading(self.driver)

    def test_Semester_Blocks(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_markers_on_block_map()
        self.assertNotEqual(0, res, msg="markers are not present on block level map")
        self.data.page_loading(self.driver)

    def test_semester_clusters(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_markers_on_clusters_map()
        self.assertNotEqual(0, res, msg="markers are not present on cluster level map")
        self.data.page_loading(self.driver)

    def test_semesterschool(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_markers_on_school_map()
        self.assertNotEqual(0, res, msg="markers are not present on cluster level map")
        self.data.page_loading(self.driver)

    def test_sem_dashboard(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.test_click_on_dashboard()
        self.assertEqual(0, res, msg='Dashboard button is not working ')
        self.data.page_loading(self.driver)

    def test_exception_Home(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.click_on_blocks_click_on_home_icon()
        self.assertEqual(0, res, msg="Home button is not working")
        self.data.page_loading(self.driver)

    def test_sem_exception_hyperlink(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        choose_dist = b.click_on_hyperlinks()
        if choose_dist == self.driver.page_source:
            print("hyperlinks are working")
        else:
            raise self.failureException("hyperlinks are not working")
        self.data.page_loading(self.driver)

    def test_semester_exception_icon(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.test_icon()
        self.assertEqual(0, res, msg='Semester exception report is not displayed')
        self.data.page_loading(self.driver)

    def test_sem_exception_Logout(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.click_on_logout()
        self.assertEqual(res, 'Log in to cQube', msg="logout button is not working")
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_exception()
        self.data.page_loading(self.driver)

    def test_check_DistrictwiseCsv(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.click_download_csv_of_districts()
        self.assertEqual(0, res, msg='mis match found at footer information')
        self.data.page_loading(self.driver)

    def test_homepage(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_semester_exception()
        count = 0
        self.data.page_loading(self.driver)
        if 'sem-exception' in self.driver.current_url:
            print("Home page of sem exception is present ")
        else:
            print('home page does not exist')
            count = count + 1
        self.assertEqual(0, count, msg='Home page not exists')
        self.data.page_loading(self.driver)

    def test_dots(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        count = len(markers) - 1
        self.assertNotEqual(0, count, msg='markers are not present ')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
