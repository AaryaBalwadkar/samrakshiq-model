import pytest
from src.rules.phone.validate import validate_phone
from src.rules.email.validate import validate_email
from src.rules.ids.validate import validate_id
from src.rules.credit.validate import validate_credit

def test_phone_validator():
    assert validate_phone("+1234567890") is True
    assert validate_phone("123-456-7890") is True
    assert validate_phone("123.456.7890") is True
    assert validate_phone("abc") is False

def test_email_validator():
    assert validate_email("user@example.com") is True
    assert validate_email("test.user@domain.co") is True
    assert validate_email("invalid@") is False

def test_id_validator():
    assert validate_id("A123") is True
    assert validate_id("ID-456") is True
    assert validate_id("12") is False

def test_credit_validator():
    assert validate_credit("4111111111111111") is True
    assert validate_credit("4111-1111-1111-1111") is True
    assert validate_credit("123") is False