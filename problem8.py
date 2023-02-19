import pytest


def make_upper(text):
    return text.upper()

def make_capital(text):
    return text.capitalize()

def make_lower(text):
    return text.lower()

def test_method():
    assert make_upper("sajjad")== "SAJJAD"
    assert make_capital("sajjad")=="Sajjad"
    assert make_lower("SaJJAd")=="sajjad"