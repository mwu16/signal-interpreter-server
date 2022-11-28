from signal_interpreter_server.json_parser import JsonParser
import os

def test_get_signal_title_with_valid_id():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    json_parser.load_file(json_parser.data)
    assert json_parser.get_signal_title("11")=="ECU Reset"

def test_load_file_with_valid_input():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    json_parser.load_file(json_parser.data)
    assert json_parser.data.shape[0]==1

def test_open_file_with_valid_file_path():
    json_parser=JsonParser()
    file_path=os.path.dirname(__file__)
    file_path=os.path.join(file_path, "..", "data", "signal_database_test.json")
    json_parser.open_file(file_path)
    assert len(json_parser.data["services"])==1
