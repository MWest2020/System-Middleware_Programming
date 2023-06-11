from loupe.data_processor import DataProcessor


def test_get_connection_durations():
    # Arrange
    processor = DataProcessor()
    # mock tcp connections
    tcp_connections = [
        {"ip.src": "192.168.1.1", "tcp.srcport": "12345", "ip.dst": "192.168.1.2", "tcp.dstport": "80", "timestamp": "Jun 07, 2023 00:00:01.000000"},
        {"ip.src": "192.168.1.1", "tcp.srcport": "12345", "ip.dst": "192.168.1.2", "tcp.dstport": "80", "timestamp": "Jun 07, 2023 00:00:02.000000"}
    ]

    # Act
    connection_durations = processor.get_connection_durations(tcp_connections, 'normally here should be an output file ')

    # Assert
    
    # check if connection id is taken out of the conenctions and the timestap process and calculated 
    assert connection_durations == {('192.168.1.1', '12345', '192.168.1.2', '80'): 1.0}

