# -*- coding: utf-8 -*-
import unittest
import sys
import os

from src.utils import get_cloud_sql_instances


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestUtils(unittest.TestCase):
    def test_get_cloud_sql_instances(self):
        instances = get_cloud_sql_instances()
        self.assertGreater(len(instances), 0)
        self.assertIn("name", instances[0])


if __name__ == "__main__":
    unittest.main()
