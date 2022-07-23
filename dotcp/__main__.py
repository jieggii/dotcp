import sys
import time
from shutil import copytree, rmtree
from pathlib import PosixPath

from dotcp import cli, config, log


def main():
    parser = cli.get_args_parser()
    args = parser.parse_args()

    cfg = config.Config(path=args.config)
    targets = cfg.get_targets()

    dest: PosixPath = args.dest
    dest.mkdir()  # asdasd

    for target in targets:
        path = target.expanduser()
        if path.is_relative_to(PosixPath.home()):
            copytree(path.resolve(), dest.joinpath(target))
        else:
            print(target, "from other")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.error("interrupted by user.", terminate=True)
