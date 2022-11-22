import joblib

from typing import Any, Dict

from internal_nodes_pb2 import EtlOutput
from public_input_pb2 import Request


def init(ctx):
    ctx.logger.info("Initializing runner")

    encoder_path = ctx.path("models/encoder.joblib")
    ctx.logger.info(f"Loading encoder from {encoder_path}")

    encoder: Dict = joblib.load(encoder_path)
    ctx.set("encoder", encoder)
    ctx.logger.info("Encoder loaded")


async def default_handler(ctx, data):
    req = Request()
    data.Unpack(req)
    encoder: Dict = ctx.get("encoder")
    return new_etl_output(ctx, encoder, req)


def new_etl_output(ctx, encoder: Dict[str, Any], req: Request):
    res = EtlOutput()
    res.request.CopyFrom(req)

    model_input = res.model_input
    model_input.bedrooms = req.bedrooms
    model_input.bathrooms = req.bathrooms
    model_input.accommodates = req.accommodates
    model_input.beds = req.beds
    model_input.latitude = req.latitude
    model_input.longitude = req.longitude
    model_input.tv = bool(req.tv)
    model_input.elevator = bool(req.elevator)
    model_input.internet = bool(req.internet)
    model_input.room_type = encoder["room_type"][req.room_type]
    model_input.neighbourhood = encoder["neighbourhood"][req.neighbourhood]

    await ctx.send_output(res)
    return
