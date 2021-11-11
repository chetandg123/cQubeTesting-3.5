import os
import time
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

    def test_blockwise_data(self):
        b = crc_visits(self.driver)
        result = b.test_blocklevel()
        self.assertEqual(0,result,msg="some district files are not downloaded")
        print("blockwise csv files are downloaded")

    def test_table_data(self):
        b= crc_visits(self.driver)
        result = b.test_table_data()
        self.assertNotEqual(0,result,"Locators not found on table")
        print("Table contains records...")


    def test_districtwise_tabledata(self):
        b = crc_visits(self.driver)
        result = b.test_table_data()
        if result != 0:
            raise self.failureException('Locators not found on table')
        print("Check with Districtwise table records")

    def test_homeicon(self):
        b=crc_visits(self.driver)
        result = b.test_homeicon()
        self.assertTrue(result,msg="Home button not working ")
        print("checking functionality of home button ")

    def test_peformance_blockwise(self):
        b = crc_visits(self.driver)
        result = b.test_blockwise()
        self.assertTrue(result, msg = "Blockwise csv is not downloaded")
        print("Block wise csv file is downloaded within 10 seconds")
        b.remove_file()

    def test_peformance_clusterwise(self):
        b = crc_visits(self.driver)
        result = b.test_clusterwise()
        self.assertTrue(result, msg = "File is not downloaded")
        print("cluster wise csv file is downloaded within 10 seconds")
        b.remove_file()


    def test_peformance_districtwise(self):
        b = crc_visits(self.driver)
        result = b.test_districtwise_csv()
        self.assertTrue(result, msg = "Districtwise csv is not downloaded")
        print("district wise csv file is downloaded within 10 seconds")
        b.remove_file()



    def test_peformance_of_crc_report(self):
        b = crc_visits(self.driver)
        result = b.test_crc_report()
        if "crc-report" in self.driver.current_url:
            print("CRC report page is exists")
        else:
            print("CRC report page is not loaded ")

    def test_orderwise_tabledata(self):
        print("checking order of table records")
        b = crc_visits(self.driver)
        result = b.test_order()
        self.assertEqual(result,"menu",msg="Menu is not exist")


    def test_crc_graph(self):
        b = crc_visits(self.driver)
        result = b.test_plots()
        self.assertNotEqual(0,result,msg="Axis options are not contains in select box")
        self.data.page_loading(self.driver)
        print("checking with graph values ")

    def test_clusterlevel_homeicon(self):
        b = crc_visits(self.driver)
        result = b.test_homeicon()
        if "crc-report" in self.driver.current_url:
            print("crc home page is loaded")
        else:
            print("crc home page is not loaded")


    def test_on_clusterlevel_to_hyperlinks(self):
        b = crc_visits(self.driver)
        result = b.test_hyperlink()
        print("checking hyper link is working or not ")


    def test_download_blockwise_csv(self):
        b = crc_visits(self.driver)
        result = b.test_blockwise()
        self.assertTrue(result, msg="File is not downloaded")
        b.remove_file()
        print("Districtwise csv files are downloaded")

    def test_donwoad_clusterwise_csv(self):
        b = crc_visits(self.driver)
        result = b.test_clusterwise()
        self.assertTrue(result, msg = "File is not downloaded")
        b.remove_file()
        print("cluster level csv files are downloaded..")

    def test_visited(self):
        b =crc_visits(self.driver)
        result1,result2 = b.test_schools()
        self.assertEqual(int(result1),result2, msg="total no of visited are mismatching in district level")
        b.remove_file()
        print("comparing visited footer values with downloaded csv files")

    def test_visits(self):
        b =crc_visits(self.driver)
        res1 ,res2  =b.test_visits()
        self.assertEqual(int(res1),res2, msg="total no of visits are mismatching in district level")
        b.remove_file()
        print("comparing visits footer values with downloaded csv files")

    def test_schoolcount(self):
        b = crc_visits(self.driver)
        res1, res2 = b.test_schools()
        self.assertEqual(int(res1), res2, msg="total no of school are mismatching in district level")
        b.remove_csv()
        print("comparing school  footer values with downloaded csv files")

    def test_download_districtwise(self):
        b = crc_visits(self.driver)
        result  = b.test_districtwise()
        self.assertTrue(result, msg="File is not downloaded")
        b.remove_csv()
        print("District csv file is downloaded..")


    def test_logout(self):
        b = crc_visits(self.driver)
        res = b.test_logout()
        if "crc-report" in self.driver.current_url:
            print("Navigated back to crc report")
        else:
            print("CRC report is not loaded ")
        time.sleep(2)


    def test_navigate_crc(self):
        b =crc_visits(self.driver)
        res = b.test_crc()
        if "crc-report" in self.driver.current_url:
            print("Navigated back to crc report")
        else:
            print("CRC report is not loaded ")
        time.sleep(2)

    def test_dash_menu(self):
        b =crc_visits(self.driver)
        res = b.test_dashboard()
        self.assertEqual(res,"menu",msg="Dashboard button is not working")
        print("checking dashboard is working or not..")

    def test_blockwise_graph(self):
        b = crc_visits(self.driver)
        res = b.test_blockwise_graph()
        if "myChart" in self.driver.page_source:
            print("CRC Scattor plot is working fine")
        else:
            print("CRC plot is not exist..")
        self.data.page_loading(self.driver)

    def test_clusterwise_graph(self):
        b = crc_visits(self.driver)
        res = b.test_clusterwise_graph()
        if "myChart" in self.driver.page_source:
            print("CRC Scattor plot is working fine")
        else:
            print("CRC plot is not exist..")
        self.data.page_loading(self.driver)

    def test_districtwise_schoolsvisited(self):
        b = crc_visits(self.driver)
        result = b.test_districtwise_schoolvisited()
        self.data.page_loading(self.driver)
        print("checking districtwise school visited footer with downloaded csv files")

    def test_crc_blockwise(self):
        b = crc_visits(self.driver)
        result = b.test_blockwise()
        print("checked with blockwise records")
        self.assertNotEqual(0, result, msg="Table data is not loaded ")
        print("checking blockwise school visited footer with downloaded csv files")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()













































































