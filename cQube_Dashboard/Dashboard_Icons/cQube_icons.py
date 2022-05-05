import time

from Locators.parameters import Data
from reuse_func import GetData


class cQube_landing_page():
    def __init__(self, driver):
        self.driver = driver

    # School infrastructure reports
    def test_school_infrastructure_map(self):
        count = 0
        self.data = GetData()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.sch_infra).click()
        if 'infrastructure-dashboard' not in self.driver.current_url:
            print("School infrastructure Report Dashboard is not displayed")
            count = count + 1
        else:
            print("infrastructure-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.inframap).click()
            if "school-infra-map" in self.driver.current_url:
                print("Navigated to  School infrastructure map based report")
            else:
                print("School infra map based report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_composite_chart_map(self):
        count=0
        self.data = GetData()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.sch_infra).click()
        if 'infrastructure-dashboard' not in self.driver.current_url:
            print("School infrastructure Report Dashboard is not displayed")
            count = count + 1
        else:
            print("infrastructure-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.composite).click()
            if "school-infrastructure" in self.driver.current_url:
                print("Navigated to  School infrastructure chart report")
            else:
                print("School infrastructure chart  report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_udise_report(self):
        self.data = GetData()
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.sch_infra).click()
        if 'infrastructure-dashboard' not in self.driver.current_url:
            print("Udise Dashboard is not displayed")
            count = count + 1
        else:
            print("UDISE-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.udise).click()
            self.data.page_loading(self.driver)
            if "udise-report" in self.driver.current_url:
                print("Navigated to udise report home page")
            else:
                print("udise report home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    # Student Performance Reports

    def test_Semester_map(self):
        count = 0
        self.data = GetData()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Report Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.satmap).click()
            if "sat-report" in self.driver.current_url:
                print("Navigated to  Semester report")
            else:
                print("Semester report is not exist")
                count = count+1
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_Semester_heatchart(self):
        count = 0
        self.data = GetData()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Report Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.sat_heatchart).click()
            if "sat-heat-chart" in self.driver.current_url:
                print("Navigated to  Semester Heatchart report")
            else:
                print("Semester Heatchart report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_periodic_map_report(self):
        self.data = GetData()
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.satmap).click()
            self.data.page_loading(self.driver)
            if "pat-report" in self.driver.current_url:
                print("Navigated to peirodic map report home page")
            else:
                print("periodic map report home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_periodic_lo_report(self):
        self.data = GetData()
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.patlotable).click()
            self.data.page_loading(self.driver)
            if "PAT-LO-table" in self.driver.current_url:
                print("Navigated to PAT-LO-table home page")
            else:
                print("PAT-LO-table home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_periodic_heatchart_report(self):
        self.data = GetData()
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard-dashboard is displayed ...")
            time.sleep(2)
            self.driver.find_element_by_id(Data.patheatchart).click()
            self.data.page_loading(self.driver)
            if "heat-chart" in self.driver.current_url:
                print("Navigated to PAT heatchart home page")
            else:
                print("PAT-heatchart home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    #Attendance Reports
    def test_SAR(self):
        self.data = GetData()
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.attendance).click()
        if 'attendance-dashboard' not in self.driver.current_url:
            print("Attendance Dashboard is not displayed")
            count = count + 1
        else:
            print("Attendance Dashboard is displayed...")
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.studentattendance).click()
            if "student-attendance" in self.driver.current_url:
                print("Navigated to Student attendance report")
            else:
                print("Student attendance report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_TAR(self):
        count = 0
        self.data = GetData()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.attendance).click()
        if 'attendance-dashboard' not in self.driver.current_url:
            print("attendance Report Dashboard is not displayed")
            count = count + 1
        else:
            print("attendance Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.teacherattendance).click()
            if "teacher-attendance" in self.driver.current_url:
                print("Navigated to  Teacher coming soon page ")
            else:
                print(" Teacher coming soon page is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    #Diksha TPD Reports
    def test_usage_by_course_report(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("TPD Dashboard is not displayed")
            count = count + 1
        else:
            print("teacher Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.usage_course).click()
            self.data.page_loading(self.driver)
            if 'usage-by-course' in self.driver.current_url:
                print('usage-by-course is displayed ')
            else:
                print("usage-by-course should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_usage_by_content_course_report(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("TPD Dashboard is not displayed")
            count = count + 1
        else:
            print("teacher Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.content_course).click()
            self.data.page_loading(self.driver)
            if 'usage-by-course-content' in self.driver.current_url:
                print('usage-by-course-content is displayed')
            else:
                print("usage-by-course-content should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_tpd_course_progress(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("TPD Dashboard is not displayed")
            count = count + 1
        else:
            print("TPD Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.course_progress).click()
            self.data.page_loading(self.driver)
            if 'tpd-course-progress' in self.driver.current_url:
                print('Diksha TPD Course progress report is present')
            else:
                print('TPD Course progress report is not displayed')
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_tpd_enrollment_icon(self):
        self.data = GetData()
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("TPD Dashboard is not displayed")
            count = count + 1
        else:
            print("TPD Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.tpd_enrollment).click()
            self.data.page_loading(self.driver)
            if 'tpd-enrollment' in self.driver.current_url:
                print('TPD Enrollment report is displayed ')
            else:
                print('TPD Enrollment icon is not working ')
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_tpd_completion_icon(self):
        self.data = GetData()
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("TPD Dashboard is not displayed")
            count = count + 1
        else:
            print("TPD Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.completion_percentage).click()
            self.data.page_loading(self.driver)
            if 'tpd-completion' in self.driver.current_url:
                print('TPD completion report is displayed ')
            else:
                print('TPD completion icon is not working ')
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count


    #Diksha ETB
    def test_usage_by_textbook_report(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.diksha_ETB).click()
        if 'etb-dashboard' not in self.driver.current_url:
            print("ETB Dashboard is not displayed")
            count = count + 1
        else:
            print("ETB Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.usage_textbook).click()
            self.data.page_loading(self.driver)
            if 'usage-by-textbook' in self.driver.current_url:
                print('usage-by-textbook is displayed ')
            else:
                print("usage-by-textbook should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def test_usage_by_content_textbook_report(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.diksha_ETB).click()
        if 'etb-dashboard' not in self.driver.current_url:
            print("ETB Dashboard is not displayed")
            count = count + 1
        else:
            print(" ETB Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.content_textbook).click()
            self.data.page_loading(self.driver)
            if 'usage-by-textbook-content' in self.driver.current_url:
                print('usage-by-textbook-content is displayed')
            else:
                print("usage-by-textbook-content should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    #CRC Visits
    def test_crc_visit_report(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.crc_visit).click()
        if 'crc-dashboard' not in self.driver.current_url:
            print("CRC Dashboard is not displayed")
            count = count + 1
        else:
            print(" CRC Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.crcreport).click()
            self.data.page_loading(self.driver)
            if 'crc-report' in self.driver.current_url:
                print('crc-report is displayed')
            else:
                print("crc-report should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    # composite Across metric
    def check_composite_metrics(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.composite_metrics).click()
        print(self.driver.current_url)
        if 'composite-dashboard' not in self.driver.current_url:
            print("composite-dashboard is not displayed")
            count = count + 1
        else:
            print("composite-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.composite_metric).click()
            time.sleep(3)
            self.data.page_loading(self.driver)
            if 'composite-report' not in self.driver.current_url:
                print(self.driver.current_url,' - composite-report is not displayed')
            else:
                print('entering to report',self.driver.current_url)
                print("composite-report is  displayed")
                self.data.page_loading(self.driver)
                self.driver.find_element_by_id(Data.cQube_logo).click()
                self.data.page_loading(self.driver)
            return count

    #Progress card
    def test_progress_Card(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.progress_card).click()
        if 'prograss-card-dashboard' not in self.driver.current_url:
            print("prograss-card-dashboard is not displayed")
            count = count + 1
        else:
            print(" prograss-card-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.Progresscard).click()
            self.data.page_loading(self.driver)
            if 'progressCard' in self.driver.current_url:
                print('progressCard is displayed')
            else:
                print("progressCard should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    #Exception List

    def check_semester_Exception_report_icon(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(5)
        self.driver.find_element_by_id('exceptList').click()
        if 'exception-dashboard' not in self.driver.current_url:
            print("exception-dashboard is not displayed")
            count = count + 1
        else:
            print("exception-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.semesterexception).click()
            self.data.page_loading(self.driver)
            time.sleep(2)
            if 'sem-exception' in self.driver.current_url:
                print('sem-exception is displayed')
            else:
                print("sem-exception should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_periodic_Exception_report_icon(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.Exception_Reports).click()
        if 'exception-dashboard' not in self.driver.current_url:
            print("exception-dashboard is not displayed")
            count = count + 1
        else:
            print("exception-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.patexception).click()
            self.data.page_loading(self.driver)
            if 'pat-exception' in self.driver.current_url:
                print('pat-exception is displayed')
            else:
                print("pat-exception should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_student_Exception_report_icon(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.Exception_Reports).click()
        if 'exception-dashboard' not in self.driver.current_url:
            print("exception-dashboard is not displayed")
            count = count + 1
        else:
            print("exception-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.studentexception).click()
            self.data.page_loading(self.driver)
            if 'student-attendance-exception' in self.driver.current_url:
                print('student-attendance-exception is displayed')
            else:
                print("student-attendance-exception should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_teacher_Exception_report_icon(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.Exception_Reports).click()
        if 'exception-dashboard' not in self.driver.current_url:
            print("exception-dashboard is not displayed")
            count = count + 1
        else:
            print("exception-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.teacherexception).click()
            self.data.page_loading(self.driver)
            if 'teacher-attendance-exception' in self.driver.current_url:
                print('teacher-attendance-exception is displayed')
            else:
                print("teacher-attendance-exception should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_isdata_exception_list(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.Exception_Reports).click()
        if 'exception-dashboard' not in self.driver.current_url:
            print("exception-dashboard is not displayed")
            count = count + 1
        else:
            print("exception-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.isData).click()
            time.sleep(2)
            if 'download-missing-data' not in self.driver.current_url:
                print('download-missing-data is not displayed')
                return count
            else:
                print("download-missing-data is displayed in url ")
                self.data.page_loading(self.driver)
                self.driver.find_element_by_id(Data.cQube_logo).click()
                self.data.page_loading(self.driver)
            return count

    #Telemetry
    def check_telemetry_icon(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.Telemetry).click()
        if 'telemetry-dashboard' not in self.driver.current_url:
            print("telemetry-dashboard is not displayed")
            count = count + 1
        else:
            print("telemetry-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.tele_report).click()
            time.sleep(2)
            self.data.page_loading(self.driver)
            if 'telemetry' in self.driver.current_url:
                print('telemetry is displayed')
            else:
                print("telemetry should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    #TPD Diksha
    def check_usage_by_course(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("tpd-dashboard is not displayed")
            count = count + 1
        else:
            print("tpd-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.usage_course).click()
            self.data.page_loading(self.driver)
            if 'usage-by-course' in self.driver.current_url:
                print('usage-by-course is displayed')
            else:
                print("usage-by-course should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_usage_by_content_course(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("tpd-dashboard is not displayed")
            count = count + 1
        else:
            print("tpd-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.content_course).click()
            self.data.page_loading(self.driver)
            if 'usage-by-course-content' in self.driver.current_url:
                print('usage-by-course-content is displayed')
            else:
                print("usage-by-course-content should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_course_progress(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("tpd-dashboard is not displayed")
            count = count + 1
        else:
            print("tpd-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.course_progress).click()
            self.data.page_loading(self.driver)
            if 'tpd-course-progress' in self.driver.current_url:
                print('tpd-course-progress is displayed')
            else:
                print("tpd-course-progress should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_enrollment_report(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("tpd-dashboard is not displayed")
            count = count + 1
        else:
            print("tpd-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.tpd_enrollment).click()
            self.data.page_loading(self.driver)
            if 'tpd-enrollment' in self.driver.current_url:
                print('tpd-enrollment is displayed')
            else:
                print("tpd-enrollment should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_tpd_completion_report(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.tpd_opts).click()
        if 'tpd-dashboard' not in self.driver.current_url:
            print("tpd-dashboard is not displayed")
            count = count + 1
        else:
            print("tpd-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.completion_percentage).click()
            time.sleep(3)
            if 'tpd-completion' in self.driver.current_url:
                print(self.driver.current_url,'tpd-completion is displayed')
            else:
                print(self.driver.current_url,"tpd-completion should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    #ETB Reports
    def check_usage_by_textbook(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.diksha_ETB).click()
        if 'etb-dashboard' not in self.driver.current_url:
            print("etb-dashboard is not displayed")
            count = count + 1
        else:
            print("etb-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.usage_textbook).click()
            self.data.page_loading(self.driver)
            if 'usage-by-textbook' in self.driver.current_url:
                print(self.driver.current_url,'usage-by-textbook is displayed')
            else:
                print(self.driver.current_url,"usage-by-textbook should be display in url ")
                count = count + 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
        return count

    def check_usage_by_content_textbook(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.diksha_ETB).click()
        if 'etb-dashboard' not in self.driver.current_url:
            print("etb-dashboard is not displayed")
            count = count + 1
        else:
            print("etb-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.content_textbook).click()
            time.sleep(4)
            self.data.page_loading(self.driver)
            if 'usage-by-textbook-content' in self.driver.current_url:
                print(self.driver.current_url,'usage-by-textbook-content is displayed')
            else:
                print(self.driver.current_url,"usage-by-textbook-content should be display in url ")
                count = count + 1
                self.data.page_loading(self.driver)
                self.driver.find_element_by_id(Data.cQube_logo).click()
                self.data.page_loading(self.driver)
        return count