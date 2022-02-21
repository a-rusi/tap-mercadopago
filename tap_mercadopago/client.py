"""REST client handling, including MercadoPagoStream base class."""

from pathlib import Path
from typing import Any, Dict, Optional

import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


class MercadoPagoStream(RESTStream):
    """MercadoPago stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["base_url"]

    records_jsonpath = "$.results[*]"
    next_page_token_jsonpath = "$.paging[*]"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        auth_token = self.config.get("auth_token")
        return BearerTokenAuthenticator.create_for_stream(self, token=f"{auth_token}")

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        headers["accept"] = "application/json"
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match

        if next_page_token:
            paging: dict = next_page_token
            if paging["offset"] >= paging["total"]:
                return None

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        payload: dict[str, Any] = {}
        if next_page_token:
            payload["offset"] = next_page_token["offset"] + next_page_token["limit"]
        payload["begin_date"] = self.config.get("start_date")
        payload["end_date"] = self.config.get("end_date")

        return payload
