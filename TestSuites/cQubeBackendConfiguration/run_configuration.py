from Backend_tests.cQubeBaseDir import directory
from Backend_tests.DataBase import check_database_created
from Backend_tests.DataBase import check_db_username_password
from Backend_tests.NifiConfiguration import nifi
from Backend_tests.NifiConfiguration import timezone
from Backend_tests.NifiConfiguration import cQube_data_storage
from Backend_tests.NifiConfiguration import composite
from Backend_tests.NifiConfiguration import crc
from Backend_tests.NifiConfiguration import data_replay
from Backend_tests.NifiConfiguration import diksha
from Backend_tests.NifiConfiguration import diksha_transformer_custom
from Backend_tests.NifiConfiguration import infra
from Backend_tests.NifiConfiguration import pat
from Backend_tests.NifiConfiguration import sat
from Backend_tests.NifiConfiguration import static
from Backend_tests.NifiConfiguration import student
from Backend_tests.NifiConfiguration import teacher_attendance
from Backend_tests.NifiConfiguration import telemetry
from Backend_tests.NifiConfiguration import udise
from Backend_tests.NifiConfiguration import progress_card_transformer
from Backend_tests.cQubeLoginPage import cqube
from get_dir import pwd
import unittest
from HTMLTestRunner import HTMLTestRunner


class MyTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("")

    def test_Issue1(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(directory.CqubeDir)
        ])
        p = pwd()
        outfile = open(p.get_nifi_processor_group_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Check cQube Base Directory Created or Not Test Report',
            verbosity=2,
        )

        runner1.run(functional_test)
        outfile.close()

    def test_Issue2(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(nifi.NifiDashboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(timezone.NifiTimeZone),
            unittest.defaultTestLoader.loadTestsFromTestCase(cQube_data_storage.cQubeDataStorageTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(static.StaticTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(student.StudentTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_attendance.TeacherAttendanceTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(crc.CrcTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(infra.InfraTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(pat.PatTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(sat.SatTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise.UdiseTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(diksha.DikshaTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(diksha_transformer_custom.DikshaTransformerCustom),
            unittest.defaultTestLoader.loadTestsFromTestCase(composite.CompositeTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(progress_card_transformer.ProgressCardTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(data_replay.DataReplayTransformer),
            unittest.defaultTestLoader.loadTestsFromTestCase(telemetry.TelemetryTransformer)

        ])
        p = pwd()
        outfile = open(p.get_nifi_processor_group_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Nifi Configuration Test Report',
            verbosity=2,
        )
        runner1.run(functional_test)
        outfile.close()

    def test_Issue3(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(check_database_created.Database),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_db_username_password.Database)

        ])
        p = pwd()
        outfile = open(p.get_nifi_processor_group_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Database Configuration Test Report',
            verbosity=2,
        )

        runner1.run(functional_test)
        outfile.close()

    def test_Issue4(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(cqube.CqubeLogin)

        ])
        p = pwd()
        outfile = open(p.get_nifi_processor_group_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='cQube login page Test Report',
            verbosity=2,

        )

        runner1.run(functional_test)
        outfile.close()


    @classmethod
    def tearDownClass(self):
        print("")


if __name__ == '__main__':
    unittest.main()
