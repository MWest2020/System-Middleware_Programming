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

    processor.write_tcp_connections(tcp, '../data/tcp_connections.json')

    
    # THIS IS ONLY FOR 1 IP ADDRESS
    if args.command == 'blacklisted':
        # If specific source or destination IP is specified, create a list with
        # only that IP address
        if args.dst and args.src and args.dstport and args.srcport:
            # Create a list with only one item, a tuple representing the
            # connection details
            blacklist = [(args.src, args.srcport, args.dst, args.dstport)]
            # Compare TCP connections against the blacklist
            blacklisted = processor.compare_blacklist(tcp, blacklist)

            # print results
            print(f"The TCP connection you entered is linked to a blacklist: ")
            print(f"Blacklisted connection: {blacklist}")
        else:
            # Error: blacklisted command needs specific connection details
            print(
                "Error: Please specify connection details" +
                "(source IP, source port, destination IP, destination port)"
            )

    if args.command == 'blacklist':
        if args.blacklist_file:
            # If a blacklist file is specified, read it

            blacklist = processor.read_json(args.blacklist_file)
            print(f"Blacklist: {blacklist}")

        # Compare TCP connections against the blacklist
        blacklisted = processor.compare_blacklist(tcp, blacklist)

        # Prob what user only wants to know:
        if blacklisted:
            for connection in blacklisted:
                src_ip = connection['ip.src']
                dst_ip = connection['ip.dst']
                if src_ip in [b['ip.src'] for b in blacklist]:
                    print(f"The source IP address {src_ip} is blacklisted.")
                if dst_ip in [b['ip.dst'] for b in blacklist]:
                    print(f"The destination IP address {dst_ip} is blacklisted.")


        if args.blacklist_file:
            print(
                f"Out of {len(tcp)} TCP connections," +
                f"{len(blacklisted)} connections have blacklisted IP addresses.")
            # print(f"Blacklisted connections: {blacklisted}")


if __name__ == '__main__':
    main()
