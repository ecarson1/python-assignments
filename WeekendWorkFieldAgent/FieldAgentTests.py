import unittest

from FieldAgentSolution import is_valid_date, sort_files

class TestHelpers(unittest.TestCase):

    def test_sort_files(self):
        files = ["NYL_FieldAgent_20200101.csv", "NYL_FieldAgent_19940201.csv", "NYL_FieldAgent_00000101.txt", "NYL_FieldAgent_0000010.csv", "NYL_FieldAgent_19980101.csv"]
        sorted_files = sort_files(files)

        self.assertEqual(sorted_files[0], "NYL_FieldAgent_20200101.csv")
        self.assertEqual(sorted_files[1], "NYL_FieldAgent_19980101.csv")
        self.assertEqual(sorted_files[2], "NYL_FieldAgent_19940201.csv")
        self.assertFalse(files[2] in sorted_files)
        self.assertFalse(files[3] in sorted_files)

    def test_is_valid_date(self):
        self.assertTrue(is_valid_date("NYL_FieldAgent_20200101.csv"))
        self.assertFalse(is_valid_date("NYL_FieldAgent_20200232.csv"))
        self.assertFalse(is_valid_date("NYL_FieldAgent_20202201.csv"))
        self.assertFalse(is_valid_date("NYL_FieldAgent_20200001.csv"))

if __name__ == '__main__':
    unittest.main()