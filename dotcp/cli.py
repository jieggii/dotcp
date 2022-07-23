from argparse import ArgumentParser, RawTextHelpFormatter, HelpFormatter
from pathlib import PosixPath

from . import __version__


def get_args_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="dotcp",
        description="copy selected dotfiles to directory",
        epilog="epilog"
    )
    parser.add_argument(
        "dest",
        type=PosixPath,
        help="destination directory (where targets will be put)",
    )
    parser.add_argument(
        "--remove-outdated",
        action="store_true",
        help="remove copies of targets, that are not listed in the config file anymore"
    )
    parser.add_argument("--config", "-c", type=PosixPath, help="path to dotcp config file")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser
