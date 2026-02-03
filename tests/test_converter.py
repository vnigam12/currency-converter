import pytest
from src.converter import convert, convert_multiple

def test_convert_same_currency():
    assert convert(100, "USD", "USD") == 100

def test_convert_valid():
    result = convert(100, "USD", "EUR")
    assert result > 0

def test_convert_invalid_amount():
    with pytest.raises(ValueError):
        convert(-5, "USD", "EUR")

def test_convert_invalid_currency():
    with pytest.raises(ValueError):
        convert(100, "XXX", "EUR")

def test_convert_multiple():
    results = convert_multiple(100, "USD", ["EUR", "CAD", "GBP"])
    assert "EUR" in results
    assert "CAD" in results
    assert "GBP" in results
    assert results["EUR"] > 0
