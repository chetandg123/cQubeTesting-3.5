import unittest
from reuse_func import GetData


class DikshaTransformer(unittest.TestCase):

    def test_diksha_transformer_runningcount(self):
        cal = GetData()
        runningcount = cal.get_runningCount("diksha_transformer")
        if runningcount == 0:
            print("diksha data transformer running count is 0 after installation")
        else:
            self.assertEqual(0, runningcount, "diksha data transformer running count is not 0 after installation")

    def test_diksha_transformer_invalidCount(self):
        cal = GetData()
        invalidCount = cal.get_invalidCount("diksha_transformer")
        if invalidCount == 0:
            print("diksha data transformer invalid count is 0 after installation")
        else:
            self.assertEqual(0, invalidCount, "diksha data transformer invalid count is not 0 after installation")

    def test_diksha_transformer_stoppedCount(self):
        cal = GetData()
        stopped = cal.get_stoppedCount("diksha_transformer")
        if stopped == 0:
            self.assertNotEqual(0, stopped, "diksha data transformer stopped count should not be 0 after installation")
        else:
            print("diksha data transformer stopped count is" + " " + str(stopped) + " " + "after installation")


if __name__ == '__main__':
    unittest.main()
