"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Request(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOM_TYPE_FIELD_NUMBER: builtins.int
    BEDROOMS_FIELD_NUMBER: builtins.int
    BATHROOMS_FIELD_NUMBER: builtins.int
    ACCOMMODATES_FIELD_NUMBER: builtins.int
    BEDS_FIELD_NUMBER: builtins.int
    NEIGHBOURHOOD_FIELD_NUMBER: builtins.int
    LATITUDE_FIELD_NUMBER: builtins.int
    LONGITUDE_FIELD_NUMBER: builtins.int
    TV_FIELD_NUMBER: builtins.int
    ELEVATOR_FIELD_NUMBER: builtins.int
    INTERNET_FIELD_NUMBER: builtins.int
    room_type: builtins.str
    bedrooms: builtins.int
    bathrooms: builtins.float
    accommodates: builtins.int
    beds: builtins.int
    neighbourhood: builtins.str
    latitude: builtins.float
    longitude: builtins.float
    tv: builtins.int
    elevator: builtins.int
    internet: builtins.int
    def __init__(
        self,
        *,
        room_type: builtins.str = ...,
        bedrooms: builtins.int = ...,
        bathrooms: builtins.float = ...,
        accommodates: builtins.int = ...,
        beds: builtins.int = ...,
        neighbourhood: builtins.str = ...,
        latitude: builtins.float = ...,
        longitude: builtins.float = ...,
        tv: builtins.int = ...,
        elevator: builtins.int = ...,
        internet: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accommodates", b"accommodates", "bathrooms", b"bathrooms", "bedrooms", b"bedrooms", "beds", b"beds", "elevator", b"elevator", "internet", b"internet", "latitude", b"latitude", "longitude", b"longitude", "neighbourhood", b"neighbourhood", "room_type", b"room_type", "tv", b"tv"]) -> None: ...

global___Request = Request

@typing_extensions.final
class Response(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    MARKET_PRICE_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    success: builtins.bool
    message: builtins.str
    market_price: builtins.str
    category: builtins.str
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        message: builtins.str = ...,
        market_price: builtins.str = ...,
        category: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["category", b"category", "market_price", b"market_price", "message", b"message", "success", b"success"]) -> None: ...

global___Response = Response

@typing_extensions.final
class SaveMetricRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREDICTED_CATEGORY_FIELD_NUMBER: builtins.int
    REAL_CATEGORY_FIELD_NUMBER: builtins.int
    DATE_FIELD_NUMBER: builtins.int
    predicted_category: builtins.str
    real_category: builtins.str
    date: builtins.int
    def __init__(
        self,
        *,
        predicted_category: builtins.str = ...,
        real_category: builtins.str = ...,
        date: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["date", b"date", "predicted_category", b"predicted_category", "real_category", b"real_category"]) -> None: ...

global___SaveMetricRequest = SaveMetricRequest

@typing_extensions.final
class SaveMetricResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    success: builtins.bool
    message: builtins.str
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message", b"message", "success", b"success"]) -> None: ...

global___SaveMetricResponse = SaveMetricResponse
