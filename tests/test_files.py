import pytest

from src.base_coach import files


def test_should_continue_processing_no_src_file_raises_filenotfounderror(
    mock_nonexistent_file, mock_existing_file
):
    with pytest.raises(FileNotFoundError):
        assert files.should_continue_processing(
            mock_nonexistent_file, mock_existing_file
        )


def test_should_continue_processing_src_path_is_directory_raises_filenotfounderror(
    mock_directory, mock_existing_file
):
    with pytest.raises(FileNotFoundError):
        assert files.should_continue_processing(mock_directory, mock_existing_file)


def test_should_continue_processing_existing_src_file_no_filenotfounderror(
    mock_existing_file, mock_nonexistent_file
):
    try:
        files.should_continue_processing(mock_existing_file, mock_nonexistent_file)
    except FileNotFoundError as ex:
        pytest.fail(str(ex))


def test_check_meets_condition_force_returns_true(mock_nonexistent_file):
    assert files.check_meets_condition(
        mock_nonexistent_file, mock_nonexistent_file, force=True
    )


def test_check_meets_condition_no_dst_returns_true(
    mock_existing_file, mock_nonexistent_file
):
    assert files.check_meets_condition(
        mock_existing_file, mock_nonexistent_file, force=False
    )


def test_check_meets_condition_src_newer_than_dst_returns_true(
    mock_newer_file, mock_older_file
):
    assert files.check_meets_condition(mock_newer_file, mock_older_file, force=False)


def test_check_meets_condition_dst_newer_than_src_returns_false(
    mock_newer_file, mock_older_file
):
    assert not any(
        files.check_meets_condition(mock_older_file, mock_newer_file, force=False)
    )
