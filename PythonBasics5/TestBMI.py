import unittest
from Day5a import get_bmi, get_bmi_grade

class TestGetBMI(unittest.TestCase):

  def test_get_bmi(self):
    self.assertEqual(round(get_bmi(80, 1.73), 2), 26.73)
    self.assertEqual(round(get_bmi(55, 1.58), 2), 22.03)
    self.assertEqual(round(get_bmi(49, 1.91), 2), 13.43)
    self.assertEqual(round(get_bmi(100, 1.81), 2), 30.52)

  def test_bmi_grade(self):
    self.assertEqual(get_bmi_grade(30.52), "obese")
    self.assertEqual(get_bmi_grade(26.73), "over")
    self.assertEqual(get_bmi_grade(22.03), "normal")
    self.assertEqual(get_bmi_grade(13.43), "under")


  if __name__ == '__main__':
   unittest.main()