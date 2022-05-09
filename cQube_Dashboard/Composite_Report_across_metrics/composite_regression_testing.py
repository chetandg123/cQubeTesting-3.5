import time
import unittest

from Locators.parameters import Data
from cQube_Dashboard.Composite_Report_across_metrics.Composite_Report_Across_Metrics import \
    Composite_report_across_Metric
from reuse_func import GetData

'''Script validating the Graphs , Block level , Cluster level buttons , District , Block and Cluster level metrics 
along with graph '''


class composite_regression_report(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_composite_report()
        self.data.page_loading(self.driver)

    def test_composite_icon(self):
        self.data.page_loading(self.driver)
        count = 0
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.driver.find_element_by_id('composite').click()
        time.sleep(1)
        self.data.page_loading(self.driver)
        if 'composite-dashboard' in self.driver.current_url:
            print("composite-Dashboard page is displayed ")
        else:
            print('Hamburger - composite-Dashboard is not working ')
            count = count + 1
        self.assertEqual(0, count, msg="Home btn is not working ")
        self.driver.find_element_by_id('compositeReport').click()
        self.data.page_loading(self.driver)

    def test_districtwise_csv_download(self):
        b = Composite_report_across_Metric(self.driver)
        res = b.test_districtwise()
        self.assertTrue(res, msg="Districtwise csv file is not downloaded ")
        print("Checked district wise csv downloading functionality is working ")
        b.remove_csv()
        self.data.page_loading(self.driver)

    def test_blockwise_csv_download(self):
        b = Composite_report_across_Metric(self.driver)
        res = b.test_blockwise()
        self.assertTrue(res, msg="Blockwise csv file is not downloaded ")
        print("Checked block wise csv downloading functionality is working ")
        b.remove_file()
        self.data.page_loading(self.driver)

    def test_clusterwise_csv_download(self):
        b = Composite_report_across_Metric(self.driver)
        res = b.test_clusterwise()
        self.assertTrue(res, msg="Clusterwise csv file is not downloaded ")
        print("Checked cluster wise csv downloading functionality is working ")
        b.remove_file()
        self.data.page_loading(self.driver)

    def test_hyperlink(self):
        b = Composite_report_across_Metric(self.driver)
        b.test_hyperlink()
        print("Checked with hyper link ")
        self.data.page_loading(self.driver)

    def test_xaxis_options(self):
        b = Composite_report_across_Metric(self.driver)
        b.test_xplots()
        print("Checked with all xaxis options are selectable")
        self.data.page_loading(self.driver)

    def test_yaxis_options(self):
        b = Composite_report_across_Metric(self.driver)
        b.test_yplots()
        print("Checked with all yaxis options are selectable")
        self.data.page_loading(self.driver)

    def test_homebutton(self):
        b = Composite_report_across_Metric(self.driver)
        res = b.test_homebutton()
        self.assertEqual(0, res, msg="Home button is not working")
        print("Home button is working ")
        self.data.page_loading(self.driver)

    def test_logout_button(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(3)
        self.assertIn('cQube', self.driver.title, msg="Logout button is not working ")
        print("logout button is working fine ")
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_composite_report()
        self.data.page_loading(self.driver)

    def test_blocks_clusters_schools(self):
        self.driver.implicitly_wait(100)
        b = Composite_report_across_Metric(self.driver)
        res = b.click_on_blocks_button()
        self.assertEqual(0, res, msg="Blocks graph is displayed ")
        print("Block wise graph is displayed ")
        self.data.page_loading(self.driver)

        b = Composite_report_across_Metric(self.driver)
        res = b.click_on_clusters_button()
        self.assertEqual(0, res, msg="Cluster graph is displayed ")
        print("Cluster wise graph is displayed ")
        self.data.page_loading(self.driver)

    def test_composite_schoolwise_records(self):
        b = Composite_report_across_Metric(self.driver)
        res = b.check_csv_download()
        self.assertTrue(res, msg="Some of school csv file is not downloaded ")
        print("Checked with School wise csv file downloading ")
        self.data.page_loading(self.driver)

    def test_composite_districtwise_records(self):
        b = Composite_report_across_Metric(self.driver)
        res = b.check_districtwise_csv_download()
        self.assertTrue(res, msg="Some of districtwise csv file is not downloaded ")
        print("Checked with districtwise wise csv file downloading ")
        self.data.page_loading(self.driver)

    def test_composite_clusterwise_records(self):
        b = Composite_report_across_Metric(self.driver)
        res = b.check_csv_download_district_block()
        self.assertTrue(res, msg="Some of clusters csv file is not downloaded ")
        print("Checked with cluster wise csv file downloading ")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
