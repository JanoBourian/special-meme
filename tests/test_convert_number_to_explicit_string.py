import pytest
from convert_number_to_explicit_string import number_to_string


def test_number_to_string_zero():
    assert number_to_string(0) == (0, f"CERO PESOS 0/100 M.N.")


def test_number_to_string_zerostr():
    assert number_to_string("0") == (0, f"CERO PESOS 0/100 M.N.")


def test_number_to_string_zero_decimal():
    assert number_to_string(0.0) == (0, f"CERO PESOS 0/100 M.N.")


def test_number_to_string_zerostr_decimal():
    assert number_to_string("0.0") == (0, f"CERO PESOS 0/100 M.N.")


def test_number_to_string_strin():
    assert number_to_string("123") == (123, f"CIENTO VEINTITRES PESOS 0/100 M.N.")


def test_number_to_string_strfloat():
    assert number_to_string("123.25") == (
        123.25,
        f"CIENTO VEINTITRES PESOS 25/100 M.N.",
    )


def test_number_to_string_float():
    assert number_to_string(123.25) == (123.25, f"CIENTO VEINTITRES PESOS 25/100 M.N.")


def test_number_to_string_int():
    assert number_to_string(123) == (123, f"CIENTO VEINTITRES PESOS 0/100 M.N.")


def test_number_to_string_1():
    assert number_to_string(1) == (1, f"UN PESOS 0/100 M.N.")


def test_number_to_string_2():
    assert number_to_string("2") == (2, f"DOS PESOS 0/100 M.N.")


def test_number_to_string_3():
    assert number_to_string("3") == (3, f"TRES PESOS 0/100 M.N.")


def test_number_to_string_raises():
    assert number_to_string("1t23.25") == None
