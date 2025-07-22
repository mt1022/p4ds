import argparse
from sys import stderr


def print_hello(to, location):
    """
    Say hello!
    """
    print(f'Hello, {to}! This is a greeting from {location}!')
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'python src/hello3.py',
        description = 'Say hello to someone from somwhere.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # required arguments (input and output)
    parser.add_argument('to',
                        metavar='to',
                        help='say hello to whom?')
    # optional arguments
    parser.add_argument('-l', '--loc',
                        type=str,
                        default='Lanzhou',
                        help='say hello from where?')
    args = parser.parse_args()
    print_hello(to=args.to, location=args.loc)
