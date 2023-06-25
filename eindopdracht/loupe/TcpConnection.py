class TcpConnection:
    def __init__(self, src_ip, src_port, dst_ip, dst_port, duration=None, flags=None):
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.duration = duration
        self.flags = flags if flags else []
        
    def to_dict(self):
        return {
            "src_ip": self.src_ip,
            "src_port": self.src_port,
            "dst_ip": self.dst_ip,
            "dst_port": self.dst_port,
            "duration": self.duration,
            "flags": self.flags
        }
