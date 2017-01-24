import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2
import firewall_service_pb2 as firewall__service__pb2


class AclServiceStub(object):
  """
  ACL Service APIs defines a set of simple RPCs to operate upon the various
  components, viz. 
  - ACL
  - ACE
  - Policer
  - Attachment Points
  - Statistics.

  Each of RPCs are named by concatenating the corresponding Acl object and the operation 
  to be performed. This give a easy to understand semantics to the RPCs.


  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AccessListAdd = channel.unary_unary(
        '/acl.AclService/AccessListAdd',
        request_serializer=firewall__service__pb2.AccessList.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListDelete = channel.unary_unary(
        '/acl.AclService/AccessListDelete',
        request_serializer=firewall__service__pb2.AccessList.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListChange = channel.unary_unary(
        '/acl.AclService/AccessListChange',
        request_serializer=firewall__service__pb2.AccessList.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListBindAdd = channel.unary_unary(
        '/acl.AclService/AccessListBindAdd',
        request_serializer=firewall__service__pb2.AccessListObjBind.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListBindDelete = channel.unary_unary(
        '/acl.AclService/AccessListBindDelete',
        request_serializer=firewall__service__pb2.AccessListObjBind.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListPolicerAdd = channel.unary_unary(
        '/acl.AclService/AccessListPolicerAdd',
        request_serializer=firewall__service__pb2.AccessListPolicer.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListPolicerReplace = channel.unary_unary(
        '/acl.AclService/AccessListPolicerReplace',
        request_serializer=firewall__service__pb2.AccessListPolicer.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListPolicerDelete = channel.unary_unary(
        '/acl.AclService/AccessListPolicerDelete',
        request_serializer=firewall__service__pb2.AccessListPolicer.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListPileupStart = channel.unary_unary(
        '/acl.AclService/AccessListPileupStart',
        request_serializer=firewall__service__pb2.AccessListVoid.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListPileupEnd = channel.unary_unary(
        '/acl.AclService/AccessListPileupEnd',
        request_serializer=firewall__service__pb2.AccessListVoid.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListCounterGet = channel.unary_unary(
        '/acl.AclService/AccessListCounterGet',
        request_serializer=firewall__service__pb2.AccessListCounter.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListCounterVal.FromString,
        )
    self.AccessListPolicerCounterGet = channel.unary_unary(
        '/acl.AclService/AccessListPolicerCounterGet',
        request_serializer=firewall__service__pb2.AccessListCounter.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListCounterVal.FromString,
        )
    self.AccessListCounterClear = channel.unary_unary(
        '/acl.AclService/AccessListCounterClear',
        request_serializer=firewall__service__pb2.AccessListCounter.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListReturnStatus.FromString,
        )
    self.AccessListCounterBulkGet = channel.unary_stream(
        '/acl.AclService/AccessListCounterBulkGet',
        request_serializer=firewall__service__pb2.AccessListCounterBulk.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListCounterVal.FromString,
        )
    self.AccessListPolicerCounterBulkGet = channel.unary_stream(
        '/acl.AclService/AccessListPolicerCounterBulkGet',
        request_serializer=firewall__service__pb2.AccessListCounterBulk.SerializeToString,
        response_deserializer=firewall__service__pb2.AccessListCounterVal.FromString,
        )


class AclServiceServicer(object):
  """
  ACL Service APIs defines a set of simple RPCs to operate upon the various
  components, viz. 
  - ACL
  - ACE
  - Policer
  - Attachment Points
  - Statistics.

  Each of RPCs are named by concatenating the corresponding Acl object and the operation 
  to be performed. This give a easy to understand semantics to the RPCs.


  """

  def AccessListAdd(self, request, context):
    """Adds an ACL and returns the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListDelete(self, request, context):
    """Delete an ACL from the system and return the result.
    For successful delete to happen, the ACL should not be bound to any object.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListChange(self, request, context):
    """Changes an ACL based on the list of ACL entries provided, and returns the result.
    It is advisable to use this API to for small incremental changes. For wholesale 
    changes, it is recommended to use the 'Replace' version of the API.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListBindAdd(self, request, context):
    """Add a binding of an ACL with a bind object and return the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListBindDelete(self, request, context):
    """Deletes a binding of an ACL with a bind object and return the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListPolicerAdd(self, request, context):
    """Adds a policer and returns the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListPolicerReplace(self, request, context):
    """Changes a policer and returns the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListPolicerDelete(self, request, context):
    """Deletes a policer and returns the result.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListPileupStart(self, request, context):
    """Following are optimized command to let the server know to <br>
    accumulate the Access List Entries and configure on when AccessListPileupEnd is received. <br>
    For every AccessList RPC invocation, the entire ACL is applied to the system <br>
    For application which wants to do batching for better performance, the AccessListPileupStart <br>
    and AccessListPileupEnd will help achive that.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListPileupEnd(self, request, context):
    """Following are optimized command to let the server know to <br>
    accumulate the ace_list and configure on when AccessListPileupEnd is received. <br>
    For every AccessList RPC invocation, the entire ACL is applied to the system <br>
    For application which wants to do batching for better performance, the AccessListPileupStart <br>
    and AccessListPileupEnd will help achive that.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListCounterGet(self, request, context):
    """Few points to note with this API. 
    The call is going to be blocking for worst case of 10 seconds which is non configurable.
    The counter name is expected to be fully resolved. For eg. for term specific policer counter
    it is expected to be passed to full counter name.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListPolicerCounterGet(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListCounterClear(self, request, context):
    """Clears a particular counter whose fully qualified name is provided,  associated with an ACL.
    Few points to note with this API. Currently only 1 counter get is supported.
    The counter name is expected to be fully resolved. For eg. for term specific policer counter
    it is expected to be passed to full counter name.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListCounterBulkGet(self, request, context):
    """Get all the counters associated with an ACL.
    Each call to this API will return 10 counters from the starting_index specified in AccessListCounterBulk message.
    The client is expected to run this API in loop which should stop in either one of the following condition:
    a. The targeted number of counters are retrieved.
    b. An error is returned.
    c. The API returns less than 10 counters.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccessListPolicerCounterBulkGet(self, request, context):
    """Get all the policer counters associated with an ACL.
    Each call to this API will return 10 counters from the starting_index specified in AccessListCounterBulk message.
    The client is expected to run this API in loop which should stop in either one of the following condition:
    a. The targeted number of counters are retrieved.
    b. An error is returned.
    c. The API returns less than 10 counters.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AclServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AccessListAdd': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListAdd,
          request_deserializer=firewall__service__pb2.AccessList.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListDelete': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListDelete,
          request_deserializer=firewall__service__pb2.AccessList.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListChange': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListChange,
          request_deserializer=firewall__service__pb2.AccessList.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListBindAdd': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListBindAdd,
          request_deserializer=firewall__service__pb2.AccessListObjBind.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListBindDelete': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListBindDelete,
          request_deserializer=firewall__service__pb2.AccessListObjBind.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListPolicerAdd': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListPolicerAdd,
          request_deserializer=firewall__service__pb2.AccessListPolicer.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListPolicerReplace': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListPolicerReplace,
          request_deserializer=firewall__service__pb2.AccessListPolicer.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListPolicerDelete': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListPolicerDelete,
          request_deserializer=firewall__service__pb2.AccessListPolicer.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListPileupStart': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListPileupStart,
          request_deserializer=firewall__service__pb2.AccessListVoid.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListPileupEnd': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListPileupEnd,
          request_deserializer=firewall__service__pb2.AccessListVoid.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListCounterGet': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListCounterGet,
          request_deserializer=firewall__service__pb2.AccessListCounter.FromString,
          response_serializer=firewall__service__pb2.AccessListCounterVal.SerializeToString,
      ),
      'AccessListPolicerCounterGet': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListPolicerCounterGet,
          request_deserializer=firewall__service__pb2.AccessListCounter.FromString,
          response_serializer=firewall__service__pb2.AccessListCounterVal.SerializeToString,
      ),
      'AccessListCounterClear': grpc.unary_unary_rpc_method_handler(
          servicer.AccessListCounterClear,
          request_deserializer=firewall__service__pb2.AccessListCounter.FromString,
          response_serializer=firewall__service__pb2.AccessListReturnStatus.SerializeToString,
      ),
      'AccessListCounterBulkGet': grpc.unary_stream_rpc_method_handler(
          servicer.AccessListCounterBulkGet,
          request_deserializer=firewall__service__pb2.AccessListCounterBulk.FromString,
          response_serializer=firewall__service__pb2.AccessListCounterVal.SerializeToString,
      ),
      'AccessListPolicerCounterBulkGet': grpc.unary_stream_rpc_method_handler(
          servicer.AccessListPolicerCounterBulkGet,
          request_deserializer=firewall__service__pb2.AccessListCounterBulk.FromString,
          response_serializer=firewall__service__pb2.AccessListCounterVal.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'acl.AclService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
