from datetime import datetime

from public_input_pb2 import SaveMetricRequest, SaveMetricResponse


async def handler(ctx, data):
    req = SaveMetricRequest()
    data.Unpack(req)

    ctx.logger.info(f"Adding real value to prediction: {req.real_category}")
    date = datetime.fromtimestamp(req.date)
    await ctx.prediction.save(req.predicted_category, req.real_category, date)

    res = SaveMetricResponse()
    res.success = True
    res.message = 'Prediction metric saved'

    return res
