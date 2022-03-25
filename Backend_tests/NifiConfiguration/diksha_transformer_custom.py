import unittest
from reuse_func import GetData


class DikshaTransformerCustom(unittest.TestCase):

    def test_diksha_transformer_custom_runningcount(self):
        cal = GetData()
        runningcount = cal.get_runningCount("diksha_transformer_custom")
        if runningcount == 0:
            print("diksha transformer custom running count is 0 after installation")
        else:
            self.assertEqual(0, runningcount, "diksha transformer custom is at started stage after installation")

    def test_diksha_transformer_custom_invalidCount(self):
        cal = GetData()
        invalidCount = cal.get_invalidCount("diksha_transformer_custom")
        if invalidCount == 0:
            print("diksha transformer custom invalid count is 0 after installation")
        else:
            self.assertEqual(0, invalidCount, "diksha transformer custom invalid count is not 0 after installation")

    def test_diksha_transformer_custom_stoppedCount(self):
        cal = GetData()
        stopped = cal.get_stoppedCount("diksha_transformer_custom")
        if stopped == 0:
            self.assertNotEqual(0, stopped, "diksha transformer custom should be at stopped stage after installation")
        else:
            print("diksha transformer custom stopped count is" + " " + str(stopped) + " " + "after installation")


if __name__ == '__main__':
    unittest.main()
