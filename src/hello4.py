import click
from sys import stderr


@click.command(context_settings=dict(help_option_names=['-h', '--help'], show_default=True))
@click.argument('to', type=click.STRING)
@click.option('-l', '--location', type=click.STRING, default='Lanzhou', help='say hello from where?')
def print_hello(to, location):
    """
    Say hello to someone from somwhere.

    Arguments\n
    to: say hello to whom?
    """
    print(f'Hello, {to}! This is a greeting from {location}!')
    return None


if __name__ == '__main__':
    print_hello()
