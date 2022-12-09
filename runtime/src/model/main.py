import joblib
from internal_nodes_pb2 import EtlOutput, ModelOutput
from sklearn.ensemble import RandomForestClassifier


def init(ctx) -> None:
    ctx.logger.info("Initializing runner")

    model_path = ctx.path("models/model.joblib")
    ctx.logger.info(f"Loading model from {model_path}")

    model: RandomForestClassifier = joblib.load(model_path)
    ctx.set("model", model)
    ctx.logger.info("Model loaded")


async def default_handler(ctx, data) -> None:
    req = EtlOutput()
    data.Unpack(req)

    clf: RandomForestClassifier = ctx.get("model")
    price_category = int(predict_price_category(clf, req.model_input))

    res = ModelOutput()
    res.request.CopyFrom(req.request)
    res.price_category = price_category

    await ctx.send_output(res)
    return


def predict_price_category(clf: RandomForestClassifier,
                           features: EtlOutput.ModelInput) -> float:
    model_input = [[
        features.accommodates,
        features.room_type,
        features.beds,
        features.bedrooms,
        features.bathrooms,
        features.neighbourhood,
        features.tv,
        features.elevator,
        features.internet,
        features.latitude,
        features.longitude,
    ]]
    prediction = clf.predict(model_input)
    return prediction.item()
