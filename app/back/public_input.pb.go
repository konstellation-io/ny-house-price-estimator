// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.24.0
// 	protoc        v3.7.1
// source: public_input.proto

package main

import (
	context "context"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type Request struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RoomType      string  `protobuf:"bytes,1,opt,name=room_type,json=roomType,proto3" json:"room_type,omitempty"`
	Bedrooms      int32   `protobuf:"varint,2,opt,name=bedrooms,proto3" json:"bedrooms,omitempty"`
	Bathrooms     float32 `protobuf:"fixed32,3,opt,name=bathrooms,proto3" json:"bathrooms,omitempty"`
	Accommodates  int32   `protobuf:"varint,4,opt,name=accommodates,proto3" json:"accommodates,omitempty"`
	Beds          int32   `protobuf:"varint,5,opt,name=beds,proto3" json:"beds,omitempty"`
	Neighbourhood string  `protobuf:"bytes,6,opt,name=neighbourhood,proto3" json:"neighbourhood,omitempty"`
	Latitude      float32 `protobuf:"fixed32,7,opt,name=latitude,proto3" json:"latitude,omitempty"`
	Longitude     float32 `protobuf:"fixed32,8,opt,name=longitude,proto3" json:"longitude,omitempty"`
	Tv            int32   `protobuf:"varint,9,opt,name=tv,proto3" json:"tv,omitempty"`
	Elevator      int32   `protobuf:"varint,10,opt,name=elevator,proto3" json:"elevator,omitempty"`
	Internet      int32   `protobuf:"varint,11,opt,name=internet,proto3" json:"internet,omitempty"`
}

func (x *Request) Reset() {
	*x = Request{}
	if protoimpl.UnsafeEnabled {
		mi := &file_public_input_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Request) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Request) ProtoMessage() {}

func (x *Request) ProtoReflect() protoreflect.Message {
	mi := &file_public_input_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Request.ProtoReflect.Descriptor instead.
func (*Request) Descriptor() ([]byte, []int) {
	return file_public_input_proto_rawDescGZIP(), []int{0}
}

func (x *Request) GetRoomType() string {
	if x != nil {
		return x.RoomType
	}
	return ""
}

func (x *Request) GetBedrooms() int32 {
	if x != nil {
		return x.Bedrooms
	}
	return 0
}

func (x *Request) GetBathrooms() float32 {
	if x != nil {
		return x.Bathrooms
	}
	return 0
}

func (x *Request) GetAccommodates() int32 {
	if x != nil {
		return x.Accommodates
	}
	return 0
}

func (x *Request) GetBeds() int32 {
	if x != nil {
		return x.Beds
	}
	return 0
}

func (x *Request) GetNeighbourhood() string {
	if x != nil {
		return x.Neighbourhood
	}
	return ""
}

func (x *Request) GetLatitude() float32 {
	if x != nil {
		return x.Latitude
	}
	return 0
}

func (x *Request) GetLongitude() float32 {
	if x != nil {
		return x.Longitude
	}
	return 0
}

func (x *Request) GetTv() int32 {
	if x != nil {
		return x.Tv
	}
	return 0
}

func (x *Request) GetElevator() int32 {
	if x != nil {
		return x.Elevator
	}
	return 0
}

func (x *Request) GetInternet() int32 {
	if x != nil {
		return x.Internet
	}
	return 0
}

type Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Success     bool   `protobuf:"varint,1,opt,name=success,proto3" json:"success,omitempty"`
	Message     string `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
	MarketPrice string `protobuf:"bytes,3,opt,name=market_price,json=marketPrice,proto3" json:"market_price,omitempty"`
	Category    string `protobuf:"bytes,4,opt,name=category,proto3" json:"category,omitempty"`
}

func (x *Response) Reset() {
	*x = Response{}
	if protoimpl.UnsafeEnabled {
		mi := &file_public_input_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Response) ProtoMessage() {}

func (x *Response) ProtoReflect() protoreflect.Message {
	mi := &file_public_input_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Response.ProtoReflect.Descriptor instead.
func (*Response) Descriptor() ([]byte, []int) {
	return file_public_input_proto_rawDescGZIP(), []int{1}
}

func (x *Response) GetSuccess() bool {
	if x != nil {
		return x.Success
	}
	return false
}

func (x *Response) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

func (x *Response) GetMarketPrice() string {
	if x != nil {
		return x.MarketPrice
	}
	return ""
}

func (x *Response) GetCategory() string {
	if x != nil {
		return x.Category
	}
	return ""
}

type SaveMetricRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PredictedCategory string `protobuf:"bytes,1,opt,name=predicted_category,json=predictedCategory,proto3" json:"predicted_category,omitempty"`
	RealCategory      string `protobuf:"bytes,2,opt,name=real_category,json=realCategory,proto3" json:"real_category,omitempty"`
	Date              int64  `protobuf:"varint,3,opt,name=date,proto3" json:"date,omitempty"`
}

func (x *SaveMetricRequest) Reset() {
	*x = SaveMetricRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_public_input_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SaveMetricRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SaveMetricRequest) ProtoMessage() {}

func (x *SaveMetricRequest) ProtoReflect() protoreflect.Message {
	mi := &file_public_input_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SaveMetricRequest.ProtoReflect.Descriptor instead.
func (*SaveMetricRequest) Descriptor() ([]byte, []int) {
	return file_public_input_proto_rawDescGZIP(), []int{2}
}

func (x *SaveMetricRequest) GetPredictedCategory() string {
	if x != nil {
		return x.PredictedCategory
	}
	return ""
}

func (x *SaveMetricRequest) GetRealCategory() string {
	if x != nil {
		return x.RealCategory
	}
	return ""
}

func (x *SaveMetricRequest) GetDate() int64 {
	if x != nil {
		return x.Date
	}
	return 0
}

type SaveMetricResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Success bool   `protobuf:"varint,1,opt,name=success,proto3" json:"success,omitempty"`
	Message string `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
}

func (x *SaveMetricResponse) Reset() {
	*x = SaveMetricResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_public_input_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SaveMetricResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SaveMetricResponse) ProtoMessage() {}

func (x *SaveMetricResponse) ProtoReflect() protoreflect.Message {
	mi := &file_public_input_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SaveMetricResponse.ProtoReflect.Descriptor instead.
func (*SaveMetricResponse) Descriptor() ([]byte, []int) {
	return file_public_input_proto_rawDescGZIP(), []int{3}
}

func (x *SaveMetricResponse) GetSuccess() bool {
	if x != nil {
		return x.Success
	}
	return false
}

func (x *SaveMetricResponse) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

var File_public_input_proto protoreflect.FileDescriptor

var file_public_input_proto_rawDesc = []byte{
	0x0a, 0x12, 0x70, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x5f, 0x69, 0x6e, 0x70, 0x75, 0x74, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x0a, 0x65, 0x6e, 0x74, 0x72, 0x79, 0x70, 0x6f, 0x69, 0x6e, 0x74,
	0x22, 0xc0, 0x02, 0x0a, 0x07, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1b, 0x0a, 0x09,
	0x72, 0x6f, 0x6f, 0x6d, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x08, 0x72, 0x6f, 0x6f, 0x6d, 0x54, 0x79, 0x70, 0x65, 0x12, 0x1a, 0x0a, 0x08, 0x62, 0x65, 0x64,
	0x72, 0x6f, 0x6f, 0x6d, 0x73, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x08, 0x62, 0x65, 0x64,
	0x72, 0x6f, 0x6f, 0x6d, 0x73, 0x12, 0x1c, 0x0a, 0x09, 0x62, 0x61, 0x74, 0x68, 0x72, 0x6f, 0x6f,
	0x6d, 0x73, 0x18, 0x03, 0x20, 0x01, 0x28, 0x02, 0x52, 0x09, 0x62, 0x61, 0x74, 0x68, 0x72, 0x6f,
	0x6f, 0x6d, 0x73, 0x12, 0x22, 0x0a, 0x0c, 0x61, 0x63, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x64, 0x61,
	0x74, 0x65, 0x73, 0x18, 0x04, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0c, 0x61, 0x63, 0x63, 0x6f, 0x6d,
	0x6d, 0x6f, 0x64, 0x61, 0x74, 0x65, 0x73, 0x12, 0x12, 0x0a, 0x04, 0x62, 0x65, 0x64, 0x73, 0x18,
	0x05, 0x20, 0x01, 0x28, 0x05, 0x52, 0x04, 0x62, 0x65, 0x64, 0x73, 0x12, 0x24, 0x0a, 0x0d, 0x6e,
	0x65, 0x69, 0x67, 0x68, 0x62, 0x6f, 0x75, 0x72, 0x68, 0x6f, 0x6f, 0x64, 0x18, 0x06, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x0d, 0x6e, 0x65, 0x69, 0x67, 0x68, 0x62, 0x6f, 0x75, 0x72, 0x68, 0x6f, 0x6f,
	0x64, 0x12, 0x1a, 0x0a, 0x08, 0x6c, 0x61, 0x74, 0x69, 0x74, 0x75, 0x64, 0x65, 0x18, 0x07, 0x20,
	0x01, 0x28, 0x02, 0x52, 0x08, 0x6c, 0x61, 0x74, 0x69, 0x74, 0x75, 0x64, 0x65, 0x12, 0x1c, 0x0a,
	0x09, 0x6c, 0x6f, 0x6e, 0x67, 0x69, 0x74, 0x75, 0x64, 0x65, 0x18, 0x08, 0x20, 0x01, 0x28, 0x02,
	0x52, 0x09, 0x6c, 0x6f, 0x6e, 0x67, 0x69, 0x74, 0x75, 0x64, 0x65, 0x12, 0x0e, 0x0a, 0x02, 0x74,
	0x76, 0x18, 0x09, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x74, 0x76, 0x12, 0x1a, 0x0a, 0x08, 0x65,
	0x6c, 0x65, 0x76, 0x61, 0x74, 0x6f, 0x72, 0x18, 0x0a, 0x20, 0x01, 0x28, 0x05, 0x52, 0x08, 0x65,
	0x6c, 0x65, 0x76, 0x61, 0x74, 0x6f, 0x72, 0x12, 0x1a, 0x0a, 0x08, 0x69, 0x6e, 0x74, 0x65, 0x72,
	0x6e, 0x65, 0x74, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x05, 0x52, 0x08, 0x69, 0x6e, 0x74, 0x65, 0x72,
	0x6e, 0x65, 0x74, 0x22, 0x7d, 0x0a, 0x08, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12,
	0x18, 0x0a, 0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x08,
	0x52, 0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x12, 0x18, 0x0a, 0x07, 0x6d, 0x65, 0x73,
	0x73, 0x61, 0x67, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73,
	0x61, 0x67, 0x65, 0x12, 0x21, 0x0a, 0x0c, 0x6d, 0x61, 0x72, 0x6b, 0x65, 0x74, 0x5f, 0x70, 0x72,
	0x69, 0x63, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x6d, 0x61, 0x72, 0x6b, 0x65,
	0x74, 0x50, 0x72, 0x69, 0x63, 0x65, 0x12, 0x1a, 0x0a, 0x08, 0x63, 0x61, 0x74, 0x65, 0x67, 0x6f,
	0x72, 0x79, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x63, 0x61, 0x74, 0x65, 0x67, 0x6f,
	0x72, 0x79, 0x22, 0x7b, 0x0a, 0x11, 0x53, 0x61, 0x76, 0x65, 0x4d, 0x65, 0x74, 0x72, 0x69, 0x63,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x2d, 0x0a, 0x12, 0x70, 0x72, 0x65, 0x64, 0x69,
	0x63, 0x74, 0x65, 0x64, 0x5f, 0x63, 0x61, 0x74, 0x65, 0x67, 0x6f, 0x72, 0x79, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x11, 0x70, 0x72, 0x65, 0x64, 0x69, 0x63, 0x74, 0x65, 0x64, 0x43, 0x61,
	0x74, 0x65, 0x67, 0x6f, 0x72, 0x79, 0x12, 0x23, 0x0a, 0x0d, 0x72, 0x65, 0x61, 0x6c, 0x5f, 0x63,
	0x61, 0x74, 0x65, 0x67, 0x6f, 0x72, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x72,
	0x65, 0x61, 0x6c, 0x43, 0x61, 0x74, 0x65, 0x67, 0x6f, 0x72, 0x79, 0x12, 0x12, 0x0a, 0x04, 0x64,
	0x61, 0x74, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x03, 0x52, 0x04, 0x64, 0x61, 0x74, 0x65, 0x22,
	0x48, 0x0a, 0x12, 0x53, 0x61, 0x76, 0x65, 0x4d, 0x65, 0x74, 0x72, 0x69, 0x63, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x18, 0x0a, 0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x08, 0x52, 0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x12,
	0x18, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x32, 0xa4, 0x01, 0x0a, 0x0a, 0x45, 0x6e,
	0x74, 0x72, 0x79, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x12, 0x3d, 0x0a, 0x0e, 0x4d, 0x61, 0x6b, 0x65,
	0x50, 0x72, 0x65, 0x64, 0x69, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x13, 0x2e, 0x65, 0x6e, 0x74,
	0x72, 0x79, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x14, 0x2e, 0x65, 0x6e, 0x74, 0x72, 0x79, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x2e, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x12, 0x57, 0x0a, 0x14, 0x53, 0x61, 0x76, 0x65, 0x50,
	0x72, 0x65, 0x64, 0x69, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x4d, 0x65, 0x74, 0x72, 0x69, 0x63, 0x12,
	0x1d, 0x2e, 0x65, 0x6e, 0x74, 0x72, 0x79, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x2e, 0x53, 0x61, 0x76,
	0x65, 0x4d, 0x65, 0x74, 0x72, 0x69, 0x63, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1e,
	0x2e, 0x65, 0x6e, 0x74, 0x72, 0x79, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x2e, 0x53, 0x61, 0x76, 0x65,
	0x4d, 0x65, 0x74, 0x72, 0x69, 0x63, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00,
	0x42, 0x06, 0x5a, 0x04, 0x6d, 0x61, 0x69, 0x6e, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_public_input_proto_rawDescOnce sync.Once
	file_public_input_proto_rawDescData = file_public_input_proto_rawDesc
)

func file_public_input_proto_rawDescGZIP() []byte {
	file_public_input_proto_rawDescOnce.Do(func() {
		file_public_input_proto_rawDescData = protoimpl.X.CompressGZIP(file_public_input_proto_rawDescData)
	})
	return file_public_input_proto_rawDescData
}

var file_public_input_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_public_input_proto_goTypes = []interface{}{
	(*Request)(nil),            // 0: entrypoint.Request
	(*Response)(nil),           // 1: entrypoint.Response
	(*SaveMetricRequest)(nil),  // 2: entrypoint.SaveMetricRequest
	(*SaveMetricResponse)(nil), // 3: entrypoint.SaveMetricResponse
}
var file_public_input_proto_depIdxs = []int32{
	0, // 0: entrypoint.Entrypoint.MakePrediction:input_type -> entrypoint.Request
	2, // 1: entrypoint.Entrypoint.SavePredictionMetric:input_type -> entrypoint.SaveMetricRequest
	1, // 2: entrypoint.Entrypoint.MakePrediction:output_type -> entrypoint.Response
	3, // 3: entrypoint.Entrypoint.SavePredictionMetric:output_type -> entrypoint.SaveMetricResponse
	2, // [2:4] is the sub-list for method output_type
	0, // [0:2] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_public_input_proto_init() }
func file_public_input_proto_init() {
	if File_public_input_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_public_input_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Request); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_public_input_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Response); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_public_input_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SaveMetricRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_public_input_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SaveMetricResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_public_input_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_public_input_proto_goTypes,
		DependencyIndexes: file_public_input_proto_depIdxs,
		MessageInfos:      file_public_input_proto_msgTypes,
	}.Build()
	File_public_input_proto = out.File
	file_public_input_proto_rawDesc = nil
	file_public_input_proto_goTypes = nil
	file_public_input_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// EntrypointClient is the client API for Entrypoint service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type EntrypointClient interface {
	MakePrediction(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error)
	SavePredictionMetric(ctx context.Context, in *SaveMetricRequest, opts ...grpc.CallOption) (*SaveMetricResponse, error)
}

type entrypointClient struct {
	cc grpc.ClientConnInterface
}

func NewEntrypointClient(cc grpc.ClientConnInterface) EntrypointClient {
	return &entrypointClient{cc}
}

func (c *entrypointClient) MakePrediction(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error) {
	out := new(Response)
	err := c.cc.Invoke(ctx, "/entrypoint.Entrypoint/MakePrediction", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *entrypointClient) SavePredictionMetric(ctx context.Context, in *SaveMetricRequest, opts ...grpc.CallOption) (*SaveMetricResponse, error) {
	out := new(SaveMetricResponse)
	err := c.cc.Invoke(ctx, "/entrypoint.Entrypoint/SavePredictionMetric", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EntrypointServer is the server API for Entrypoint service.
type EntrypointServer interface {
	MakePrediction(context.Context, *Request) (*Response, error)
	SavePredictionMetric(context.Context, *SaveMetricRequest) (*SaveMetricResponse, error)
}

// UnimplementedEntrypointServer can be embedded to have forward compatible implementations.
type UnimplementedEntrypointServer struct {
}

func (*UnimplementedEntrypointServer) MakePrediction(context.Context, *Request) (*Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method MakePrediction not implemented")
}
func (*UnimplementedEntrypointServer) SavePredictionMetric(context.Context, *SaveMetricRequest) (*SaveMetricResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SavePredictionMetric not implemented")
}

func RegisterEntrypointServer(s *grpc.Server, srv EntrypointServer) {
	s.RegisterService(&_Entrypoint_serviceDesc, srv)
}

func _Entrypoint_MakePrediction_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EntrypointServer).MakePrediction(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/entrypoint.Entrypoint/MakePrediction",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EntrypointServer).MakePrediction(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _Entrypoint_SavePredictionMetric_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SaveMetricRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EntrypointServer).SavePredictionMetric(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/entrypoint.Entrypoint/SavePredictionMetric",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EntrypointServer).SavePredictionMetric(ctx, req.(*SaveMetricRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _Entrypoint_serviceDesc = grpc.ServiceDesc{
	ServiceName: "entrypoint.Entrypoint",
	HandlerType: (*EntrypointServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "MakePrediction",
			Handler:    _Entrypoint_MakePrediction_Handler,
		},
		{
			MethodName: "SavePredictionMetric",
			Handler:    _Entrypoint_SavePredictionMetric_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "public_input.proto",
}
