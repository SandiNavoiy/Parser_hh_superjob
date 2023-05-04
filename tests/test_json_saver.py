import json
import pytest
from json import JSONDecodeError
from scr.abc import JsonSave
from scr.json_saver import JSONSaver


@pytest.fixture
def json_saver(tmp_path):
    file_path = tmp_path / "test_file.json"
    file_path.touch()
    return JSONSaver(file_path)


def test_add_vacancy(json_saver):
    json_saver.add_vacancy("1", [{"number": "1", "title": "Python Developer"}])
    with json_saver.filename.open() as file:
        data = json.load(file)
    assert len(data) == 1
    assert data[0]["number"] == "1"
    assert data[0]["title"] == "Python Developer"


def test_remove_vacancy(json_saver):
    json_saver.add_vacancy("1", [{"number": "1", "title": "Python Developer"}])
    json_saver.add_vacancy("2", [{"number": "2", "title": "Java Developer"}])
    json_saver.remove_vacancy("1")
    with json_saver.filename.open() as file:
        data = json.load(file)
    assert len(data) == 1
    assert data[0]["number"] == "2"
    assert data[0]["title"] == "Java Developer"


