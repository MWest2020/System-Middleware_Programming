import argparse


class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Print the capture.')
        self.parser.add_argument('filename', help='File to read')

        # Define a subparser for the blacklist command
        self.subparsers = self.parser.add_subparsers(dest='command')

        ## For `blacklist` as a command taking a filename as an argument
        self.blacklist_parser = self.subparsers.add_parser(
            'blacklist', help='process blacklist')
        self.blacklist_parser.add_argument(
            '--blacklist_file', help='the blacklist JSON file')
        self.blacklist_parser.add_argument(
            '--src', '-s', help='source IP for blacklist')
        self.blacklist_parser.add_argument(
            '--srcport', '-p', help='source port for blacklist')
        self.blacklist_parser.add_argument(
            '--dst', '-d', help='destination IP for blacklist')
        self.blacklist_parser.add_argument(
            '--dstport', '-P', help='destination port for blacklist')

        ## Separate parser for `blacklisted` command
        self.blacklisted_parser = self.subparsers.add_parser(
            'blacklisted', help='process individual blacklist entry')
        self.blacklisted_parser.add_argument(
            '--dst', '-d', required=False, help='destination IP for blacklist')
        self.blacklisted_parser.add_argument(
            '--src', '-s', required=False, help='source IP for blacklist')

        ## Add --srcport and --dstport arguments to 'blacklisted' command as
        # well
        self.blacklisted_parser.add_argument(
            '--srcport', '-p', help='source port for blacklist')
        self.blacklisted_parser.add_argument(
            '--dstport', '-P', help='destination port for blacklist')
        
        
        # work from here on for the get functionality
        self.get_parser = self.subparsers.add_parser(
            'get', help='process get command'
        )
        
        ## here's where the second commands need to be
        self.get_parser.add_argument(
            '--flags',
            # action='store_true',
            help='Tacks changes in TCP flags'    
        )
        
        self.get_parser.add_argument(
            '--src', '-s', help='source IP for get command')
        self.get_parser.add_argument(
            '--srcport', '-p', help='source IP for get command')
        self.get_parser.add_argument(
            '--dst', '-d', help='source IP for get command')
        self.get_parser.add_argument(
            '--dstport', '-P', help='source IP for get command')
        
        
    def parse_args(self):
        return self.parser.parse_args()
