import sys
sys.path.append("..")
import unittest
from scripts_py_template.utils import read_geojson

class Test_geojson(unittest.TestCase):
    def test_geojson(self):
        """Test geojson reading and writing"""
        features = read_geojson('tests/fixtures/points.geojson')
        self.assertEqual(len(features), 2)
