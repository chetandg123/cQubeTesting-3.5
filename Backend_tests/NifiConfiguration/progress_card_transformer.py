import unittest
from reuse_func import GetData


class ProgressCardTransformer(unittest.TestCase):

    def test_progress_card_transformer_runningcount(self):
        cal = GetData()
        runningcount = cal.get_runningCount("progress_card_transformer")
        if runningcount == 0:
            print("progress card transformer running count is 0 after installation")
        else:
            self.assertEqual(0,runningcount,"progress card transformer is at started stage after installation")

    def test_progress_card_transformer_invalidCount(self):
        cal = GetData()
        invalidCount = cal.get_invalidCount("progress_card_transformer")
        if invalidCount == 0:
            print("progress card data transformer invalid count is 0 after installation")
        else:
            self.assertEqual(0,invalidCount,"progress card data transformer invalid count is not 0 after installation")

    def test_progress_card_transformer_stoppedCount(self):
        cal = GetData()
        stopped = cal.get_stoppedCount("progress_card_transformer")
        if stopped == 0:
            self.assertNotEqual(0,stopped,"progress card transformer should be at stopped stage after installation")
        else:
            print("progress card transformer stopped count is"+" "+str(stopped)+" "+"after installation")


if __name__ == '__main__':
    unittest.main()
