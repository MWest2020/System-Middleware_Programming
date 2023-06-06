#! /usr/bin/env python3

# form the module, import the CLI class
from cli import CLI
from data_processing import DataProcessor

def main():
    print('Hello loupe!')
    cli = CLI()
    args = cli.parse_args()

    #  instantieer de DataProcessor class
    processor = DataProcessor()
    capture = processor.read_json(args.filename)

    connection = ('192.168.1.9', '80', '10.128.0.26', '60755')

    

    # print(capture)
    grouped = processor.group_TCP(connection,  capture)
    print(grouped)



if __name__ == '__main__':
    main()