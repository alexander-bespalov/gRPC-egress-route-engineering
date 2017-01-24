# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: registration_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='registration_service.proto',
  package='registration',
  syntax='proto3',
  serialized_pb=_b('\n\x1aregistration_service.proto\x12\x0cregistration\"\x8d\x01\n\x0fRegisterRequest\x12\x14\n\njson_input\x18\x01 \x01(\tH\x00\x12\x14\n\nfile_input\x18\x02 \x01(\tH\x00\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x13\n\x0bregister_id\x18\x04 \x01(\t\x12\x1b\n\x13skip_authentication\x18\x05 \x01(\x08\x42\x0c\n\ninput_type\".\n\rRegisterReply\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t2[\n\x08Register\x12O\n\x0fRegisterService\x12\x1d.registration.RegisterRequest\x1a\x1b.registration.RegisterReply\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='registration.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_input', full_name='registration.RegisterRequest.json_input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_input', full_name='registration.RegisterRequest.file_input', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='registration.RegisterRequest.target', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='register_id', full_name='registration.RegisterRequest.register_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skip_authentication', full_name='registration.RegisterRequest.skip_authentication', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='input_type', full_name='registration.RegisterRequest.input_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=45,
  serialized_end=186,
)


_REGISTERREPLY = _descriptor.Descriptor(
  name='RegisterReply',
  full_name='registration.RegisterReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='registration.RegisterReply.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='registration.RegisterReply.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=234,
)

_REGISTERREQUEST.oneofs_by_name['input_type'].fields.append(
  _REGISTERREQUEST.fields_by_name['json_input'])
_REGISTERREQUEST.fields_by_name['json_input'].containing_oneof = _REGISTERREQUEST.oneofs_by_name['input_type']
_REGISTERREQUEST.oneofs_by_name['input_type'].fields.append(
  _REGISTERREQUEST.fields_by_name['file_input'])
_REGISTERREQUEST.fields_by_name['file_input'].containing_oneof = _REGISTERREQUEST.oneofs_by_name['input_type']
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterReply'] = _REGISTERREPLY

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERREQUEST,
  __module__ = 'registration_service_pb2'
  # @@protoc_insertion_point(class_scope:registration.RegisterRequest)
  ))
_sym_db.RegisterMessage(RegisterRequest)

RegisterReply = _reflection.GeneratedProtocolMessageType('RegisterReply', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERREPLY,
  __module__ = 'registration_service_pb2'
  # @@protoc_insertion_point(class_scope:registration.RegisterReply)
  ))
_sym_db.RegisterMessage(RegisterReply)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class RegisterStub(object):
    """The service Registration definition.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.RegisterService = channel.unary_unary(
          '/registration.Register/RegisterService',
          request_serializer=RegisterRequest.SerializeToString,
          response_deserializer=RegisterReply.FromString,
          )


  class RegisterServicer(object):
    """The service Registration definition.
    """

    def RegisterService(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_RegisterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'RegisterService': grpc.unary_unary_rpc_method_handler(
            servicer.RegisterService,
            request_deserializer=RegisterRequest.FromString,
            response_serializer=RegisterReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'registration.Register', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaRegisterServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The service Registration definition.
    """
    def RegisterService(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaRegisterStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The service Registration definition.
    """
    def RegisterService(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    RegisterService.future = None


  def beta_create_Register_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('registration.Register', 'RegisterService'): RegisterRequest.FromString,
    }
    response_serializers = {
      ('registration.Register', 'RegisterService'): RegisterReply.SerializeToString,
    }
    method_implementations = {
      ('registration.Register', 'RegisterService'): face_utilities.unary_unary_inline(servicer.RegisterService),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Register_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('registration.Register', 'RegisterService'): RegisterRequest.SerializeToString,
    }
    response_deserializers = {
      ('registration.Register', 'RegisterService'): RegisterReply.FromString,
    }
    cardinalities = {
      'RegisterService': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'registration.Register', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
