# gRPC-egress-route-engineering

## Description
The application is scannning BGP routing table and finding routes advertised by multiple BGP peers. Each route advertised by multiple BGP peers will be splitted to several sub-routes with a single BGP next-hop.
E.g route 10.0.0.0/22 is advertised by BGP peers [ 1.1.1.1, 2.2.2.2, 3.3.3.3, 4.4.4.4 ] will be splitted and avertised as 4 sub-routes:
 - 10.0.0.0/24 => 1.1.1.1
 - 10.0.1.0/24 => 2.2.2.2
 - 10.0.2.0/24 => 3.3.3.3
 - 10.0.3.0/24 => 4.4.4.4

## Junos requirements
Junos 16.2 and higher

Junos configuration example to enable gRPC:
```
system {
    services {
        extension-service {
            request-response {
                grpc {
                    clear-text {
                        port 50051;
                    }
                }
            }
        }
    }
}
```
