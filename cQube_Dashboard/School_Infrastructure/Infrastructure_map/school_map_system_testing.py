import time
import unittest

from cQube_Dashboard.School_Infrastructure.Infrastructure_map.Infrastructure_access_by_location import \
    Infrastructure_Access_By_Location
from reuse_func import GetData

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class cQube_SI_Map_Report(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        time.sleep(5)

    def test_districtwise_download(self):
        b = Infrastructure_Access_By_Location(self.driver)
        res = b.test_donwload()
        self.assertEqual(0, res, msg="mismatch found at no of school values")
        self.data.page_loading(self.driver)

    def test_schools_per_cluster_csv_download1(self):
        school = Infrastructure_Access_By_Location(self.driver)
        result = school.check_download_csv1()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download1 is working")

    def test_infrascore(self):
        b = Infrastructure_Access_By_Location(self.driver)
        infra_score = b.infra_score()
        b.remove_csv()
        self.assertNotEqual(0, infra_score, msg='Failed')

        boy_toilet = b.Boys_toilet_percentage()
        b.remove_csv()
        self.assertNotEqual(0, boy_toilet, msg='Failed')

        drinking_water = b.drinking_water()
        b.remove_csv()
        self.assertNotEqual(0, drinking_water, msg='Failed')

        Electricity = b.Electricity()
        b.remove_csv()
        self.assertNotEqual(0, Electricity, msg='Failed')

        girl_toilet = b.girls_toilet()
        b.remove_csv()
        self.assertNotEqual(0, girl_toilet, msg='Failed')

        Handpump = b.Handpump()
        b.remove_csv()
        self.assertNotEqual(0, Handpump, msg='Failed')

        Handwash = b.Handwash()
        b.remove_csv()
        self.assertNotEqual(0, Handwash, msg='Failed')

        Library = b.Library()
        b.remove_csv()
        self.assertNotEqual(0, Library, msg='Failed')

        Solar_panel = b.Solar_panel()
        b.remove_csv()
        self.assertNotEqual(0, Solar_panel, msg='Failed')

        Tapwater = b.Tapwater()
        b.remove_csv()
        self.assertNotEqual(0, Tapwater, msg='Failed')

        Toilet = b.Toilet()
        b.remove_csv()
        self.assertNotEqual(0, Toilet, msg='Failed')

    def test_click_on_block_cluster_school(self):
        b = Infrastructure_Access_By_Location(self.driver)
        res1, res2 = b.test_blocks_button()
        self.assertNotEqual(0, res1, msg="Records are not present on map ")
        self.assertTrue(res2, msg='Block wise file downloading is not working ')
        print("Block buttons is working...")

        b = Infrastructure_Access_By_Location(self.driver)
        res1, res2 = b.test_clusterbtn()
        self.assertNotEqual(0, res1, msg="Records are not present on map ")
        self.assertTrue(res2, msg='Cluster wise file downloading is not working ')
        print("cluster button is working ")

        b = Infrastructure_Access_By_Location(self.driver)
        res1, res2 = b.test_click_on_school_btn()
        self.assertNotEqual(0, res1, msg="Records are not present on map ")
        self.assertTrue(res2, msg='School wise file downloading is not working ')
        print("school button is working ")

    def test_mouseover_on_dots(self):
        b = Infrastructure_Access_By_Location(self.driver)
        b.test_mousehover()
        count = self.data.test_mouse_over()
        self.assertNotEqual(0, count, msg="markers not present in map ")
        print("markers present on map ")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
