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

    processor.write_json('../data/tcp_connections.json', tcp)
    
    
    if args.command == 'get':
        print('Are you getting this?') 
    

    # THIS IS ONLY FOR 1 CONNECTION
    if args.command == 'blacklisted':
        # If specific source or destination IP is specified, create a list with
        # only that IP address

        # If all arg.args are truthy
        if args.dst and args.src and args.dstport and args.srcport:
            # Create a list with only one item, a tuple representing the
            # connection details
            blacklist = {
                "ip.src": args.src,
                "tcp.srcport": args.srcport,
                "ip.dst": args.dst,
                "tcp.dstport": args.dstport
            }

            # Compare TCP connections against the blacklist
            blacklisted = processor.compare_blacklist(tcp, blacklist)



            # print results
            print(f"The TCP connection you entered is a marked connection: ")
            print(f"Blacklisted connection: ")
            # check and print blacklisted ips
            processor.check_blacklisted_ips(
                blacklisted, '../data/blacklisted_ips.json')
            # bla

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

        # Compare TCP connections against the blacklist
        blacklisted = processor.compare_blacklist(tcp, blacklist)

        # Prob what user only wants to know:
        if blacklisted:
            # makes unique
            printed_ips = set()
            for connection in blacklisted:
                src_ip = connection['ip.src']
                dst_ip = connection['ip.dst']
                # if ip is in blacklist and NOT in printed_ips
                if src_ip in [b['ip.src']
                              for b in blacklist] and src_ip not in printed_ips:
                    print(f"The source IP address {src_ip} is blacklisted.")
                    printed_ips.add(src_ip)
                if dst_ip in [b['ip.dst']
                              for b in blacklist] and dst_ip not in printed_ips:
                    print(
                        f"The destination IP address {dst_ip} is blacklisted.")
                    printed_ips.add(dst_ip)

        if args.blacklist_file:
            print(
                f"Out of {len(tcp)} TCP connections," +
                f"{len(blacklisted)} connections have blacklisted IP addresses.")
            # print(f"Blacklisted connections: {blacklisted}")


if __name__ == '__main__':
    main()
