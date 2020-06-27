from pathlib import Path
from typing import Iterable


def should_continue_processing(
    srcfile: Path, dstfile: Path, force: bool = False
) -> bool:
    """
    Determines whether or not processing should continue
    """

    if srcfile.exists() and srcfile.is_file():
        return any(check_meets_condition(srcfile, dstfile, force))
    else:
        raise FileNotFoundError(f"'{srcfile}' wasn't found or isn't a file...")


def check_meets_condition(srcfile: Path, dstfile: Path, force: bool) -> Iterable[bool]:
    """
    Takes an infile path, an outfile path, and whether or not the job was forced, and returns
    whether or not the existing conditions meet the requirements for processing to continue.
    """

    yield force
    yield not dstfile.exists()
    yield srcfile.lstat().st_mtime_ns > dstfile.lstat().st_mtime_ns
