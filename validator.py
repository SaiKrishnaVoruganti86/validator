from sdx_topology_validator import (load_openapi_schema, resolve_references, get_validator_schema, validate)
from pathlib import Path

dir = Path(__file__).parent
yml_file = dir / "test.yaml"



data = {
    "id": "urn:sdx:topology:amlight.net",
    "name": "AmLight-OXP",
    "version": 2,
    "model_version": "2.0.0",
    "timestamp": "2021-07-01T23:59:59Z",
    "nodes": [
        {
            "id": "urn:sdx:node:amlight.net:Ampath1",
            "name": "Ampath1",
            "location": {
                "address": "Equinix MI1, Miami, FL",
                "latitude": 25.76,
                "longitude": -80.19
            },
            "ports": [
                {
                    "id": "urn:sdx:port:amlight.net:Ampath1:1",
                    "name": "Ampath1-eth1",
                    "node": "urn:sdx:node:amlight.net:Ampath1",
                    "type": "1GE",
                    "status": "up",
                    "state": "disabled"
                }
            ],
            "status": "error",
            "state": "enabled"
        }
    ],
    "links": [
        {
            "id": "urn:sdx:link:amlight.net:Ampath3/2_Ampath1/2",
            "name": "Link1",
            "ports": [  {
                    "id": "urn:sdx:port:amlight.net:Ampath1:1",
                    "name": "Ampath1-eth1",
                    "node": "urn:sdx:node:amlight.net:Ampath1",
                    "type": "1GE",
                    "status": "up",
                    "state": "enabled"
                }],
            "type": "intra",
            "bandwidth": 500000,
            "residual_bandwidth": 80,
            "latency": 25,
            "packet_loss": 0.1,
            "availability": 99.5,
            "status": "up",
            "state": "enabled"
        }
    ]
}

validator_schema = get_validator_schema(resolve_references(load_openapi_schema(yml_file)))  
validation_result = validate(data, validator_schema)
print(validation_result)