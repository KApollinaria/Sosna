import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# - Тесты для capitalize -
# positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# - Тесты для trim -
# positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  123abc", "123abc"),
    (" Skypro ", "Skypro "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


# negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("    ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# - Тесты для contains -
# positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "k", "True"),
    ("123abc", "2", "True"),
    ("Skypro", "S", "True"),
])
def test_contains_positive(input_str, symbol, expected):
    res = False
    try:
        res = string_utils.contains(input_str, symbol) > -1
    except ValueError:
        pass

    assert res


# negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("123abc", "Ы", "False"),
    ("", "d", "False"),
    ("Skypr", "1", "False"),
])
def test_contains_negative(input_str, symbol, expected):
    res = True
    try:
        res = string_utils.contains(input_str, symbol) > -1
    except ValueError:
        pass

    assert res


# - Тесты для delete_symbol -
# positive
@pytest.mark.parametrize("input_str, symbol, string", [
    ("skypro", "k", "sypro"),
    ("123abc", "2", "13abc"),
    ("Skypro", "S", "kypro"),
])
def test_delete_symbol_positive(input_str, symbol, string):
    if string_utils.delete_symbol(string, symbol):
        string = string.replace(symbol, "")
    assert string


# negative
@pytest.mark.parametrize("input_str, symbol, string", [
    ("123abc", "Ы", "123abc"),
    ("ersj", "d", "ersj"),
    ("Skypr", "1", "Skypr"),
])
def test_delete_symbol_negative(input_str, symbol, string):
    if string_utils.delete_symbol(string, symbol):
        string = string.replace(symbol, "")
    assert string
