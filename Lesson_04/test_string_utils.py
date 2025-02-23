import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, result",
    [
        ("escapism", "Escapism"),
        ("hello kitty", "Hello kitty"),
        ("class3", "Class3"),
        ("number-5", "Number-5"),
        ("österreich", "Österreich")
    ])
def test_capitalize_positive(string, result):
    assert string_utils.capitalize(string) == result


@pytest.mark.parametrize(
    "string, result",
    [
        (" Trombone", "Trombone"),
        ("   Violin", "Violin"),
        (" 2016-2021", "2016-2021")
    ])
def test_trim_positive(string, result):
    assert string_utils.trim(string) == result


@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("Hippo", "i", True),
        (" rhino", "r", True),
        ("Zebra  ", "a", True),
        ("Mary-Alice", "-", True),
        ("1990", "1", True),
        ("UFC", "F", True)
    ])

def test_contains_positive(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("Football", "ball", "Foot"),
        ("Basketball", "Basket", "ball"),
        ("20256", "6", "2025"),
        ("Stalin-grad", "-", "Stalingrad"),
        ("Nov gorod", " ", "Novgorod"),
        ("Snow", "S", "now"),
        ("Rabbit", "b", "Rait")
    ])

def test_delete_symbol_positive(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, result",
    [
        ("1998year", "1998year"),
        ("", ""),
        ("   ", "   "),
        ("Rose", "Rose")
    ])

def test_capitalize_negative(string, result):
    assert string_utils.capitalize(string) == result


@pytest.mark.parametrize(
    "string, result",
    [
        (". Drums", ". Drums"),
        ("b u s i n e s s", "b u s i n e s s"),
        ("George ", "George "),
        ("", "")
    ])
def test_trim_negative(string, result):
    assert string_utils.trim(string) == result


@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("Lion", "l", False),
        ("giraffe", "G", False),
        ("wolf", "v", False),
        ("Mary Alice", "-", False),
        ("", "a", False),
        ("tiger", "abc", False)
    ])

def test_contains_negative(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("Penguin", "q", "Penguin"),
        ("", "", ""),
        ("", "k", ""),
        ("2012", "3", "2012"),
        ("Polar bear", "-", "Polar bear"),
        ("Frog", "", "Frog")
    ])

def test_delete_symbol_negative(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result
