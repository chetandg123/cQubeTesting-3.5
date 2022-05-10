import unittest
from HTMLTestRunner import HTMLTestRunner

from Admin_Console.summary_statistics import test_crc_summary, test_diksha_data_summary, test_dikshatpd_file_summary, \
    test_infra_summary, test_inspection_summary, test_pat_file_summary, test_semester_summary, \
    test_static_block_file_summary, test_static_cluster_file_summary, test_static_districtfile_summary, \
    test_static_school_file_summary, test_student_summary, test_udise_summary
from get_dir import pwd

''' Test suite is performs the validation of each data source summary result table '''


class MyTestSuite(unittest.TestCase):

    def test_Issue01(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_crc_summary.TestCrcSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_diksha_data_summary.TestDikshaSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_dikshatpd_file_summary.TestDikshaTPDSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_infra_summary.TestInfraSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_inspection_summary.TestInspectionSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_pat_file_summary.TestPatSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_semester_summary.TestSemesterSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_static_block_file_summary.TestStaticBlockSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase
            (test_static_cluster_file_summary.TestStaticClusterSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase
            (test_static_districtfile_summary.TestStaticDistrictSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase
            (test_static_school_file_summary.TestStaticSchoolSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_student_summary.TestSummaryReport),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_udise_summary.TestUdiseFileSummary),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Summary Functional Test Report',
            verbosity=1,
            description="Admin Console Test Result "
        )

        runner1.run(functional_test)
        outfile.close()
