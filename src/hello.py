from sys import argv


def print_hello(to, location):
    """
    Say hello!
    """
    print(f'Hello, {to}! This is a greeting from {location}!')
    return None


if __name__ == '__main__':
    print_hello(argv[1], argv[2])
