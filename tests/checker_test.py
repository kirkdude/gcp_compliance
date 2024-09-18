# -*- coding: utf-8 -*-
import unittest
from src.checker import ComplianceChecker


class TestComplianceChecker(unittest.TestCase):
    def setUp(self):
        self.checker = ComplianceChecker(dry_run=True)

    def test_load_rules(self):
        rules = self.checker.load_rules()
        self.assertGreater(len(rules), 0)
        self.assertEqual(rules[0]["id"], "SQL-001")

    def test_check_sql_instances_not_public(self):
        self.checker.check_sql_instances_not_public()
        # Since we're using mocked data, we can assert based on that
        # For example, ensure that the warning was logged
        # This would require a logging handler or mock


if __name__ == "__main__":
    unittest.main()
