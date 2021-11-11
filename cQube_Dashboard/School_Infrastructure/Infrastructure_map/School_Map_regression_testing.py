import time
import unittest
from Locators.parameters import Data
from cQube_Dashboard.School_Infrastructure.Infrastructure_map.Infrastructure_access_by_location import \
    Infrastructure_access_by_location

from reuse_func import GetData


class cQube_SI_Map_Report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        time.sleep(2)
        self.data.navigate_to_school_infrastructure_map()
        time.sleep(3)


    def test_hyperlink(self):
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_link()
        if "school-infra-map" in self.driver.current_url:
            print("school infra map based report present")
        else:
            print("home icon is not working ")

    def test_districtwise_download(self):
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_donwload()
        self.assertEqual(0,res,msg="mismatch found at no of school values")
        self.data.page_loading(self.driver)

    def test_schools_per_cluster_csv_download1(self):
        school = Infrastructure_access_by_location(self.driver)
        result = school.check_download_csv1()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download1 is working")



    def test_logout(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.logout).click()
        self.data.page_loading(self.driver)
        count = 0
        print(self.driver.title)
        if 'Log in to cQube' in self.driver.title:
            print('logout button is working and Login page is displayed')
        else:
            print("logout button is not working ")
            count = count + 1
        self.assertEqual(0,count,msg='logout button is not worked')
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        self.data.page_loading(self.driver)

    def test_infrascore(self):
        b = Infrastructure_access_by_location(self.driver)
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

    def test_infrascores(self):
        b = Infrastructure_access_by_location(self.driver)
        res = b.test_infrascores()
        self.assertNotEqual(0, res, msg="infra score options not contains in drop down")
        print("checked with infrascores options")

    def test_click_on_block_cluster_school(self):
        b = Infrastructure_access_by_location(self.driver)
        res1,res2 = b.test_blocks_button()
        self.assertNotEqual(0, res1, msg="Records are not present on map ")
        self.assertTrue(res2,msg='Block wise file downloading is not working ')
        print("Block buttons is working...")

        b = Infrastructure_access_by_location(self.driver)
        res1, res2 = b.test_clusterbtn()
        self.assertNotEqual(0, res1, msg="Records are not present on map ")
        self.assertTrue(res2, msg='Cluster wise file downloading is not working ')
        print("cluster button is working ")

        b = Infrastructure_access_by_location(self.driver)
        res1,res2 = b.test_click_on_school_btn()
        self.assertNotEqual(0, res1, msg="Records are not present on map ")
        self.assertTrue(res2, msg='School wise file downloading is not working ')
        print("school button is working ")

    def test_no_of_schools(self):
        b = Infrastructure_access_by_location(self.driver)
        r, r1, r2, r3 = b.test_check_total_schoolvalue()
        self.assertEqual(int(r), int(r1), msg="mis match found in no of school in block level")
        self.assertEqual(int(r), int(r2), msg="mis match found in no of school in cluster level")
        self.assertEqual(int(r), int(r3), msg="mis match found in no of school in school level")
        self.data.page_loading(self.driver)
        print("checked with comapared with footer values ")


    def test_block_cluster_schools_infrascores(self):
        b = Infrastructure_access_by_location(self.driver)
        result = b.test_click_blocks()
        self.data.page_loading(self.driver)
        print("block button is worked and infra scores is working ")

        b = Infrastructure_access_by_location(self.driver)
        result = b.test_click_clusters()
        self.data.page_loading(self.driver)
        print("cluster button is worked and infra scores is working ")

        b = Infrastructure_access_by_location(self.driver)
        self.driver.implicitly_wait(30)
        res = b.test_click_schools()
        self.data.page_loading(self.driver)
        print("school button is worked and infra scores is working ")

    def test_homebtn(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.sch_infra).click()
        time.sleep(2)
        self.data.page_loading(self.driver)
        count = 0
        if 'infrastructure-dashboard' in self.driver.current_url:
            print("infrastructure-dashboard Dashboard page is displayed ")
        else:
            print('cQube logo home button is not working ')
            count = count + 1
        self.assertEqual(0,count,msg='Landing page does not exists')
        self.driver.find_element_by_id(Data.inframap).click()
        time.sleep(2)
        self.data.page_loading(self.driver)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

