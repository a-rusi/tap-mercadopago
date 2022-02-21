"""Stream type classes for tap-mercadopago."""

from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mercadopago.client import MercadoPagoStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class PaymentsStream(MercadoPagoStream):
    """Stream for consuming historic user payments."""

    name = "payments"
    path = "/payments/search"
    primary_keys = ["id"]
    replication_key = "date_last_updated"
    schema = th.PropertiesList(
        th.Property("operation_type", th.StringType),
        th.Property("date_approved", th.DateTimeType),
        th.Property("date_last_updated", th.DateTimeType),
    ).to_dict()
