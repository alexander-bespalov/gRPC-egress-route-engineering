import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import registration_service_pb2 as registration__service__pb2
import registration_service_pb2 as registration__service__pb2


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
        request_serializer=registration__service__pb2.RegisterRequest.SerializeToString,
        response_deserializer=registration__service__pb2.RegisterReply.FromString,
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
          request_deserializer=registration__service__pb2.RegisterRequest.FromString,
          response_serializer=registration__service__pb2.RegisterReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'registration.Register', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
