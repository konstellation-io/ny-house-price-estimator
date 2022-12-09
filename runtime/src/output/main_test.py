import os
from unittest import mock

import pytest
from google.protobuf.json_format import MessageToDict
from internal_nodes_pb2 import ModelOutput
from main import handler, init
from public_input_pb2 import Response


class CtxMock:
    logger = mock.Mock()
    set = mock.Mock()
    get = mock.Mock()
    measurement = mock.Mock()

    def path(self, p):
        return os.path.join("../../", p)


def test_init(monkeypatch):
    ctx = CtxMock()

    mock_currency = "EUR"

    def getenv_mocked(var):
        if var == "OUTPUT_PRICE_CURRENCY":
            return mock_currency
        else:
            raise Exception("Must get OUTPUT_PRICE_CURRENCY env var")

    monkeypatch.setattr(os, "getenv", getenv_mocked)

    init(ctx)
    ctx.set.assert_called_once_with("currency", mock_currency)


@pytest.mark.asyncio
async def test_handler():
    ctx = CtxMock()
    ctx.get.return_value = "EUR"

    expected_result = Response()
    expected_result.success = True
    expected_result.message = "Predicted market price"
    expected_result.market_price = "+401 EUR"
    expected_result.category = "lux"

    class DataMock:

        def Unpack(self, obj):
            obj.request.neighbourhood = "Manhattan"
            obj.price_category = 3

    result = await handler(ctx, DataMock())
    assert result == expected_result

    req = ModelOutput()
    req.request.neighbourhood = "Manhattan"
    measurement_fields = MessageToDict(
        req.request,
        preserving_proto_field_name=True,
        including_default_value_fields=True,
    )
    measurement_fields["prediction"] = "lux"
    ctx.measurement.save.assert_called_once_with("features",
                                                 measurement_fields, {})
