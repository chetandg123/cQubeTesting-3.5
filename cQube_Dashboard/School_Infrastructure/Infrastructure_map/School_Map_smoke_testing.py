import time
import unittest

from cQube_Dashboard.School_Infrastructure.Infrastructure_map.Infrastructure_access_by_location import \
    Infrastructure_access_by_location
from reuse_func import GetData


class cQube_SI_Map_Report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(80)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        self.data.page_loading(self.driver)

    def test_click_on_block(self):
        print("Clicking on blocks button ")
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_blocks_button()
        self.assertNotEqual(0, res, msg="Records are not present on map ")
        self.data.page_loading(self.driver)

    def test_check_district_names(self):
        print("check with districtwise drop down")
        b = Infrastructure_access_by_location(self.driver)
        result = b.test_districtlist()
        self.assertNotEqual(0, result, msg="All Districts are not present in select box!..")
        self.data.page_loading(self.driver)

    def test_check_markers_on_map(self):
        print("checking markers on map ")
        b = Infrastructure_access_by_location(self.driver)
        result = b.test_map()
        self.assertNotEqual(0,result,msg="Locators not present on map")
        self.data.page_loading(self.driver)


    def test_districtwise_download(self):
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_donwload()
        self.assertEqual(0, res, msg="mismatch found at no of school values")
        self.data.page_loading(self.driver)

    def test_click_on_home(self):
        print("check with footer values")
        b = Infrastructure_access_by_location(self.driver)
        c1, c2, c3 = b.test_home()
        self.assertNotEqual(0, c1, msg="Records are not present on map ")
        self.assertNotEqual(0, c2, msg="Records are not present on map ")
        self.assertNotEqual(0, c3, msg="Records are not present on map ")
        self.data.page_loading(self.driver)

    def test_no_of_schools(self):
        print("check with no of school values ")
        b = Infrastructure_access_by_location(self.driver)
        r, r1, r2, r3 = b.test_check_total_schoolvalue()
        self.assertEqual(int(r), int(r1), msg="mis match found in no of school in block level")
        self.assertEqual(int(r), int(r2), msg="mis match found in no of school in cluster level")
        self.assertEqual(int(r), int(r3), msg="mis match found in no of school in school level")
        self.data.page_loading(self.driver)



    def test_district_options(self):
        print("districtwise functionality working fine")
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_options()
        self.assertNotEqual(0, res, msg="district list are present")
        self.data.page_loading(self.driver)

    def test_clusterbtn(self):
        print("check with cluster button ")
        b = Infrastructure_access_by_location(self.driver)
        self.assertNotEqual(0, b, msg="Records are not present on map ")
        self.data.page_loading(self.driver)
        time.sleep(5)

    def test_hyperlink(self):
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_link()
        if "school-infra-map" in self.driver.current_url:
            print("school infra map based report present")
        else:
            print("home icon is not working ")
        self.data.page_loading(self.driver)

    def test_infrascore_click(self):
        print("click on each infra scores dropdown")
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_infrascores()
        self.assertNotEqual(0, res, msg="infra score options not contains in drop down")
        self.data.page_loading(self.driver)

    def test_districtwise_csv(self):
        print("download districtwise csv file")
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_districtwise()
        self.data.page_loading(self.driver)

    def test_mouseover_on_dots(self):
        print("mouseover on markers present on map")
        b = Infrastructure_access_by_location(self.driver)
        res  =b.test_mousehover()
        count = self.data.test_mouse_over()
        self.assertNotEqual(0,count,msg="markers not present in map ")
        self.data.page_loading(self.driver)

    def test_blockwise(self):
        print("check with blockwise records")
        b =Infrastructure_access_by_location(self.driver)
        res = b.test_dist_blocks()
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()