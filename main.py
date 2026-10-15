import airbyte as ab
import source_destination_setup

def replicate_xero_to_bigquery(XERO_OBJECTS: list[str]) -> None:
    """Replicate data from Xero source to BigQuery destination."""
    
    xero_source = source_destination_setup.create_xero_source()
    xero_source.select_streams(XERO_OBJECTS)

    bigquery_destination = source_destination_setup.create_bigquery_destination()
    
    write_result: ab.WriteResult = bigquery_destination.write(
            source_data=xero_source,
            cache=False,                    # Bypass the local DuckDB cache and stream directly from the
                                            # source connector to the destination connector.
            force_full_refresh=True,        # Refresh the destination with a fresh copy of the source data.
        )

def main() -> None:
    """Main function to create source and destination connectors."""

    XERO_OBJECTS = ["contacts","invoices"]

    replicate_xero_to_bigquery(XERO_OBJECTS)

if __name__ == "__main__":
    main()