import argparse

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Print the capture.')
        self.parser.add_argument('filename', help='File to read')

        # Define a subparser for the blacklist command
        self.subparsers = self.parser.add_subparsers(dest='command')

        # For `blacklist` as a command taking a filename as an argument
        self.blacklist_parser = self.subparsers.add_parser('blacklist', help='process blacklist')
        self.blacklist_parser.add_argument('--blacklist_file', help='the blacklist JSON file')
        self.blacklist_parser.add_argument('--src', help='source IP for blacklist')
        self.blacklist_parser.add_argument('--srcport', help='source port for blacklist')
        self.blacklist_parser.add_argument('--dst', help='destination IP for blacklist')
        self.blacklist_parser.add_argument('--dstport', help='destination port for blacklist')

    def parse_args(self):
        return self.parser.parse_args()
