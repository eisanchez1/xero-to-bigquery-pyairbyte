import airbyte as ab

import config

def create_xero_source() -> ab.Source:
    """Create a Xero source connector."""
    return ab.get_source(
        "source-xero",
        config={
            "credentials": {
                "auth_type": "oauth2_confidential_application",
                "client_id": config.XERO_CLIENT_ID,
                "client_secret": config.XERO_CLIENT_SECRET,
            },
            "tenant_id": config.XERO_TENANT_ID,
            "start_date": "2005-01-01T00:00:00Z",
        },
        install_if_missing=True,
        docker_image=True
    )


def create_bigquery_destination() -> ab.Destination:
    """Create a BigQuery destination connector."""

    # Read the JSON file contents into a string
    with open(file=config.GOOGLE_APPLICATION_CREDENTIALS, mode="r") as f:
        private_key_str = f.read()

    return ab.get_destination(
        "destination-bigquery",
        config={
            "project_id": config.GOOGLE_CLOUD_PROJECT,
            "dataset_id": config.BIGQUERY_DATASET_ID,
            "credentials_json": private_key_str,
            "dataset_location": config.BIGQUERY_DATASET_LOCATION
        },
        install_if_missing=True,
        docker_image=True
    )