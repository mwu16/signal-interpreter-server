from unittest.mock import patch
from signal_interpreter_server.main import parse_arguments, ArgumentParser

class MockArgs:
    file_path="path/to/file"

@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    string='--file_path'
    assert parse_arguments(string)==MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with(string)

