import pytest
import json
import pandas as pd
import os.path

from scr.transform import Transform
@pytest.fixture
def test_json_file():
    """Фикстура для тестов"""
    data = [
        {"title": "Software Engineer", "location": "San Francisco"},
        {"title": "Data Scientist", "location": "New York"},
        {"title": "Product Manager", "location": "Seattle"}
    ]
    file_name = "test.json"
    with open(file_name, "w") as f:
        json.dump(data, f)
    yield file_name
    os.remove(file_name)


def test_to_txt(test_json_file):
    """Тест для метода test_to_txt класса Transform"""
    file_name = "favor.txt"
    t = Transform(test_json_file)
    t.to_txt()
    assert os.path.isfile(file_name)
    with open(file_name, "r", encoding="utf8") as f:
        data = json.load(f)
    assert data == json.load(open(test_json_file))
    os.remove(file_name)


def test_json_to_xls(test_json_file):
    """Тест для метода test_json_to_xls класса Transform"""
    file_name = "favor.xlsx"
    t = Transform(test_json_file)
    t.json_to_xls()
    assert os.path.isfile(file_name)
    data = pd.read_excel(file_name)
    assert data.to_dict("records") == json.load(open(test_json_file))
    os.remove(file_name)