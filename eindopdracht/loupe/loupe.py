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

    # print(capture)
    grouped = processor.group_TCP(capture)
    print(grouped)



if __name__ == '__main__':
    main()