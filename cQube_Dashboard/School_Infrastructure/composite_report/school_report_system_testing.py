import unittest

from cQube_Dashboard.School_Infrastructure.composite_report.Composite_Report import Composite_Report
from reuse_func import GetData


class cQube_SI_Report(unittest.TestCase):
    data = None
    driver = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(50)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_composite_infrastructure()
        self.data.page_loading(self.driver)

    def test_school_report(self):
        b = Composite_Report(self.driver)
        res = b.test_report()
        self.assertEqual("menu", "menu", msg="Dashboard is not exists!")
        print("Menu list is displayed")
        self.data.page_loading(self.driver)

    def test_download_district_wise(self):
        b = Composite_Report(self.driver)
        path = b.test_schools()
        self.assertEqual(path, 0, msg="File is not downloaded")
        print("districtwise csv file is downloaded")
        self.data.page_loading(self.driver)

    def test_download_blockwise(self):
        b = Composite_Report(self.driver)
        res = b.test_block()
        self.assertEqual(res, 0, msg="File is not downloaded")
        print("blockwise csv file downloaded")
        self.data.page_loading(self.driver)

    def test_schoolwise_download(self):
        b = Composite_Report(self.driver)
        res = b.test_schoolwise()
        self.assertEqual(res, 0, msg="File is not downloaded")
        print("school wise csv file is downloaded")
        self.data.page_loading(self.driver)

    def test_clusterwise_download(self):
        b = Composite_Report(self.driver)
        res = b.test_clusterwise()
        self.assertEqual(res, 0, msg="File is not downloaded")
        print("cluster wise csv file is downloaded")
        self.data.page_loading(self.driver)

    def test_check_orderwise(self):
        b = Composite_Report(self.driver)
        print("Table record order wise..")
        res = b.test_tablevalue()
        print("checked with orderwise of table data")
        self.data.page_loading(self.driver)

    def test_schools_per_cluster_csv_download(self):
        school = Composite_Report(self.driver)
        result = school.check_csv_download1()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download1 is working")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
