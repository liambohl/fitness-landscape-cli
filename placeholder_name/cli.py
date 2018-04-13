"""
fitness-landscape-cli
Usage:
  fitness-landscape-cli hello
  fitness-landscape-cli -h | --help
  fitness-landscape-cli --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
Examples:
  fitness-landscape-cli hello
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/liambohl/fitness-landscape-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import placeholder_name.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(placeholder_name.commands, k) and v:
            module = getattr(placeholder_name.commands, k)
            placeholder_name.commands = getmembers(module, isclass)
            command = [command[1] for command in placeholder_name.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
