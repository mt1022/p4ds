from sys import argv, stderr


def print_hello(to, location):
    """
    Say hello!
    """
    print(f'Hello, {to}! This is a greeting from {location}!')
    return None


if __name__ == '__main__':
    if len(argv[1:]) == 2:
        print_hello(*argv[1:])
    else:
        print(f'Parameter error: 2 were required but {len(argv[1:])} were given.', file=stderr)
