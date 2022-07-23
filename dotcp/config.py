import os
import sys
from getpass import getuser
from pathlib import PosixPath
from typing import List, NoReturn, Optional, Union, Generator, Iterable

from . import log


def detect_config_home() -> Optional[PosixPath]:
    for path in [
        PosixPath(os.getenv("XDG_CONFIG_HOME")),
        PosixPath("~/.config"),
        PosixPath("~/.config").expanduser(),
        PosixPath(f"/home/{getuser()}/.config"),
        PosixPath(PosixPath.home().joinpath(".config")),
    ]:
        if path.exists():
            return path
    return None


class Config:
    path: PosixPath
    content: str

    def __init__(self, *, path: Optional[PosixPath]):
        if path:
            self.path = path
        else:
            config_home = detect_config_home()
            if not config_home:
                log.error(
                    "could not detect config home. Please set config file path manually "
                    "(using --config parameter)",
                    terminate=True,
                )
            self.path = config_home.joinpath("dotcp", "config")
        if not self.path.exists():
            log.error(f"dotcp config file ({self.path}) does not exist", terminate=True)
        self.content = self._read()

    def _read(self) -> Union[str, NoReturn]:
        try:
            with open(self.path, "r", encoding="utf=8") as file:
                return file.read()
        except FileNotFoundError:
            log.error(f"could not open dotcp config file ({self.path}) - file not found", terminate=True)
        except PermissionError:
            log.error(
                f"could not open dotcp config file ({self.path}) - permission denied", terminate=True
            )
        except Exception as err:
            log.error(
                f"could not open dotcp config file ({self.path}) - unknown error: {str(err)}",
                terminate=True,
            )

    def get_targets(self) -> Union[List[PosixPath], NoReturn]:
        terminate = False
        lines = self.content.splitlines()
        for i, line in enumerate(lines):
            line_number = i + 1
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            target = PosixPath(line)
            if target.expanduser().exists():
                yield target
            else:
                terminate = True
                log.error(f"target {target} indicated in ({self.path}:{line_number}) does not exist")
        if terminate:
            log.echo("Terminating due to errors above.")
            sys.exit(-1)
