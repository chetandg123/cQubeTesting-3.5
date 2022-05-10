import unittest

from cQube_Dashboard.CRC_Visit.CRC_Report import CrcVisits
from reuse_func import GetData

'''Script developed to test whether scatter graph , table records , time periods , district , block and cluster level 
crc visits '''


class crc_System_Testing(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_crc_report()
        self.data.page_loading(self.driver)

    def test_dash_menu(self):
        b = CrcVisits(self.driver)
        res = b.test_homeicon()
        self.assertEqual(res, "menu", msg="Dashboard button is not working")
        print("Dashboard icon is working....")
        self.data.page_loading(self.driver)

    def test_download_districtwise(self):
        b = CrcVisits(self.driver)
        result = b.test_districtwise()
        self.assertTrue(result, msg="File is not downloaded")
        b.remove_file()
        print("district wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_download_blockwise_csv(self):
        b = CrcVisits(self.driver)
        result = b.test_blockwise()
        self.assertTrue(result, msg="File is not downloaded")
        b.remove_file()
        print("blockwise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_donwoad_clusterwise_csv(self):
        b = CrcVisits(self.driver)
        result = b.test_clusterwise()
        self.assertTrue(result, msg="File is not downloaded")
        b.remove_file()
        print("cluster wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_download_schoolwise(self):
        b = CrcVisits(self.driver)
        result = b.test_schoolwise()
        self.assertTrue(result, msg="File is not downloaded")
        b.remove_file()
        print("district wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_crc_clusterwise(self):
        b = CrcVisits(self.driver)
        res = b.check_csv_download()
        print("Clusterwise records checking ")
        self.assertEqual(0, res, msg='Some of clusterwise records mismatch found! ')
        self.data.page_loading(self.driver)

    def test_districtwise_tabledata(self):
        b = CrcVisits(self.driver)
        result = b.test_table_data()
        if result != 0:
            raise self.failureException('Locators not found on table')
        print("checked with districtwise table data")
        self.data.page_loading(self.driver)

    def test_crc_graph(self):
        b = CrcVisits(self.driver)
        res1, res2 = b.test_plots()
        self.assertNotEqual(0, res1, msg="x Axis options are not contains in select box")
        self.assertNotEqual(0, res2, msg="y axis options are not present in drop down")
        self.data.page_loading(self.driver)
        print("checked graph x and y axis options")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
