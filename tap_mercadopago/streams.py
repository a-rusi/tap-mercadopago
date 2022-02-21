"""Stream type classes for tap-mercadopago."""

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mercadopago.client import MercadoPagoStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


def _build_point_of_interaction_property():
    business_info = th.Property(
        "business_info",
        th.ObjectType(
            th.Property("unit", th.StringType), th.Property("sub_unit", th.StringType)
        ),
    )
    return th.Property(
        "point_of_interaction",
        th.ObjectType(business_info, th.Property("type", th.StringType)),
    )


def _build_fee_details_property():
    return th.Property(
        "fee_details",
        th.ArrayType(
            th.ObjectType(
                th.Property("amount", th.NumberType),
                th.Property("fee_payer", th.StringType),
                th.Property("type", th.StringType),
            )
        ),
    )


def _build_transaction_details_property():
    return th.Property(
        "transaction_details",
        th.ObjectType(
            th.Property("total_paid_amount", th.NumberType),
            th.Property("acquirer_reference", th.StringType),
            th.Property("installment_amount", th.NumberType),
            th.Property("financial_institution", th.StringType),
            th.Property("net_received_amount", th.NumberType),
            th.Property("overpaid_amount", th.NumberType),
            th.Property("external_resource_url", th.StringType),
            th.Property("payable_deferral_period", th.StringType),
            th.Property("payment_method_reference_id", th.StringType),
        ),
    )


class PaymentsStream(MercadoPagoStream):
    """Stream for consuming historic user payments."""

    name = "payments"
    path = "/payments/search"
    primary_keys = ["id"]
    replication_key = "date_last_updated"

    schema = th.PropertiesList(
        _build_point_of_interaction_property(),
        _build_fee_details_property(),
        _build_transaction_details_property(),
        th.Property("corporation_id", th.StringType),
        th.Property("operation_type", th.StringType),
        th.Property("notification_url", th.StringType),
        th.Property("date_approved", th.DateTimeType),
        th.Property("statement_descriptor", th.StringType),
        th.Property("call_for_authorize_id", th.StringType),
        th.Property("installments", th.IntegerType),
        th.Property("pos_id", th.StringType),
        th.Property("external_reference", th.StringType),
        th.Property("date_of_expiration", th.DateTimeType),
        th.Property("id", th.IntegerType),
        th.Property("payment_type_id", th.StringType),
        th.Property("counter_currency", th.StringType),
        th.Property("brand_id", th.StringType),
        th.Property("status_detail", th.StringType),
        th.Property("differential_pricing_id", th.StringType),
        th.Property("live_mode", th.BooleanType),
        th.Property("payer_id", th.IntegerType),
        th.Property("marketplace_owner", th.StringType),
        th.Property("integrator_id", th.IntegerType),
        th.Property("status", th.StringType),
        th.Property("transaction_amount_refunded", th.IntegerType),
        th.Property("transaction_amount", th.NumberType),
        th.Property("description", th.StringType),
        th.Property("money_release_date", th.DateTimeType),
        th.Property("merchant_number", th.IntegerType),
        th.Property("authorization_code", th.StringType),
        th.Property("captured", th.BooleanType),
        th.Property("merchant_account_id", th.IntegerType),
        th.Property("taxes_amount", th.IntegerType),
        th.Property("date_last_updated", th.DateTimeType),
        th.Property("coupon_amount", th.IntegerType),
        th.Property("store_id", th.StringType),
        th.Property("date_created", th.DateTimeType),
        th.Property("sponsor_id", th.IntegerType),
        th.Property("shipping_amount", th.IntegerType),
        th.Property("issuer_id", th.StringType),
        th.Property("payment_method_id", th.StringType),
        th.Property("binary_mode", th.BooleanType),
        th.Property("currency_id", th.StringType),
        th.Property("shipping_cost", th.IntegerType),
    ).to_dict()
