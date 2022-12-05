import os

from google.protobuf.json_format import MessageToDict

from typing import Any, Dict, Tuple

from internal_nodes_pb2 import ModelOutput
from public_input_pb2 import Response

MEASUREMENT = "features"
MEASUREMENT_TAGS = Dict[str, Any]

PRICE_RANGES = ("10-90", "91-180", "181-400", "+401")
PRICE_LABELS = ("low", "mid", "high", "lux")


def init(ctx):
    ctx.logger.info("Reading currency from env var...")
    currency = os.getenv("OUTPUT_PRICE_CURRENCY")
    ctx.set("currency", currency)
    ctx.logger.info("Currency loaded correctly")


async def default_handler(ctx, data) -> None:
    req = ModelOutput()
    data.Unpack(req)

    market_price, label = get_market_price_and_label(req.price_category, ctx.get("currency"))
    ctx.logger.info(f"Estimated market price[{market_price}] with label[{label}]")

    # Stores input fields and prediction to measurements
    measurement_fields = MessageToDict(
        req.request, preserving_proto_field_name=True, including_default_value_fields=True
    )
    measurement_fields["prediction"] = label
    ctx.measurement.save(MEASUREMENT, measurement_fields, MEASUREMENT_TAGS)

    res = Response()
    res.success = True
    res.message = "Predicted market price"
    res.market_price = market_price
    res.category = label

    await ctx.send_output(res)
    return


def get_market_price_and_label(price_cat: int, currency: str) -> Tuple[str, str]:
    market_price = f"{PRICE_RANGES[price_cat]} {currency}"
    label = PRICE_LABELS[price_cat]
    return market_price, label
