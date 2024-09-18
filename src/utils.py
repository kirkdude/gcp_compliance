# -*- coding: utf-8 -*-
import logging

# from google.cloud import sql_v1beta4


def get_cloud_sql_instances():
    logging.debug("Fetching Cloud SQL instances...")
    # Placeholder for actual API interaction
    # client = sql_v1beta4.SqlAdminServiceClient()
    # response = client.list_instances(project='your-gcp-project-id')
    # return response.items

    # Mocked data for illustration purposes
    instances = [
        {"name": "sql-instance-1", "authorizedNetworks": ["0.0.0.0/0"]},
        {"name": "sql-instance-2", "authorizedNetworks": ["10.0.0.0/24"]},
    ]
    logging.debug(f"Retrieved instances: {instances}")
    return instances
