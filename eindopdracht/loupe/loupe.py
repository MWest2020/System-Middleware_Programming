#! /usr/bin/env python3

# form the module, import the CLI class
from cli import CLI
from data_processor import DataProcessor


def main():
    print('Hello loupe!')
    cli = CLI()
    args = cli.parse_args()

    # Instantiate the data_processor class
    processor = DataProcessor()

    # Read the file from the CLI input and store it in a variable
    capture = processor.read_json(args.filename)

    # Get all connections from the capture
    tcp = processor.get_tcp_connections(capture)

    if args.command == 'blacklist':
        if args.blacklist_file:
            # If a blacklist file is specified, read it
            blacklist = processor.read_json(args.blacklist_file)
            
            
        elif args.src and args.srcport and args.dst and args.dstport:
            # If specific connection details are specified, create a list
            blacklist = [[args.src, args.srcport, args.dst, args.dstport]]
            print(f"The TCP connection you enters is linked to a blacklist: ")
            print(f"Blacklisted connection: {blacklist}")
        else:
            # Error: blacklist command needs either a blacklist file or specific connection details
            print("Error: Please specify either a blacklist file or specific connection details")
            return 
        
        # Compare TCP connections against the blacklist
        blacklisted = processor.compare_blacklist(tcp, blacklist)

        if args.blacklist_file:
            print(f"Out of {len(tcp)} TCP connections, {len(blacklisted)} are blacklisted.")
            print(f"Blacklisted connections: {blacklisted}")

if __name__ == '__main__':
    main()
