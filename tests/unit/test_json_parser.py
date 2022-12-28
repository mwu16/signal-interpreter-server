from unittest.mock import patch, mock_open
from pandas.testing import assert_frame_equal
from signal_interpreter_server.json_parser import JsonParser, json
import pandas as pd 

data={"services": [{"title": "ECU Reset", "id": "11"}]}
data_string=json.dumps(data)
df=pd.DataFrame(data["services"])

jsonParser = JsonParser()


def test_load_file():
    with patch("builtins.open", mock_open(read_data=data_string)):
        jsonParser.load_file("file_to_path")
        print(data_string)
        assert jsonParser.get_data()==data_string

def test_data2pd():
    jsonParser.data2pd(data_string)
    assert_frame_equal(jsonParser.get_data(),df)

def test_get_signal_title():
    assert jsonParser.get_signal_title(df,"11")=="ECU Reset"

