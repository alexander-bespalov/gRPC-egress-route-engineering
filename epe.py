#!/usr/bin/python

import math
import socket
import struct
import time
from grpc.beta import implementations
import lib.authentication_service_pb2 as authentication_service_pb2
import lib.bgp_route_service_pb2 as bgp_route_service_pb2
import lib.dcd_service_pb2 as dcd_service_pb2
import lib.firewall_service_pb2 as firewall_service_pb2
import lib.jnx_addr_pb2 as jnx_addr_pb2
import lib.mgd_service_pb2 as mgd_service_pb2
import lib.openconfig_service_pb2 as openconfig_service_pb2
import lib.prpd_common_pb2 as prpd_common_pb2
import lib.prpd_service_pb2 as prpd_service_pb2
import lib.registration_service_pb2 as registration_service_pb2

user = 'api'
password = 'juniper-api'
host = '192.168.255.18'
client_id = 'jet-epe'
port = 50051
timeout = 5

def auth():
	try:
		global channel
		channel = implementations.insecure_channel(host=host, port=port)
		login = authentication_service_pb2.beta_create_Login_stub(channel)
		login_response = login.LoginCheck(
			authentication_service_pb2.LoginRequest(
				user_name = user,
				password = password,
				client_id = client_id
			),
			timeout
		)
		if login_response.result == True:
			print "gRPC: Connected and authenticated"
		else:
			print "gRPC: Authentication failed"
			exit(0)
	except Exception as tx:
		print "Unable to establish gRPC connection:", tx
		exit(0)

def bgp_init():
	global bgp
	bgp = bgp_route_service_pb2.beta_create_BgpRoute_stub(channel)
	result = bgp.BgpRouteCleanup(bgp_route_service_pb2.BgpRouteCleanupRequest(), timeout)
	result = bgp.BgpRouteInitialize(bgp_route_service_pb2.BgpRouteInitializeRequest(), timeout)
	if result.status == 0:
		print "BGP route initialize: SUCCESS"
	else:
		print "BGP route initialize:", result
		exit(0)

def get_bgp_route(prefix, prefix_len, protocol, table, or_longer):
	if protocol == "BGP":
		protocol = 1
	elif protocol == "BGP_STATIC":
		protocol = 2
	else:
		protocol = 0
	bgp_route_request = bgp_route_service_pb2.BgpRouteGetRequest(
		bgp_route = bgp_route_service_pb2.BgpRouteMatch(
			dest_prefix = prpd_common_pb2.RoutePrefix(
				inet = jnx_addr_pb2.IpAddress(addr_string = prefix)
			),
			dest_prefix_len = prefix_len,
			table = prpd_common_pb2.RouteTable(
				rtt_name = prpd_common_pb2.RouteTableName(name = table)
			),
			protocol = protocol
		),
		or_longer = or_longer
	)
	result = dict()
	for routes in bgp.BgpRouteGet(bgp_route_request, timeout):
		if routes.status == 8:
			pass
		elif routes.status != 0:
			exit(0)
		for route in routes.bgp_routes:
			if route.aspath.aspath_string != "":
				try:
					result[route.dest_prefix.inet.addr_string]
				except:
					result[route.dest_prefix.inet.addr_string] = {}
				try:
					result[route.dest_prefix.inet.addr_string][route.dest_prefix_len]
				except:
					result[route.dest_prefix.inet.addr_string][route.dest_prefix_len] = []
				result[route.dest_prefix.inet.addr_string][route.dest_prefix_len].append(route.protocol_nexthops[0].addr_string)
	return result

def update_bgp_route(table, prefix, prefix_len, next_hop):
	print "update_bgp_route:", table, prefix, "/", prefix_len, "=>", next_hop
	result = bgp.BgpRouteUpdate(
		bgp_route_service_pb2.BgpRouteUpdateRequest(
			bgp_routes = [
				bgp_route_service_pb2.BgpRouteEntry(
					dest_prefix = prpd_common_pb2.RoutePrefix(
						inet = jnx_addr_pb2.IpAddress(addr_string = prefix)
					),
					dest_prefix_len = prefix_len,
					table = prpd_common_pb2.RouteTable(
						rtt_name = prpd_common_pb2.RouteTableName(name = table)
					),
					protocol_nexthops = [ jnx_addr_pb2.IpAddress(addr_string = next_hop) ],
					communities = bgp_route_service_pb2.CommunityList(
						com_list = [
							bgp_route_service_pb2.Community(community_string = "65535:65281")
						]
					)
				)
			]
		)
		, timeout
	)
	if result.status != 0:
		print result

def remove_bgp_route(table, prefix, prefix_len, next_hop):
	print "remove_bgp_route:", table, prefix, "/", prefix_len, "=>", next_hop
	result = bgp.BgpRouteRemove(
		bgp_route_service_pb2.BgpRouteRemoveRequest(
			or_longer = 0,
			bgp_routes = [
				bgp_route_service_pb2.BgpRouteMatch(
					dest_prefix = prpd_common_pb2.RoutePrefix(
						inet = jnx_addr_pb2.IpAddress(addr_string = prefix)
					),
					dest_prefix_len = prefix_len,
					table = prpd_common_pb2.RouteTable(
						rtt_name = prpd_common_pb2.RouteTableName(name = table)
					),
					protocol = 2
				)
			]
		),
		timeout
	)
	if result.status != 0:
		print result

def main():
	auth()
	bgp_init()
	programmed = []
	while True:
		routes = get_bgp_route(
			prefix = "0.0.0.0",
			prefix_len = 0,
			protocol = "BGP",
			table = "inet.0",
			or_longer = True
		)
		to_programm = []
		to_remove = []
		for destination, ref1 in routes.iteritems():
			for length, nh in ref1.iteritems():
				nh.sort()
				if len(nh) > 1 and length < 28:
					if len(nh) == 2 or len(nh) == 4 or len(nh) == 8 or len(nh) == 16 or len(nh) == 32:
						split_to = len(nh)
					elif len(nh) > 8:
						split_to = 32
					elif len(nh) > 4:
						split_to = 16
					else:
						split_to = 8
					destination_dec = destination.split(".")
					destination_dec = long(destination_dec[0]) * 256 * 256 * 256 + long(destination_dec[1]) * 256 * 256 + long(destination_dec[2]) * 256 + long(destination_dec[3])
					new_length = length + int(math.log(split_to, 2))
					add = 2 ** (32 - new_length)
					for i in range(0, split_to):
						new_destination = destination_dec + add * i
						new_destination = socket.inet_ntoa(struct.pack('!L', new_destination))
						new_nh = nh[int(math.fmod(i, len(nh)))]
						to_programm.append(new_destination + "-" + str(new_length) + "-" + new_nh)
		new_programmed = [x for x in to_programm]
		to_remove = [x for x in programmed]
		i = 0
		for exist in to_remove:
			for new in to_programm:
				if exist == new:
					to_remove[i] = ''
					break
			i = i + 1
		to_remove = [x for x in to_remove if x != '']
		i = 0
		for new in to_programm:
			for exist in programmed:
				if exist == new:
					to_programm[i] = ''
					break
			i = i + 1
		to_programm = [x for x in to_programm if x != '']
		for item in to_remove:
			[prefix, prefix_len, next_hop] = item.split("-")
			remove_bgp_route(table = "inet.0", prefix = prefix, prefix_len = int(prefix_len), next_hop = next_hop)
		for item in to_programm:
			[prefix, prefix_len, next_hop] = item.split("-")
			update_bgp_route(table = "inet.0", prefix = prefix, prefix_len = int(prefix_len), next_hop = next_hop)
		programmed = [x for x in new_programmed]
		time.sleep(5)
	exit(1)

if __name__ == "__main__":
	main()
