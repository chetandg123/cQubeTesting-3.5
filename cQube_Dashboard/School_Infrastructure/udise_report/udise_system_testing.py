import time
import unittest
from Locators.parameters import Data
from cQube_Dashboard.School_Infrastructure.udise_report.udise_report import UdiseReport
from reuse_func import GetData

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class cQube_UdiseReport(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_udise_report()
        time.sleep(3)

    def test_udise_icon(self):
        count = 0
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print('cQube Landing page is displayed and home button is working fine')
        else:
            print('Home button is not working')
            count = count + 1
        self.driver.find_element_by_id('udise').click()
        self.data.page_loading(self.driver)
        if 'udise-report' in self.driver.current_url:
            print('UDISE Infra_Table_Report home page is displayed ')
        else:
            print("Udise report is not exists ")
            count = count + 1
        self.assertEqual(0, count, msg='Udise report icon not working ')
        self.data.page_loading(self.driver)

    def test_download_districtcsv(self):
        fn = UdiseReport(self.driver)
        res = fn.test_districtwise()
        self.assertEqual(0, res, msg='Districtwise csv is not downloaded')
        self.data.page_loading(self.driver)

    def test_test_school_map_schoollevel_records(self):
        b = UdiseReport(self.driver)
        res = b.check_download_csv1()
        self.assertEqual(0, res, msg="Some school level csv file not downloaded")
        self.data.page_loading(self.driver)

    def test_block_wise_download(self):
        b = UdiseReport(self.driver)
        res, res1 = b.test_download_blockwise()
        self.assertTrue(res, msg='School level csv file is not downloaded')
        self.assertNotEqual(res1, 0, msg='Markers are missing on school level map ')
        print('blockwise csv file download is working')

    def test_cluster_wise_download(self):
        b = UdiseReport(self.driver)
        res, res1 = b.test_download_blockwise()
        self.assertTrue(res, msg='School level csv file is not downloaded')
        self.assertNotEqual(res1, 0, msg='Markers are missing on school level map ')
        print('clusterwise csv file download is working')

    def test_school_wise_download(self):
        b = UdiseReport(self.driver)
        res, res1 = b.test_download()
        self.assertTrue(res, msg='School level csv file is not downloaded')
        self.assertNotEqual(res1, 0, msg='Markers are missing on school level map ')
        print('Schoolwise csv file download is working')

    def test_indices_download(self):
        b = UdiseReport(self.driver)

        indices_score = b.infrastructure_score()
        b.remove_csv()
        self.assertNotEqual(0, indices_score, msg='Failed')

        administation = b.administation()
        b.remove_csv()
        self.assertNotEqual(0, administation, msg='Failed')

        artslab = b.artslab()
        b.remove_csv()
        self.assertNotEqual(0, artslab, msg='Failed')

        community = b.community()
        b.remove_csv()
        self.assertNotEqual(0, community, msg='Failed')

        Enrollment = b.Enrollment()
        b.remove_csv()
        self.assertNotEqual(0, Enrollment, msg='Failed')

        grant = b.grant_expenditure()
        b.remove_csv()
        self.assertNotEqual(0, grant, msg='Failed')

        ictlab = b.ictlab()
        b.remove_csv()
        self.assertNotEqual(0, ictlab, msg='Failed')

        Medical = b.Medical()
        b.remove_csv()
        self.assertNotEqual(0, Medical, msg='Failed')

        nsqf = b.nsqf()
        b.remove_csv()
        self.assertNotEqual(0, nsqf, msg='Failed')

        policy = b.policy()
        b.remove_csv()
        self.assertNotEqual(0, policy, msg='Failed')

        Safety = b.Safety()
        b.remove_csv()
        self.assertNotEqual(0, Safety, msg='Failed')

        School_infrastructure = b.School_infrastructure()
        b.remove_csv()
        self.assertNotEqual(0, School_infrastructure, msg='Failed')

        School_inspection = b.School_inspection()
        b.remove_csv()
        self.assertNotEqual(0, School_inspection, msg='Failed')

        School_perfomance = b.School_perfomance()
        b.remove_csv()
        self.assertNotEqual(0, School_perfomance, msg='Failed')

        Science_lab = b.Science_lab()
        b.remove_csv()
        self.assertNotEqual(0, Science_lab, msg='Failed')

        Teacher_profile = b.Teacher_profile()
        b.remove_csv()
        self.assertNotEqual(0, Teacher_profile, msg='Failed')
        print('selecting each indices and checking csv file is downloading or not ')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
