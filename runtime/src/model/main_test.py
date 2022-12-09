import os
from unittest import mock

import joblib
import pytest
from internal_nodes_pb2 import EtlOutput, ModelOutput
from main import handler, init, predict_price_category


class CtxMock:
    logger = mock.Mock()
    set = mock.Mock()
    get = mock.Mock()

    def path(self, p):
        return os.path.join("../../", p)


def test_init():
    ctx = CtxMock()
    init(ctx)

    ctx.set.assert_called_once_with("model", mock.ANY)


@pytest.mark.asyncio
async def test_handler():
    ctx = CtxMock()
    ctx.get.return_value = joblib.load("../../models/model.joblib")

    expected_result = ModelOutput()
    expected_result.request.neighbourhood = "Manhattan"
    expected_result.price_category = 3

    class DataMock:

        def Unpack(self, obj):
            obj.request.neighbourhood = expected_result.request.neighbourhood
            m = obj.model_input
            m.neighbourhood = 5  # Manhattan
            m.latitude = 40.73019
            m.longitude = -73.98505
            m.room_type = 3  # Entire home/apa
            m.bedrooms = 4
            m.bathrooms = 4
            m.accommodates = 12
            m.beds = 5
            m.tv = True
            m.elevator = True
            m.internet = True

    result = await handler(ctx, DataMock())
    assert result == expected_result


def test_get_price_category_lux():
    req = EtlOutput()
    m = req.model_input
    m.neighbourhood = 5  # Manhattan
    m.latitude = 40.73019
    m.longitude = -73.98505
    m.room_type = 3  # Entire home/apa
    m.bedrooms = 4
    m.bathrooms = 4
    m.accommodates = 12
    m.beds = 5
    m.tv = True
    m.elevator = True
    m.internet = True

    clf = joblib.load("../../models/model.joblib")
    cat = predict_price_category(clf, m)
    assert cat == 3


def test_get_price_category_low():
    req = EtlOutput()
    m = req.model_input
    m.neighbourhood = 1  # Bronx
    m.latitude = 40.74228
    m.longitude = -73.90049
    m.room_type = 1  # Shared room
    m.bedrooms = 1
    m.bathrooms = 1
    m.accommodates = 1
    m.beds = 1
    m.tv = False
    m.elevator = False
    m.internet = False

    clf = joblib.load("../../models/model.joblib")
    cat = predict_price_category(clf, m)
    assert cat == 0
