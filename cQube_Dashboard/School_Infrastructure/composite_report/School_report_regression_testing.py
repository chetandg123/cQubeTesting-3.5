import time
import unittest

from cQube_Dashboard.School_Infrastructure.composite_report.Composite_Report import Composite_Report
from reuse_func import GetData


class cQube_SI_Report(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_composite_infrastructure()
        self.data.page_loading(self.driver)

    def test_dashboard(self):
        b = Composite_Report(self.driver)
        res = b.test_menulist()
        print("check with dashboard options is working fine ")
        self.data.page_loading(self.driver)

    def test_download_blockwise(self):
        b = Composite_Report(self.driver)
        res = b.test_block()
        self.assertEqual(0, res, msg="File is not downloaded")
        print("blockwise csv file downloaded")
        self.data.page_loading(self.driver)

    def test_download_districtwise(self):
        b = Composite_Report(self.driver)
        res = b.test_districtwise()
        self.assertEqual(0, res, msg="File is not downloaded")
        print("districtwise csv file is downloaded")
        self.data.page_loading(self.driver)

    def test_download_clusterwise(self):
        b = Composite_Report(self.driver)
        res = b.test_clusterwise()
        self.assertEqual(0, res, msg="File is not downloaded")
        print("clusterwise csv file is downloaded")
        self.data.page_loading(self.driver)

    def test_download_schoolwise(self):
        b = Composite_Report(self.driver)
        res = b.test_schoolwise()
        self.assertEqual(0, res, msg="File is not downloaded")
        print("schoolwise csv file is downloaded")
        self.data.page_loading(self.driver)

    # def test_check_hyperlinks(self):
    #     hyperlinks = Composite_Report(self.driver)
    #     choose_dist = hyperlinks.click_on_hyperlinks()
    #     print('checked with hyperlinks from district , block and cluster level ')
    #     self.data.page_loading(self.driver)

    def test_homebutton(self):
        b = Composite_Report(self.driver)
        res = b.test_homebtn()
        print("homeicon is working..")
        self.assertEqual(res, 0, msg='Home button is not working ')
        self.data.page_loading(self.driver)

    def test_check_orderwise(self):
        b = Composite_Report(self.driver)
        print("Table record order wise..")
        res = b.test_tablevalue()
        print("checked with orderwise of table data")
        self.data.page_loading(self.driver)

    def test_schools_per_cluster_csv_download1(self):
        school = Composite_Report(self.driver)
        result = school.check_csv_download1()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download1 is working")

    def test_tabledata_districtwise(self):
        b = Composite_Report(self.driver)
        res = b.test_table_data()
        if res != 0:
            raise self.failureException('Locators not found on table')
        print("Districtwise table data is present...")
        self.data.page_loading(self.driver)

    def test_logout(self):
        b = Composite_Report(self.driver)
        res = b.test_logout()
        self.assertNotIn(" School Infrastructure report for: ", self.driver.page_source,
                         msg="School infrastructure report not exist ")
        self.assertEqual("Log in to cQube", self.driver.title, msg="logout is not working ")
        print("logout functionality is working...")
        time.sleep(3)
        self.data.login_cqube(self.driver)
        time.sleep(3)
        self.data.navigate_to_composite_infrastructure()
        self.data.page_loading(self.driver)

    def test_plotxvalues(self):
        b = Composite_Report(self.driver)
        res = b.test_xplots()
        print("Checked with xaxis values are working..")
        self.data.page_loading(self.driver)

    def test_plotyvalues(self):
        b = Composite_Report(self.driver)
        res = b.test_yaxis()
        print("Checked with  y axis values are working..")
        self.data.page_loading(self.driver)

    def test_sc_scator_districtwise(self):
        b = Composite_Report(self.driver)
        result = b.test_districtwise()
        self.assertEqual(0, result, msg="No data found")
        print("Checked with each district wise records")
        self.data.page_loading(self.driver)

    def test_sc_scator_blockwise(self):
        b = Composite_Report(self.driver)
        result = b.test_blockwise()
        self.assertEqual(0, result, msg="No data found")
        print("Checked with each block wise records")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
