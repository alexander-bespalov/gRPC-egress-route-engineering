import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2
import openconfig_service_pb2 as openconfig__service__pb2


class OpenconfigRpcApiStub(object):
  """
  MGD Service Definitions
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDataEncodings = channel.unary_unary(
        '/openconfig.OpenconfigRpcApi/GetDataEncodings',
        request_serializer=openconfig__service__pb2.GetDataEncodingsRequest.SerializeToString,
        response_deserializer=openconfig__service__pb2.GetDataEncodingsResponse.FromString,
        )
    self.SetDataEncoding = channel.unary_unary(
        '/openconfig.OpenconfigRpcApi/SetDataEncoding',
        request_serializer=openconfig__service__pb2.SetDataEncodingRequest.SerializeToString,
        response_deserializer=openconfig__service__pb2.SetDataEncodingResponse.FromString,
        )
    self.GetModels = channel.unary_unary(
        '/openconfig.OpenconfigRpcApi/GetModels',
        request_serializer=openconfig__service__pb2.GetModelsRequest.SerializeToString,
        response_deserializer=openconfig__service__pb2.GetModelsResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/openconfig.OpenconfigRpcApi/Get',
        request_serializer=openconfig__service__pb2.GetRequest.SerializeToString,
        response_deserializer=openconfig__service__pb2.GetResponse.FromString,
        )
    self.Set = channel.unary_unary(
        '/openconfig.OpenconfigRpcApi/Set',
        request_serializer=openconfig__service__pb2.SetRequest.SerializeToString,
        response_deserializer=openconfig__service__pb2.SetResponse.FromString,
        )


class OpenconfigRpcApiServicer(object):
  """
  MGD Service Definitions
  """

  def GetDataEncodings(self, request, context):
    """
    Return the set of data encodings supported by the device for
    configuration and telemetry data modeled in YANG
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDataEncoding(self, request, context):
    """
    Select and set one of the data encodings returned by
    getDataEncodings.  This RPC sets the global encoding
    serialization for all data exchanged with the target
    device. The global data encoding may be optionally overriden
    by setting the encoding for an individual RPC if supported by the target
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModels(self, request, context):
    """
    Returns a repeated structure of supported data models
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """
    Requests data from the network device.  The get RPC
    request should include a subcommand to indicate the type of
    data desired by the requestor.  Supported types of data
    include: configuration data (config: true nodes in the schema)
    operational state data (config: false nodes)
    derived operational state only (config: false nodes that
    represent derived operational state, exluding config: false
    nodes that represent applied configuration.
    all data (config: true and config: false nodes)
    A get RPC can contain multiple requests for data.  Each
    request includes a path specifying a subtree in the data
    model, and a command to indicate which type of data should be returned
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Set(self, request, context):
    """
    Modify configuration on the target device. The set
    RPC accepts a combination of commands, each with an
    associated path specification to indicate which data should be modified.
    The commands in a set request should be fully validated and accepted by
    the device before a response is returned.  The
    application of the configuration commands may or may not be
    complete when the command returns.  The NMS is expected to be
    able to track the application of the configuration using the
    operational state data in the telemetry stream, or by
    retrieving the state data using an RPC
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OpenconfigRpcApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDataEncodings': grpc.unary_unary_rpc_method_handler(
          servicer.GetDataEncodings,
          request_deserializer=openconfig__service__pb2.GetDataEncodingsRequest.FromString,
          response_serializer=openconfig__service__pb2.GetDataEncodingsResponse.SerializeToString,
      ),
      'SetDataEncoding': grpc.unary_unary_rpc_method_handler(
          servicer.SetDataEncoding,
          request_deserializer=openconfig__service__pb2.SetDataEncodingRequest.FromString,
          response_serializer=openconfig__service__pb2.SetDataEncodingResponse.SerializeToString,
      ),
      'GetModels': grpc.unary_unary_rpc_method_handler(
          servicer.GetModels,
          request_deserializer=openconfig__service__pb2.GetModelsRequest.FromString,
          response_serializer=openconfig__service__pb2.GetModelsResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=openconfig__service__pb2.GetRequest.FromString,
          response_serializer=openconfig__service__pb2.GetResponse.SerializeToString,
      ),
      'Set': grpc.unary_unary_rpc_method_handler(
          servicer.Set,
          request_deserializer=openconfig__service__pb2.SetRequest.FromString,
          response_serializer=openconfig__service__pb2.SetResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'openconfig.OpenconfigRpcApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
