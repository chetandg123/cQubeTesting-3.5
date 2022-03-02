import unittest

from cQube_Dashboard.Teacher_Professional_Development.tpd_user_on_boarding.user_on_boarding_scripts import \
    user_on_boarding_report
from reuse_func import GetData


class user_on_boarding_line_chart_smoke(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_user_on_boarding_report()
        self.data.page_loading(self.driver)

    def test_navigation_to_user_engagement(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_navigation_to_user_on_boarding_report()
        self.assertEqual(0,method,msg="Navigation to on boarding  is failed")

    def test_check_hyperlink_functionality(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_hyperlink_functionality()
        self.assertEqual(0,method,msg="hyperlink is not working")

    def test_check_selection_of_program_dropdown(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_selection_of_program_dropdown()
        self.assertNotEqual(0,method,msg="check_selection_of_program_dropdown options are not present")

    def test_check_selection_of_course_dropdown(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_selection_of_course_dropdown()
        self.assertEqual(0,method,msg="Selection of course dropdown options")

    def test_check_download_button_on_selection_of_programs(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_download_button_on_selection_of_programs()
        self.assertEqual(0,method,msg='Program wise csv file is not downloaded ')

    def test_check_download_button_on_selection_of_courses(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_download_button_on_selection_of_courses()
        self.assertEqual(0,method,msg='Course wise csv file is not downloaded ')

    def test_check_download_button_on_selection_of_courses_and_districts(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_download_button_on_selection_of_courses_and_districts()
        self.assertEqual(0,method,msg='Course and district wise csv file is not downloaded ')

    def test_check_download_button_on_selection_of_program_courses_and_districts(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_download_button_on_selection_of_program_courses_and_districts()
        self.assertEqual(0,method,msg='check_download_button_on_selection_of_program_courses_and_districts csv file is not downloaded ')

    def test_check_logout_from_report(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_logout_from_report()
        self.assertEqual(0,method,msg="logout button is not working")

    def test_check_download_button_on_statewise(self):
        fun = user_on_boarding_report(self.driver)
        method = fun.check_download_button_on_statewise()
        self.assertEqual(0,method,msg="Download button is not working ")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()