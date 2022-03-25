import unittest
from reuse_func import GetData


class cQubeDataStorageTransformer(unittest.TestCase):

    def test_cQube_data_storage_transformer_runningcount(self):
        cal = GetData()
        runningcount = cal.get_runningCount("cQube_data_storage")
        if runningcount == 0:
            print("cQube_data_storage transformer running count is 0 after installation")
        else:
            self.assertEqual(0, runningcount, "cQube_data_storage transformer is at started stage after installation")

    def test_cQube_data_storage_transformer_invalidCount(self):
        cal = GetData()
        invalidCount = cal.get_invalidCount("cQube_data_storage")
        if invalidCount == 0:
            print("cQube_data_storage data transformer invalid count is 0 after installation")
        else:
            self.assertEqual(0, invalidCount,
                             "cQube_data_storage data transformer invalid count is not 0 after installation")

    def test_cQube_data_storage_transformer_stoppedCount(self):
        cal = GetData()
        stopped = cal.get_stoppedCount("cQube_data_storage")
        if stopped == 0:
            self.assertNotEqual(0, stopped,
                                "cQube_data_storage transformer should be at stopped stage after installation")
        else:
            print("cQube_data_storage transformer stopped count is" + " " + str(stopped) + " " + "after installation")


if __name__ == '__main__':
    unittest.main()
