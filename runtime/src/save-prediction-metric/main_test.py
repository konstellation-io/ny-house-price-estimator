from datetime import datetime
from unittest import mock
from unittest.mock import AsyncMock

import pytest

from main import handler
from public_input_pb2 import SaveMetricResponse


class CtxMock:
    logger = mock.Mock()
    prediction = AsyncMock()


@pytest.mark.asyncio
async def test_handler():
    class DataMock:
        def Unpack(self, obj):
            obj.predicted_category = "lux"
            obj.real_category = "lux"
            obj.date = 1608110979

    ctx = CtxMock()

    expected_res = SaveMetricResponse()
    expected_res.success = True
    expected_res.message = 'Prediction metric saved'

    result = await handler(ctx, DataMock())
    assert result == expected_res
    ctx.prediction.save.assert_called_once_with('lux', 'lux', datetime(2020, 12, 16, 10, 29, 39))
