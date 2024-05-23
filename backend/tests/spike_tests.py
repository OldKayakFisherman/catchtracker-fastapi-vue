import sys
import unittest

class SpikeTests(unittest.TestCase):

    def test_path_resolution(self):
        print(sys.path[0])
        self.assertTrue(True)
