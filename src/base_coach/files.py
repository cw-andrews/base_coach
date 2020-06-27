from pathlib import Path


def should_continue_processing(
    infile: Path, outfile: Path, force: bool = False
) -> bool:
    """
    Determines whether or not processing should continue
    """

    if infile.exists() and infile.is_file():
        return any(check_meets_condition(infile, outfile, force))
    else:
        raise FileNotFoundError(f"'{infile}' wasn't found or isn't a file...")


def check_meets_condition(infile: Path, outfile: Path, force: bool):
    """
    Takes an infile path, an outfile path, and whether or not the job was forced, and returns
    whether or not the existing conditions meet the requirements for processing to continue.
    """

    yield force
    yield not outfile.exists()
    yield infile.lstat().st_mtime_ns > outfile.lstat().st_mtime_ns
