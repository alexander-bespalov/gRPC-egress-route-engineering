# gRPC-egress-route-engineering

## Description
The application is scannning BGP routing table and finding routes advertised by multiple BGP peers. Each route advertised my multiple BGP peers will be splitted to several sub-routes with a single BGP next-hop.


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
