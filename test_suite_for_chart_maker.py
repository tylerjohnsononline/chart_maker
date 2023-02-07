import unittest
import numpy as np
sample_array = np.arange(3)

class RetrievePhotoTestCase(unittest.TestCase):
#   def setUp():
  def test_that_this_is_an_array(self):
    self.assertIsInstance(sample_array, "scalar")
#   def test_that_the_array_is_a_scalar(self):
    

if __name__ == '__main__':
    unittest.main()
