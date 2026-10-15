import os

from dotenv import load_dotenv

load_dotenv()

def get_env(name: str) -> str:
    """Retrieve the value of an environment variable and avoid None values.
    Args:
        name (str): The name of the environment variable to retrieve.
    Returns:
        str: The value of the environment variable converted to string.
        
    Raises:
        ValueError: If the environment variable is not set.
    """

    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Environment variable '{name}' is not set.")
    return value

#BigQuery target configuration
GOOGLE_APPLICATION_CREDENTIALS=get_env("GOOGLE_APPLICATION_CREDENTIALS")
GOOGLE_CLOUD_PROJECT=get_env("GOOGLE_CLOUD_PROJECT")
BIGQUERY_DATASET_ID=get_env("BIGQUERY_DATASET_ID")
BIGQUERY_DATASET_LOCATION=get_env("BIGQUERY_DATASET_LOCATION")

#Xero Source configuration
XERO_CLIENT_ID=get_env("XERO_CLIENT_ID")
XERO_CLIENT_SECRET=get_env("XERO_CLIENT_SECRET")
XERO_TENANT_ID=get_env("XERO_TENANT_ID")