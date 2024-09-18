# -*- coding: utf-8 -*-
import logging
import json
from .utils import get_cloud_sql_instances


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
            check_function_name = rule.get("check_function")
            check_function = getattr(self, check_function_name, None)
            if callable(check_function):
                try:
                    check_function(rule)
                except Exception as e:
                    logging.error(f"Error during check '{rule['id']}': {e}")
                    # Output the gcloud command for debugging
                    gcloud_command = rule.get("gcloud_command")
                    if gcloud_command:
                        logging.info(
                            f'{"You can run the following gcloud command to debug:"}'
                        )
                        logging.info(gcloud_command)
            else:
                logging.error(f"Check function {check_function_name} not implemented.")

    def check_sql_instances_not_public(self, rule):
        instances = get_cloud_sql_instances()
        for instance in instances:
            authorized_networks = instance.get("authorizedNetworks", [])
            if "0.0.0.0/0" in authorized_networks:
                logging.warning(f"Instance '{instance['name']}' is open to the world.")
                if not self.dry_run:
                    self.remediate_instance(instance)
                else:
                    logging.debug(
                        "Dry-run mode enabled. No remediation will be performed."
                    )
                # Output the gcloud command for debugging
                gcloud_command = rule.get("gcloud_command")
                if gcloud_command:
                    logging.info(
                        f'{"You can run the following gcloud command to debug:"}'
                    )
                    logging.info(gcloud_command)
            else:
                logging.info(f"Instance '{instance['name']}' is secure.")

    def remediate_instance(self, instance):
        logging.info(f"Remediating instance '{instance['name']}'...")
        # Placeholder for actual remediation logic
        logging.debug("Applying changes to the instance.")
        # Implement the API call to update the instance configuration
