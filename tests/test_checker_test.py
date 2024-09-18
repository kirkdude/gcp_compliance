# -*- coding: utf-8 -*-
import unittest
import sys
import os
from unittest.mock import patch
from src.checker import ComplianceChecker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestComplianceChecker(unittest.TestCase):
    def setUp(self):
        self.checker = ComplianceChecker(dry_run=True)

    @patch("src.checker.get_cloud_sql_instances")
    def test_check_sql_instances_not_public(self, mock_get_instances):
        # Mock instances data
        mock_get_instances.return_value = [
            {"name": "sql-instance-1", "authorizedNetworks": ["0.0.0.0/0"]}
        ]
        # Capture the logs
        with self.assertLogs(level="INFO") as log:
            self.checker.run_checks()
            # Check that the gcloud command was output
            self.assertIn(
                "You can run the following gcloud command to debug:", log.output[-2]
            )
            self.assertIn(
                'gcloud sql instances list --filter="settings.ipConfiguration.authorizedNetworks.value=0.0.0.0/0"',
                log.output[-1],
            )


if __name__ == "__main__":
    unittest.main()
