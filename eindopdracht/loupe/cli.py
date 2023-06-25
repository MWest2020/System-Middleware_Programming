import argparse


class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Print the capture.')
        self.parser.add_argument('filename', help='File to read')

        # Define a subparser for the blacklist command
        self.subparsers = self.parser.add_subparsers(dest='command')

        # For `blacklist` as a command taking a filename as an argument
        self.blacklist_parser = self.subparsers.add_parser(
            'blacklist', help='process blacklist')
        self.blacklist_parser.add_argument(
            '--blacklist_file', help='the blacklist JSON file')

        # Separate parser for `blacklisted` command
        self.blacklisted_parser = self.subparsers.add_parser(
            'blacklisted', help='process individual blacklist entry')
        self.blacklisted_parser.add_argument(
            '--dst', '-d', required=True, help='destination IP for blacklist')
        self.blacklisted_parser.add_argument(
            '--src', '-s', required=True, help='source IP for blacklist')

        # Add --srcport and --dstport arguments to 'blacklisted' command as
        # well
        self.blacklisted_parser.add_argument(
            '--srcport', '-p', required=True, help='source port for blacklist')
        self.blacklisted_parser.add_argument(
            '--dstport', '-P', required=True, help='destination port for blacklist')

        # work from here on for the get functionality
        self.get_parser = self.subparsers.add_parser(
            'get', help='process get command'
        )

        # ## here's where the second commands need to be
        # self.get_parser = self.subparsers.add_parser(
        #     'get', help='process get command')

        self.get_parser.add_argument(
            '--flags',
            action="store_true",
            help="Track changes in TCP flags"
        )

        self.get_parser.add_argument(
            '--src', help='source IP for get command')
        self.get_parser.add_argument(
            '--srcport', help='source port for get command')
        self.get_parser.add_argument(
            '--dst', help='destination IP for get command')
        self.get_parser.add_argument(
            '--dstport', help='destination port for get command')

        self.scan_parser = self.subparsers.add_parser(
            'scan', help='scan entire dataset for potential attacks')
        self.scan_parser.add_argument(
            '--output', '-o', required=True,
            help='File to which potential attacks should be written')

        # thirs question
        self.time_parser = self.subparsers.add_parser(
            'time', help='Process time duration thresholds')

        self.time_parser.add_argument(
            '--duration',
            action="store_true",
            help="Show duration of each TCP connection"
        )

        # Add the duration-threshold argument to the 'time' subparser
        self.time_parser.add_argument(
            '--duration-threshold',
            type=float,
            default=300.0,  # Default value of 5 minutes
            help="Duration threshold for TCP connections, in seconds"
        )

        self.time_parser.add_argument(
            '--blacklist_file',
            required=False,
            help='File that contains blacklisted IP addresses'
        )

        self.time_parser.add_argument(
            '--output', '-o', required=False,
            help='File to which times connections are written to')

    def parse_args(self):
        return self.parser.parse_args()
