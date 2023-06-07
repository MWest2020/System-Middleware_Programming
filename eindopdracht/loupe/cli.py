import argparse

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Print the capture.')
        self.parser.add_argument('filename', help='File to read')

        # Define a subparser for the blacklist command
        self.subparsers = self.parser.add_subparsers(dest='command')

        # For `blacklist` as a command taking a filename as an argument
        self.blacklist_file_parser = self.subparsers.add_parser('blacklist', help='process blacklist from file')
        self.blacklist_file_parser.add_argument('blacklist_file', help='the blacklist JSON file')

        # For `blacklist` as a command with individual src, srcport, dst, dstport as arguments
        self.blacklist_parser = self.subparsers.add_parser('blacklisted', help='process individual blacklist entry')
        self.blacklist_parser.add_argument('--src', required=True, help='source IP for blacklist')
        self.blacklist_parser.add_argument('--srcport', required=True, help='source port for blacklist')
        self.blacklist_parser.add_argument('--dst', required=True, help='destination IP for blacklist')
        self.blacklist_parser.add_argument('--dstport', required=True, help='destination port for blacklist')

    def parse_args(self):
        return self.parser.parse_args()
