# -*- coding: utf-8 -*-
import unittest
from src.utils import get_cloud_sql_instances


class TestUtils(unittest.TestCase):
    def test_get_cloud_sql_instances(self):
        instances = get_cloud_sql_instances()
        self.assertGreater(len(instances), 0)
        self.assertIn("name", instances[0])


if __name__ == "__main__":
    unittest.main()
