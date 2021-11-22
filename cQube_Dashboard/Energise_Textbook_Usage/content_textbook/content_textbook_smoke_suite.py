

import unittest

from cQube_Dashboard.Energise_Textbook_Usage.content_textbook.diksha_content_textbook import \
    diksha_content_textbook_report
from reuse_func import GetData


class cQube_content_textbook_smoke(unittest.TestCase):

    @classmethod
    def setUpClass(self):
            self.data = GetData()
            self.driver = self.data.get_driver()
            self.driver.implicitly_wait(100)
            self.data.open_cqube_appln(self.driver)
            self.data.login_cqube(self.driver)
            self.data.page_loading(self.driver)
            self.data.navigate_to_diksha_content_textbook()
            self.data.page_loading(self.driver)

    def test_diksha_page(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_navigation()
        self.assertEqual(res,0,msg='content course page is present but url is not matching to report')
        self.data.page_loading(self.driver)


    def test_content_textbook_hyperlink(self):
        self.data.page_loading(self.driver)
        b = diksha_content_textbook_report(self.driver)
        res = b.test_hyperlink()
        print("checked with hyper link functionality ")
        self.data.page_loading(self.driver)

    def test_textbook_districtwise_records(self):
        b =diksha_content_textbook_report(self.driver)
        res = b.test_alldata_districts()
        self.assertEqual(0,res,msg='Records are not present on table ')
        self.data.page_loading(self.driver)

    def test_textbook_districtwise_lastweek_record(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_each_districts()
        self.assertEqual(res,0,msg='records count mismatch in downloaded file and table records')
        print('checked with last 7days records ')
        self.data.page_loading(self.driver)

    def test_textbook_districtwise_lastday_record(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_each_districts()
        self.assertEqual(res, 0, msg='records count mismatch in downloaded file and table records')
        print('checked with last day records ')
        self.data.page_loading(self.driver)

    def test_textbook_districtwise_lastmonth_chart(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_each_districts()
        self.assertEqual(res, 0, msg='records count mismatch in downloaded file and table records')
        print('checked with last 30 days records ')
        self.data.page_loading(self.driver)

    def test_Districtwise_lastday_records(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_districts()
        self.assertEqual(res,0,msg='Some districts does not have table records')
        self.data.page_loading(self.driver)

    def test_Districtwise_lastweek_records(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_districts()
        self.assertEqual(res,0,msg='Some districts does not have table records')
        self.data.page_loading(self.driver)

    def test_Districtwise_monthwise_records(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_districts()
        self.assertEqual(res, 0, msg='Some districts does not have table records')
        self.data.page_loading(self.driver)


    def test_homebutton(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_homebutton()
        print('Home btn is working ')
        self.data.page_loading(self.driver)



    def test_Table_orderwise(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_tablevalue()
        print("checking order of the table and working as per requirement ")
        self.data.page_loading(self.driver)

    def test_content_textbook_logout(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_logout()
        self.assertEqual(res,'Log in to cQube',msg="logout button is not working")
        self.data.page_loading(self.driver)


    def test_download_raw_files_overall_period(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_overall_rawfile_download()
        self.assertEqual(0,res,msg='Raw file is not downloaded')

    def test_download_raw_files_last_30days_period(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_last_30_days_rawfile_download()
        self.assertEqual(0,res,msg='Raw file is not downloaded')

    def test_download_raw_files_last_7_day_period(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_last_7_days_rawfile_download()
        self.assertEqual(0,res,msg='Raw file is not downloaded')

    def test_download_raw_files_lastday_period(self):
        b = diksha_content_textbook_report(self.driver)
        res = b.test_last_day_rawfile_download()
        self.assertEqual(0,res,msg='Raw file is not downloaded')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()