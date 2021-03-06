# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prpd_common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import jnx_addr_pb2 as jnx__addr__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='prpd_common.proto',
  package='routing',
  syntax='proto3',
  serialized_pb=_b('\n\x11prpd_common.proto\x12\x07routing\x1a\x0ejnx_addr.proto\"\x1e\n\x0eRouteTableName\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1a\n\x0cRouteTableId\x12\n\n\x02id\x18\x01 \x01(\r\"s\n\nRouteTable\x12\'\n\x06rtt_id\x18\x01 \x01(\x0b\x32\x15.routing.RouteTableIdH\x00\x12+\n\x08rtt_name\x18\x02 \x01(\x0b\x32\x17.routing.RouteTableNameH\x00\x42\x0f\n\rRtTableFormat\"5\n\x07RdType0\x12\x11\n\tas_number\x18\x01 \x01(\r\x12\x17\n\x0f\x61ssigned_number\x18\x02 \x01(\r\"J\n\x07RdType1\x12&\n\nip_address\x18\x01 \x01(\x0b\x32\x12.jnxBase.IpAddress\x12\x17\n\x0f\x61ssigned_number\x18\x02 \x01(\r\"5\n\x07RdType2\x12\x11\n\tas_number\x18\x01 \x01(\r\x12\x17\n\x0f\x61ssigned_number\x18\x02 \x01(\r\"\x83\x01\n\x12RouteDistinguisher\x12\x1f\n\x03rd0\x18\x01 \x01(\x0b\x32\x10.routing.RdType0H\x00\x12\x1f\n\x03rd1\x18\x02 \x01(\x0b\x32\x10.routing.RdType1H\x00\x12\x1f\n\x03rd2\x18\x03 \x01(\x0b\x32\x10.routing.RdType2H\x00\x42\n\n\x08RdFormat\"]\n\x0cL3vpnAddress\x12\'\n\x02rd\x18\x01 \x01(\x0b\x32\x1b.routing.RouteDistinguisher\x12$\n\x08vpn_addr\x18\x02 \x01(\x0b\x32\x12.jnxBase.IpAddress\"\xbc\x01\n\x0bRoutePrefix\x12\"\n\x04inet\x18\x01 \x01(\x0b\x32\x12.jnxBase.IpAddressH\x00\x12#\n\x05inet6\x18\x02 \x01(\x0b\x32\x12.jnxBase.IpAddressH\x00\x12(\n\x07inetvpn\x18\x03 \x01(\x0b\x32\x15.routing.L3vpnAddressH\x00\x12)\n\x08inet6vpn\x18\x04 \x01(\x0b\x32\x15.routing.L3vpnAddressH\x00\x42\x0f\n\rRoutePrefixAf*Y\n\nReturnCode\x12\x0f\n\x0bRET_SUCCESS\x10\x00\x12\x0f\n\x0bRET_FAILURE\x10\x01\x12\x11\n\rRET_NOT_FOUND\x10\x02\x12\x16\n\x12RET_INVALID_PARAMS\x10\x03*2\n\x10RouteTableFormat\x12\x10\n\x0cTABLE_STRING\x10\x00\x12\x0c\n\x08TABLE_ID\x10\x01*g\n\x0bRouteAfType\x12\x10\n\x0cRT_AF_UNSPEC\x10\x00\x12\x0e\n\nRT_AF_INET\x10\x01\x12\x0f\n\x0bRT_AF_INET6\x10\x02\x12\x11\n\rRT_AF_INETVPN\x10\x03\x12\x12\n\x0eRT_AF_INET6VPN\x10\x04\x62\x06proto3')
  ,
  dependencies=[jnx__addr__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_RETURNCODE = _descriptor.EnumDescriptor(
  name='ReturnCode',
  full_name='routing.ReturnCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RET_SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RET_FAILURE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RET_NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RET_INVALID_PARAMS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=829,
  serialized_end=918,
)
_sym_db.RegisterEnumDescriptor(_RETURNCODE)

ReturnCode = enum_type_wrapper.EnumTypeWrapper(_RETURNCODE)
_ROUTETABLEFORMAT = _descriptor.EnumDescriptor(
  name='RouteTableFormat',
  full_name='routing.RouteTableFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TABLE_STRING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TABLE_ID', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=920,
  serialized_end=970,
)
_sym_db.RegisterEnumDescriptor(_ROUTETABLEFORMAT)

RouteTableFormat = enum_type_wrapper.EnumTypeWrapper(_ROUTETABLEFORMAT)
_ROUTEAFTYPE = _descriptor.EnumDescriptor(
  name='RouteAfType',
  full_name='routing.RouteAfType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RT_AF_UNSPEC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RT_AF_INET', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RT_AF_INET6', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RT_AF_INETVPN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RT_AF_INET6VPN', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=972,
  serialized_end=1075,
)
_sym_db.RegisterEnumDescriptor(_ROUTEAFTYPE)

RouteAfType = enum_type_wrapper.EnumTypeWrapper(_ROUTEAFTYPE)
RET_SUCCESS = 0
RET_FAILURE = 1
RET_NOT_FOUND = 2
RET_INVALID_PARAMS = 3
TABLE_STRING = 0
TABLE_ID = 1
RT_AF_UNSPEC = 0
RT_AF_INET = 1
RT_AF_INET6 = 2
RT_AF_INETVPN = 3
RT_AF_INET6VPN = 4



_ROUTETABLENAME = _descriptor.Descriptor(
  name='RouteTableName',
  full_name='routing.RouteTableName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='routing.RouteTableName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=46,
  serialized_end=76,
)


_ROUTETABLEID = _descriptor.Descriptor(
  name='RouteTableId',
  full_name='routing.RouteTableId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='routing.RouteTableId.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=78,
  serialized_end=104,
)


_ROUTETABLE = _descriptor.Descriptor(
  name='RouteTable',
  full_name='routing.RouteTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rtt_id', full_name='routing.RouteTable.rtt_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtt_name', full_name='routing.RouteTable.rtt_name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='RtTableFormat', full_name='routing.RouteTable.RtTableFormat',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=106,
  serialized_end=221,
)


_RDTYPE0 = _descriptor.Descriptor(
  name='RdType0',
  full_name='routing.RdType0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='as_number', full_name='routing.RdType0.as_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assigned_number', full_name='routing.RdType0.assigned_number', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=223,
  serialized_end=276,
)


_RDTYPE1 = _descriptor.Descriptor(
  name='RdType1',
  full_name='routing.RdType1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='routing.RdType1.ip_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assigned_number', full_name='routing.RdType1.assigned_number', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=278,
  serialized_end=352,
)


_RDTYPE2 = _descriptor.Descriptor(
  name='RdType2',
  full_name='routing.RdType2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='as_number', full_name='routing.RdType2.as_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assigned_number', full_name='routing.RdType2.assigned_number', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=354,
  serialized_end=407,
)


_ROUTEDISTINGUISHER = _descriptor.Descriptor(
  name='RouteDistinguisher',
  full_name='routing.RouteDistinguisher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rd0', full_name='routing.RouteDistinguisher.rd0', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rd1', full_name='routing.RouteDistinguisher.rd1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rd2', full_name='routing.RouteDistinguisher.rd2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='RdFormat', full_name='routing.RouteDistinguisher.RdFormat',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=410,
  serialized_end=541,
)


_L3VPNADDRESS = _descriptor.Descriptor(
  name='L3vpnAddress',
  full_name='routing.L3vpnAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rd', full_name='routing.L3vpnAddress.rd', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vpn_addr', full_name='routing.L3vpnAddress.vpn_addr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=543,
  serialized_end=636,
)


_ROUTEPREFIX = _descriptor.Descriptor(
  name='RoutePrefix',
  full_name='routing.RoutePrefix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inet', full_name='routing.RoutePrefix.inet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inet6', full_name='routing.RoutePrefix.inet6', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inetvpn', full_name='routing.RoutePrefix.inetvpn', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inet6vpn', full_name='routing.RoutePrefix.inet6vpn', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='RoutePrefixAf', full_name='routing.RoutePrefix.RoutePrefixAf',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=639,
  serialized_end=827,
)

_ROUTETABLE.fields_by_name['rtt_id'].message_type = _ROUTETABLEID
_ROUTETABLE.fields_by_name['rtt_name'].message_type = _ROUTETABLENAME
_ROUTETABLE.oneofs_by_name['RtTableFormat'].fields.append(
  _ROUTETABLE.fields_by_name['rtt_id'])
_ROUTETABLE.fields_by_name['rtt_id'].containing_oneof = _ROUTETABLE.oneofs_by_name['RtTableFormat']
_ROUTETABLE.oneofs_by_name['RtTableFormat'].fields.append(
  _ROUTETABLE.fields_by_name['rtt_name'])
_ROUTETABLE.fields_by_name['rtt_name'].containing_oneof = _ROUTETABLE.oneofs_by_name['RtTableFormat']
_RDTYPE1.fields_by_name['ip_address'].message_type = jnx__addr__pb2._IPADDRESS
_ROUTEDISTINGUISHER.fields_by_name['rd0'].message_type = _RDTYPE0
_ROUTEDISTINGUISHER.fields_by_name['rd1'].message_type = _RDTYPE1
_ROUTEDISTINGUISHER.fields_by_name['rd2'].message_type = _RDTYPE2
_ROUTEDISTINGUISHER.oneofs_by_name['RdFormat'].fields.append(
  _ROUTEDISTINGUISHER.fields_by_name['rd0'])
_ROUTEDISTINGUISHER.fields_by_name['rd0'].containing_oneof = _ROUTEDISTINGUISHER.oneofs_by_name['RdFormat']
_ROUTEDISTINGUISHER.oneofs_by_name['RdFormat'].fields.append(
  _ROUTEDISTINGUISHER.fields_by_name['rd1'])
_ROUTEDISTINGUISHER.fields_by_name['rd1'].containing_oneof = _ROUTEDISTINGUISHER.oneofs_by_name['RdFormat']
_ROUTEDISTINGUISHER.oneofs_by_name['RdFormat'].fields.append(
  _ROUTEDISTINGUISHER.fields_by_name['rd2'])
_ROUTEDISTINGUISHER.fields_by_name['rd2'].containing_oneof = _ROUTEDISTINGUISHER.oneofs_by_name['RdFormat']
_L3VPNADDRESS.fields_by_name['rd'].message_type = _ROUTEDISTINGUISHER
_L3VPNADDRESS.fields_by_name['vpn_addr'].message_type = jnx__addr__pb2._IPADDRESS
_ROUTEPREFIX.fields_by_name['inet'].message_type = jnx__addr__pb2._IPADDRESS
_ROUTEPREFIX.fields_by_name['inet6'].message_type = jnx__addr__pb2._IPADDRESS
_ROUTEPREFIX.fields_by_name['inetvpn'].message_type = _L3VPNADDRESS
_ROUTEPREFIX.fields_by_name['inet6vpn'].message_type = _L3VPNADDRESS
_ROUTEPREFIX.oneofs_by_name['RoutePrefixAf'].fields.append(
  _ROUTEPREFIX.fields_by_name['inet'])
_ROUTEPREFIX.fields_by_name['inet'].containing_oneof = _ROUTEPREFIX.oneofs_by_name['RoutePrefixAf']
_ROUTEPREFIX.oneofs_by_name['RoutePrefixAf'].fields.append(
  _ROUTEPREFIX.fields_by_name['inet6'])
_ROUTEPREFIX.fields_by_name['inet6'].containing_oneof = _ROUTEPREFIX.oneofs_by_name['RoutePrefixAf']
_ROUTEPREFIX.oneofs_by_name['RoutePrefixAf'].fields.append(
  _ROUTEPREFIX.fields_by_name['inetvpn'])
_ROUTEPREFIX.fields_by_name['inetvpn'].containing_oneof = _ROUTEPREFIX.oneofs_by_name['RoutePrefixAf']
_ROUTEPREFIX.oneofs_by_name['RoutePrefixAf'].fields.append(
  _ROUTEPREFIX.fields_by_name['inet6vpn'])
_ROUTEPREFIX.fields_by_name['inet6vpn'].containing_oneof = _ROUTEPREFIX.oneofs_by_name['RoutePrefixAf']
DESCRIPTOR.message_types_by_name['RouteTableName'] = _ROUTETABLENAME
DESCRIPTOR.message_types_by_name['RouteTableId'] = _ROUTETABLEID
DESCRIPTOR.message_types_by_name['RouteTable'] = _ROUTETABLE
DESCRIPTOR.message_types_by_name['RdType0'] = _RDTYPE0
DESCRIPTOR.message_types_by_name['RdType1'] = _RDTYPE1
DESCRIPTOR.message_types_by_name['RdType2'] = _RDTYPE2
DESCRIPTOR.message_types_by_name['RouteDistinguisher'] = _ROUTEDISTINGUISHER
DESCRIPTOR.message_types_by_name['L3vpnAddress'] = _L3VPNADDRESS
DESCRIPTOR.message_types_by_name['RoutePrefix'] = _ROUTEPREFIX
DESCRIPTOR.enum_types_by_name['ReturnCode'] = _RETURNCODE
DESCRIPTOR.enum_types_by_name['RouteTableFormat'] = _ROUTETABLEFORMAT
DESCRIPTOR.enum_types_by_name['RouteAfType'] = _ROUTEAFTYPE

RouteTableName = _reflection.GeneratedProtocolMessageType('RouteTableName', (_message.Message,), dict(
  DESCRIPTOR = _ROUTETABLENAME,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.RouteTableName)
  ))
_sym_db.RegisterMessage(RouteTableName)

RouteTableId = _reflection.GeneratedProtocolMessageType('RouteTableId', (_message.Message,), dict(
  DESCRIPTOR = _ROUTETABLEID,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.RouteTableId)
  ))
_sym_db.RegisterMessage(RouteTableId)

RouteTable = _reflection.GeneratedProtocolMessageType('RouteTable', (_message.Message,), dict(
  DESCRIPTOR = _ROUTETABLE,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.RouteTable)
  ))
_sym_db.RegisterMessage(RouteTable)

RdType0 = _reflection.GeneratedProtocolMessageType('RdType0', (_message.Message,), dict(
  DESCRIPTOR = _RDTYPE0,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.RdType0)
  ))
_sym_db.RegisterMessage(RdType0)

RdType1 = _reflection.GeneratedProtocolMessageType('RdType1', (_message.Message,), dict(
  DESCRIPTOR = _RDTYPE1,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.RdType1)
  ))
_sym_db.RegisterMessage(RdType1)

RdType2 = _reflection.GeneratedProtocolMessageType('RdType2', (_message.Message,), dict(
  DESCRIPTOR = _RDTYPE2,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.RdType2)
  ))
_sym_db.RegisterMessage(RdType2)

RouteDistinguisher = _reflection.GeneratedProtocolMessageType('RouteDistinguisher', (_message.Message,), dict(
  DESCRIPTOR = _ROUTEDISTINGUISHER,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.RouteDistinguisher)
  ))
_sym_db.RegisterMessage(RouteDistinguisher)

L3vpnAddress = _reflection.GeneratedProtocolMessageType('L3vpnAddress', (_message.Message,), dict(
  DESCRIPTOR = _L3VPNADDRESS,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.L3vpnAddress)
  ))
_sym_db.RegisterMessage(L3vpnAddress)

RoutePrefix = _reflection.GeneratedProtocolMessageType('RoutePrefix', (_message.Message,), dict(
  DESCRIPTOR = _ROUTEPREFIX,
  __module__ = 'prpd_common_pb2'
  # @@protoc_insertion_point(class_scope:routing.RoutePrefix)
  ))
_sym_db.RegisterMessage(RoutePrefix)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
