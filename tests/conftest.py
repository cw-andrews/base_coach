import pytest


@pytest.fixture()
def mock_older_file(mocker):
    older_file = mocker.Mock()
    older_file.exists.return_value = True
    older_file.is_file.return_value = True
    older_file.lstat().st_mtime_ns = 1593281870429685672
    return older_file


@pytest.fixture()
def mock_newer_file(mocker):
    newer_file = mocker.Mock()
    newer_file.exists.return_value = True
    newer_file.is_file.return_value = True
    newer_file.lstat().st_mtime_ns = 1593283551691606047
    return newer_file


@pytest.fixture()
def mock_existing_file(mocker):
    existing_file = mocker.Mock()
    existing_file.exists.return_value = True
    return existing_file


@pytest.fixture()
def mock_nonexistent_file(mocker):
    nonexistent_file = mocker.Mock()
    nonexistent_file.exists.return_value = False
    return nonexistent_file


@pytest.fixture()
def mock_directory(mocker):
    directory = mocker.Mock()
    directory.exists.return_value = True
    directory.is_file.return_value = False
    return directory
