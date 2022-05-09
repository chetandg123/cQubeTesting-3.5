import unittest

from cQube_Dashboard.Exception_List.sat_exception.Semester_Assessment_Test_Exception import \
    Semester_Assessment_Test_Exception
from reuse_func import GetData

'''Script perform the functionality test of blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class cQube_semester_exception_report(unittest.TestCase):
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

    def test_Semester_Blocks(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_markers_on_block_map()
        self.assertNotEqual(0, res, msg="markers are not present on block level map")

    def test_semester_clusters(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_markers_on_clusters_map()
        self.assertNotEqual(0, res, msg="markers are not present on cluster level map")

    def test_semesterschool(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_markers_on_school_map()
        self.assertNotEqual(0, res, msg="markers are not present on cluster level map")

    def test_DistrictwiseDownload(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_districts_csv_download()
        self.assertEqual(0, res, msg="Some district level csv file is not downloaded")

    def test_ClusterPerBlockCsvDownload(self):
        b = Semester_Assessment_Test_Exception(self.driver)
        res = b.check_csv_download()
        self.assertEqual(0, res, msg='Some cluster level files are not downloaded')

    def test_options(self):
        d = Semester_Assessment_Test_Exception(self.driver)
        res = d.sem_exception_options_test()
        self.assertEqual(0, res, msg='Csv file is downloaded')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
