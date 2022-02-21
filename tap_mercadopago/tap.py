"""MercadoPago tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_mercadopago.streams import PaymentsStream

STREAM_TYPES = [PaymentsStream]
DEFAULT_BASE_URL = "https://api.mercadopago.com/v1"
DEFAULT_END_DATE = "NOW"
DEFAULT_START_DATE = "NOW-1DAYS"


class TapMercadoPago(Tap):
    """MercadoPago tap class."""

    name = "tap-mercadopago"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            default=DEFAULT_START_DATE,
            description="The earliest record date to sync (default is yesterday)",
        ),
        th.Property(
            "end_date",
            th.DateTimeType,
            default=DEFAULT_END_DATE,
            description=f"The latest record date to sync (default = {DEFAULT_END_DATE})",
        ),
        th.Property(
            "base_url",
            th.StringType,
            default=DEFAULT_BASE_URL,
            description=f"URL of the Mercado Pago API (default = {DEFAULT_BASE_URL})",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
