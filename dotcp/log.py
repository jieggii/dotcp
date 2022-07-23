import sys


def echo(message: str) -> None:
    sys.stdout.write(f"{message}\n")


def warning(message: str) -> None:
    sys.stdout.write(f"Warning: {message}.\n")


def error(message: str, *, terminate: bool = False) -> None:
    sys.stderr.write(f"Error: {message}.\n")
    if terminate:
        sys.exit(-1)
