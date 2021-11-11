import unittest



from cQube_Dashboard.CRC_Visit.CRC_Report import crc_visits
from reuse_func import GetData

class cQube_CRC_Report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
            self.data = GetData()
            self.driver = self.data.get_driver()
            self.data.open_cqube_appln(self.driver)
            self.data.login_cqube(self.driver)
            self.data.navigate_to_crc_report()
            self.data.page_loading(self.driver)
            self.driver.implicitly_wait(100)

    def test_navigate_crc(self):
        b = crc_visits(self.driver)
        res = b.test_crc()
        if "crc-report" in self.driver.current_url:
            print("Navigated back to crc report")
        else:
            print("CRC report is not loaded ")
        self.data.page_loading(self.driver)

    def test_download_districtwise(self):
        b = crc_visits(self.driver)
        result = b.test_districtwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print("district wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_download_blockwise_csv(self):
        b = crc_visits(self.driver)
        result = b.test_blockwise()
        self.assertEqual(0,result, msg="File is not downloaded")
        print("blockwise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_download_clusterwise_csv(self):
        b = crc_visits(self.driver)
        result = b.test_clusterwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print("cluster wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_download_schoolwise(self):
        b = crc_visits(self.driver)
        result = b.test_schoolwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print("district wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_crc_districtwise(self):
        b = crc_visits(self.driver)
        result = b.test_districtwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print('checked with districts records')
        self.data.page_loading(self.driver)

    def test_homeicon(self):
        b = crc_visits(self.driver)
        result = b.test_homeicon()
        self.assertTrue(result, msg="Home button not working ")
        print("checking with home icon and it is working ")
        self.data.page_loading(self.driver)

    def test_schools_per_cluster_csv_download1(self):
        school = crc_visits(self.driver)
        result = school.check_csv_download()
        self.assertEqual(result,0,msg='csv file is not downloaded')
        self.data.page_loading(self.driver)

    def test_districtwise_tabledata(self):
        b = crc_visits(self.driver)
        result = b.test_table_data()
        if result != 0:
            raise self.failureException('Locators not found on table')
        print("checked with districtwise table data")
        self.data.page_loading(self.driver)

    def test_logout(self):
        b = crc_visits(self.driver)
        res = b.test_logout()
        if "crc-report" in self.driver.current_url:
            print("Navigated back to crc report")
        else:
            print("CRC report is not loaded ")
        self.data.page_loading(self.driver)

    def test_crc_graph(self):
        b = crc_visits(self.driver)
        res1, res2 = b.test_plots()
        self.assertNotEqual(0, res1, msg="Xaxis options are not present")
        self.assertNotEqual(0, res2, msg='Yaxis options are not present')
        self.data.page_loading(self.driver)
        print("checked graph x and y axis options")

    def test_orderwise_tabledata(self):
        b = crc_visits(self.driver)
        result = b.test_order()
        self.assertEqual(result, "menu", msg="Menu is not exist")
        print("check order of table records is working ")
        self.data.page_loading(self.driver)

    def test_on_clusterlevel_to_hyperlinks(self):
        b = crc_visits(self.driver)
        result = b.test_hyperlink()
        print("checking hyperlink from cluster levels ")
        self.data.page_loading(self.driver)

    def test_homebutton(self):
        b = crc_visits(self.driver)
        result = b.test_homebutton()
        self.assertEqual(0,result,msg="Home button is not working ")
        print("checking with home icon and it is working ")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()













































































