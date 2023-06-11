from loupe.data_processor import DataProcessor


def test_get_tcp_connections_negative():
    
    # Arrange
    tcp_data = [
        { # Missing 'ip.src'
            "tcp.srcport": "36310",
            "ip.dst": "192.168.0.30",
            "tcp.dstport": "443"       
        },
        { # Missing 'tcp.srcport'
            "ip.src": "192.168.0.1",
            "ip.dst": "192.168.0.34",
            "tcp.dstport": "443"
        },
        { # Missing 'ip.dst'
            "ip.src": "192.168.0.1",
            "tcp.srcport": "37622",
            "tcp.dstport": "443"
        },
        { # Missing 'tcp.dstport'
            "ip.src": "192.168.0.1",
            "tcp.srcport": "37622",
            "ip.dst": "192.168.0.34",
        }
    ]
    
    processor = DataProcessor()
    
    #  ACT
    for data in tcp_data:
        try:
            processor.get_tcp_connections([data])
            # Assert
            assert False, "Expected KeyError"
        except KeyError:
            pass