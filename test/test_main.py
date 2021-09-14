import pyappgen.main as main
import pytest


@pytest.mark.parametrize("name, allowed_chars, is_long_name",
                         [("test_name", ["_"], False),
                          ("test_name_one", ["_"], False),
                          ("tony", ["_"], False),
                          ])
def test_valid_project_name(name: str, allowed_chars: [], is_long_name: bool):
    assert main.is_name_valid(name, allowed_chars, is_long_name).is_valid


@pytest.mark.parametrize("name, allowed_chars, is_long_name",
                         [("testName", ["_"], False),
                          ("test_name_one_&", ["_"], False),
                          ("testnameone_", ["_"], False),
                          ("_testnameone", ["_"], False),
                          ])
def test_invalid_project_name(name: str, allowed_chars: [], is_long_name: bool):
    assert not main.is_name_valid(name, allowed_chars, is_long_name).is_valid


@pytest.mark.parametrize("name, allowed_chars, is_long_name",
                         [("test_name", ["_"], False),
                          ("test_name_one", ["_"], False),
                          ("tony", ["_"], False),
                          ("ToNyN", ["_"], False)
                          ])
def test_valid_project_long_name(name: str, allowed_chars: [], is_long_name: bool):
    pass


@pytest.mark.parametrize("name, allowed_chars, is_long_name",
                         [("test_name_one_&", ["_"], False),
                          ("testnameone_", ["_"], False),
                          ("_testnameone", ["_"], False),
                          ])
def test_invalid_project_long_name(name: str, allowed_chars: [], is_long_name: bool):
    pass
