import time
import unittest

from cQube_Dashboard.Teacher_Professional_Development.tpd_completion.tpd_completion_percentage_report import \
    tpd_completion_percentage_report
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , chart 
etc '''


class cQube_completion_percentage_functional(unittest.TestCase):
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
        self.data.navigate_to_tpd_completion_percentage()
        time.sleep(3)

    def test_completion_percentage_icon(self):
        b = tpd_completion_percentage_report(self.driver)
        res = b.test_completion_percentage_icon()
        self.assertEqual(0, res, msg="Completion icon is not working ")
        self.data.page_loading(self.driver)

    def test_Homebtn_functionalities(self):
        b = tpd_completion_percentage_report(self.driver)
        res = b.test_homebtn_funtion()
        self.assertEqual(res, 0, msg="Homebtn is not worked")
        self.data.page_loading(self.driver)

    def test_hyperlink_function(self):
        b = tpd_completion_percentage_report(self.driver)
        b.test_hyperlink_function()
        print("Hyper link is working ")
        self.data.page_loading(self.driver)

    def test_Click_download_icon(self):
        b = tpd_completion_percentage_report(self.driver)
        res = b.test_check_download_icon()
        self.assertEqual(res, 0, msg='Districtwise csv file is not downloaded')
        self.data.page_loading(self.driver)

    def test_districtwise_records(self):
        b = tpd_completion_percentage_report(self.driver)
        res, res1 = b.test_district_selectbox()
        self.assertEqual(0, res, msg='Some district csv file is not downloaded')
        self.assertNotEqual(0, res1, msg="Collection items are not present")
        self.data.page_loading(self.driver)

    def test_blockwise_records(self):
        b = tpd_completion_percentage_report(self.driver)
        res, res1 = b.test_blocks_selectbox()
        self.assertEqual(0, res, msg='Some Blocks csv file is not downloaded')
        self.assertNotEqual(0, res1, msg="Collection items are not present")
        self.data.page_loading(self.driver)

    def test_clusterwise_records(self):
        b = tpd_completion_percentage_report(self.driver)
        res = b.test_clusters_selectbox()
        self.assertEqual(0, res, msg='Some Cluster csv file is not downloaded')
        # self.assertNotEqual(0, res1, msg="Collection items are not present")
        self.data.page_loading(self.driver)

    def test_logout_button(self):
        b = tpd_completion_percentage_report(self.driver)
        res = b.click_on_logout_btn()
        self.assertEqual(0, res, msg='Logout btn is not working ')
        self.data.page_loading(self.driver)

    def test_collection_records_districtwise(self):
        b = tpd_completion_percentage_report(self.driver)
        res1, res2 = b.test_download_collection_options()
        self.assertNotEqual(0, res1, msg='Collection names are not present')
        self.assertEqual(0, res2, "Collection name csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_collection_records_district(self):
        b = tpd_completion_percentage_report(self.driver)
        res1, res2 = b.test_districtwise_collections()
        self.assertNotEqual(0, res1, msg='Collection names are not present')
        self.assertEqual(0, res2, "Collection name csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_collection_records_block(self):
        b = tpd_completion_percentage_report(self.driver)
        res1, res2 = b.test_blockwise_collections()
        self.assertNotEqual(0, res1, msg='Collection names are not present')
        self.assertEqual(0, res2, "Collection name csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_collection_records_cluster(self):
        b = tpd_completion_percentage_report(self.driver)
        res1, res2 = b.test_clusterwise_collections()
        self.assertNotEqual(0, res1, msg='Collection names are not present')
        self.assertEqual(0, res2, "Collection name csv file is not downloaded")
        self.data.page_loading(self.driver)

    def test_download_raw_files(self):
        b = tpd_completion_percentage_report(self.driver)
        b.test_overall_rawfile_download()
        self.assertEqual(0, b, msg="Raw file is not downloaded..")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
