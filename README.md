# gRPC-egress-route-engineering

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
