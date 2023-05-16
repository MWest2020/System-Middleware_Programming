import argparse

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Print the capture.')
        self.parser.add_argument('filename', help='File to print')

    def parse_args(self):
        return self.parser.parse_args()
