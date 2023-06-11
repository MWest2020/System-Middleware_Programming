from loupe.data_processor import DataProcessor

import pytest


# ARRANGE
@pytest.fixture
def real_tcp_data_sample():
    return [
        {
            "_source": {
                "layers": {
                    "ip": {
                        "ip.src": "192.168.0.1",
                        "ip.dst": "192.168.0.30",
                    },
                    "tcp": {
                        "tcp.srcport": "36310",
                        "tcp.dstport": "443"
                    },
                    "frame":{
                        "frame.time": "date"
                    }
                }
            }     
        },
        {
            "_source": {
                "layers": {
                    "ip": {
                        "ip.src": "192.168.0.1",
                        "ip.dst": "192.168.0.34",
                    },
                    "tcp": {
                        "tcp.srcport": "37622",
                        "tcp.dstport": "443"
                    },
                    "frame":{
                        "frame.time": "date"
                    }
                    
                }
            }
        }
    ]

@pytest.fixture 
def processor():
    return DataProcessor()

# Act
def test_get_tcp_connections(real_tcp_data_sample, processor):
    tcp_connections = processor.get_tcp_connections(real_tcp_data_sample)

    # ASSERT
    # Asserting that the number of tcp connections is the same as the input data
    assert len(tcp_connections) == len(real_tcp_data_sample)

    # Assert keys and values are present in each connection. 
    for connection in tcp_connections:
        assert 'ip.src' in connection and connection['ip.src']
        assert 'ip.dst' in connection and connection['ip.dst']
        assert 'tcp.srcport' in connection and connection['tcp.srcport']
        assert 'tcp.dstport' in connection and connection['tcp.dstport']


