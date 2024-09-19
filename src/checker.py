# -*- coding: utf-8 -*-
import logging
import json
import subprocess  # nosec: B404
import re
import shlex


class ComplianceChecker:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.rules = self.load_rules()

    def load_rules(self):
        try:
            with open("compliance_rules/rules.json") as f:
                rules = json.load(f)
            logging.debug("Compliance rules loaded successfully.")
            return rules
        except Exception as e:
            logging.error(f"Failed to load compliance rules: {e}")
            return []

    def run_checks(self):
        for rule in self.rules:
            logging.info(f"Running check: {rule['id']} - {rule['description']}")
            gcloud_command = rule.get("gcloud_command")
            if gcloud_command:
                self.run_gcloud_check(rule)
            else:
                logging.error(f"No gcloud_command specified for rule '{rule['id']}'.")

    def run_gcloud_check(self, rule):
        """
        Executes the gcloud command specified in the compliance rule.

        Parses the command into a list and executes it without shell=True to enhance security
        and prevent shell injection vulnerabilities.

        Args:
            rule (dict): The compliance rule containing the gcloud command.
        """
        gcloud_command = rule.get("gcloud_command")
        if not gcloud_command:
            logging.error(f"No gcloud command specified for rule '{rule['id']}'.")
            return

        if not gcloud_command.startswith("gcloud"):
            logging.error(f"Invalid gcloud command in rule '{rule['id']}'.")
            return

        try:
            # Parse the command into a list
            cmd_list = shlex.split(gcloud_command)
            logging.debug(f"Executing gcloud command: {' '.join(cmd_list)}")
            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                check=False,
            )  # nosec: B603

            if result.returncode != 0:
                stderr = result.stderr.strip()
                if self.is_service_disabled_error(stderr):
                    logging.info(
                        f"Service not enabled for rule '{rule['id']}'. Compliance check passed."
                    )
                    return
                elif self.is_permission_denied_error(stderr):
                    logging.error(
                        f"Permission denied while executing gcloud command for rule '{rule['id']}': {stderr}"
                    )
                    return
                else:
                    logging.error(
                        f"Error executing gcloud command for rule '{rule['id']}': {stderr}"
                    )
                    return

            output = result.stdout.strip()
            if output:
                logging.warning(f"Compliance check failed for rule '{rule['id']}':")
                logging.warning(output)
                logging.info("You can run the following gcloud command to debug:")
                logging.info(gcloud_command)
            else:
                logging.info(f"Compliance check passed for rule '{rule['id']}'.")

        except Exception as e:
            logging.error(
                f"Exception occurred while executing gcloud command for rule '{rule['id']}': {e}"
            )

    def is_service_disabled_error(self, stderr):
        """
        Checks if the stderr contains an error indicating that the API is not enabled.
        """
        service_disabled_patterns = [
            r"API \[.*\] not enabled on project",
            r"Cloud [^\s]+ API has not been used in project",
            r"permission to access project [^\s]+ \(or it may not exist\)",
        ]
        for pattern in service_disabled_patterns:
            if re.search(pattern, stderr):
                return True
        return False

    def is_permission_denied_error(self, stderr):
        """
        Checks if the stderr contains a permission denied error.
        """
        permission_denied_patterns = [
            r"Permission denied",
            r"User \[.*\] does not have permission",
            r"Request had insufficient authentication scopes",
        ]
        for pattern in permission_denied_patterns:
            if re.search(pattern, stderr):
                return True
        return False
