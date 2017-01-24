import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import prpd_service_pb2 as prpd__service__pb2
import prpd_service_pb2 as prpd__service__pb2
import prpd_service_pb2 as prpd__service__pb2
import prpd_service_pb2 as prpd__service__pb2
import prpd_service_pb2 as prpd__service__pb2
import prpd_service_pb2 as prpd__service__pb2


class BaseStub(object):
  """*
  ---------------------------------------------------------------
  APIs for the RPD Infra Operations
  ---------------------------------------------------------------
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RoutePurgeTimeConfig = channel.unary_unary(
        '/routing.Base/RoutePurgeTimeConfig',
        request_serializer=prpd__service__pb2.RtPurgeConfigRequest.SerializeToString,
        response_deserializer=prpd__service__pb2.RtOperReply.FromString,
        )
    self.RoutePurgeTimeUnconfig = channel.unary_unary(
        '/routing.Base/RoutePurgeTimeUnconfig',
        request_serializer=prpd__service__pb2.RtEmptyRequest.SerializeToString,
        response_deserializer=prpd__service__pb2.RtOperReply.FromString,
        )
    self.RoutePurgeTimeGet = channel.unary_unary(
        '/routing.Base/RoutePurgeTimeGet',
        request_serializer=prpd__service__pb2.RtEmptyRequest.SerializeToString,
        response_deserializer=prpd__service__pb2.RtPurgeTimeGetReply.FromString,
        )


class BaseServicer(object):
  """*
  ---------------------------------------------------------------
  APIs for the RPD Infra Operations
  ---------------------------------------------------------------
  """

  def RoutePurgeTimeConfig(self, request, context):
    """*
    ---------------------------------------------------------------
    Service to configure purge timer for the client
    ---------------------------------------------------------------

    Configure a purge timer for the client so that server side will retain
    the client installed routes till this time after client disconnects and
    provide sufficient time for the client to reconnect if possible.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RoutePurgeTimeUnconfig(self, request, context):
    """*
    ---------------------------------------------------------------
    Service to unconfigure purge timer for the client
    ---------------------------------------------------------------

    Unconfigure a previously configured purge timer for the client.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RoutePurgeTimeGet(self, request, context):
    """*
    ---------------------------------------------------------------
    Service to retrive the purge timer for the client
    ---------------------------------------------------------------

    Get a purge timer for the client
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BaseServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RoutePurgeTimeConfig': grpc.unary_unary_rpc_method_handler(
          servicer.RoutePurgeTimeConfig,
          request_deserializer=prpd__service__pb2.RtPurgeConfigRequest.FromString,
          response_serializer=prpd__service__pb2.RtOperReply.SerializeToString,
      ),
      'RoutePurgeTimeUnconfig': grpc.unary_unary_rpc_method_handler(
          servicer.RoutePurgeTimeUnconfig,
          request_deserializer=prpd__service__pb2.RtEmptyRequest.FromString,
          response_serializer=prpd__service__pb2.RtOperReply.SerializeToString,
      ),
      'RoutePurgeTimeGet': grpc.unary_unary_rpc_method_handler(
          servicer.RoutePurgeTimeGet,
          request_deserializer=prpd__service__pb2.RtEmptyRequest.FromString,
          response_serializer=prpd__service__pb2.RtPurgeTimeGetReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'routing.Base', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
