import unittest
from cQube_Dashboard.Student_Performance.sat_heatchart.sat_heatchart_scripts import Sat_Heat_Chart
from reuse_func import GetData


class cQube_SatChart_Functional_Test(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_sat_heatchart_report()
        self.data.page_loading(self.driver)

    def test_Catagory_series(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.viewbys_options()
        self.assertEqual(0, res, msg='View by csv file is not downloaded')
        self.data.page_loading(self.driver)

    def test_Download_districtwise(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.download_all_district_records()
        self.assertEqual(res, 0, msg="Districtwise csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_exams_series(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.exams_dates()
        self.assertEqual(res, 0, msg="exam date is not displayed on chart")
        self.data.page_loading(self.driver)

    def test_subject_levels(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.subjects_types()
        self.assertEqual(res, 0, msg="Subject's csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_Home_functions(self):
        b = Sat_Heat_Chart(self.driver)
        b.test_homeicons()
        self.data.page_loading(self.driver)

    def test_Homebtn_functions(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.test_homebutton()
        self.assertEqual(res, 0, msg='Homebtn is not working')
        self.data.page_loading(self.driver)

    def test_logout_function(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.test_logoutbtn()
        self.assertEqual(0, res, msg="Logout button is not working ")
        self.data.login_cqube(self.driver)
        self.data.navigate_to_sat_heatchart_report()
        self.data.page_loading(self.driver)

    def test_year_selection(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.test_year_dropdown()
        self.assertEqual(0, res, msg='Year is not selected ')
        self.data.page_loading(self.driver)

    def test_districtwise(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.District_select_box()
        self.assertEqual(0, res, msg='Some districtwise csv file is not downloaded')
        self.data.page_loading(self.driver)

    def test_clusterwise(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.Clusters_select_box()
        self.assertEqual(0, res, msg='Some cluster wise csv file is not downloaded ')
        self.data.page_loading(self.driver)

    def test_gradewise_records(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.grades_files()
        self.assertEqual(0, res, msg='Some grade files are not downloaded')
        self.data.page_loading(self.driver)

    def test_Random_test(self):
        b = Sat_Heat_Chart(self.driver)
        res = b.test_randoms()
        self.assertEqual(0, res, msg='Random selection is failed ')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
