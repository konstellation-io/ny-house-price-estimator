from internal_nodes_pb2 import EtlOutput
from main import init, handler
from unittest import mock
import os

import pytest
import joblib


class CtxMock:
    logger = mock.Mock()
    set = mock.Mock()
    get = mock.Mock()

    def path(self, p):
        return os.path.join("../../", p)


def test_init():
    ctx = CtxMock()
    init(ctx)

    ctx.set.assert_called_once_with("encoder", mock.ANY)


@pytest.mark.asyncio
async def test_handler():
    ctx = CtxMock()
    ctx.get.return_value = joblib.load('../../models/encoder.joblib')

    expected_result = EtlOutput()
    req = expected_result.request
    model_input = expected_result.model_input

    req.neighbourhood = "Queens"
    req.latitude = 40.74228
    req.longitude = -73.90049
    req.room_type = "Private room"
    req.bedrooms = 1
    req.bathrooms = 1
    req.accommodates = 1
    req.beds = 1
    req.tv = 0
    req.elevator = 0
    req.internet = 0

    model_input.neighbourhood = 2
    model_input.latitude = 40.74228
    model_input.longitude = -73.90049
    model_input.room_type = 2
    model_input.bedrooms = 1
    model_input.bathrooms = 1
    model_input.accommodates = 1
    model_input.beds = 1
    model_input.tv = False
    model_input.elevator = False
    model_input.internet = False

    class DataMock:
        def Unpack(self, obj):
            obj.neighbourhood = req.neighbourhood
            obj.latitude = req.latitude
            obj.longitude = req.longitude
            obj.room_type = req.room_type
            obj.bedrooms = req.bedrooms
            obj.bathrooms = req.bathrooms
            obj.accommodates = req.accommodates
            obj.beds = req.beds
            obj.tv = req.tv
            obj.elevator = req.elevator
            obj.internet = req.internet

    result = await handler(ctx, DataMock())
    assert result == expected_result
