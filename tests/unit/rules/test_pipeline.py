import pytest
from src.rules.pipeline import apply_rules, load_and_validate

real_messages = [
    ("Call me at +919876543210 or email support@xyzbank.com for your order ID-7890. Card: 4539-1234-5678-9012.", {"phone": True, "email": True, "id": True, "credit": True}),
    ("IRS Notice: You have an outstanding tax issue ref A12345. Immediate action is required. Pay using card 4012888888881881 or contact +441234567890.", {"phone": True, "email": False, "id": True, "credit": True}),
    ("Your bank account is locked. Verify at security@bank.com with ID B4567 or call 1-800-123-4567.", {"phone": True, "email": True, "id": True, "credit": False}),
    ("E-Toll Alert: You have an outstanding balance. Pay immediately to avoid penalties: billing@etoll.com or ID: ET-123456.", {"phone": False, "email": True, "id": True, "credit": False}),
]

@pytest.mark.parametrize("text, expected", real_messages)
def test_apply_rules(text, expected):
    results = apply_rules(text)
    assert results["phone"] is expected["phone"]
    assert results["email"] is expected["email"]
    assert results["id"] is expected["id"]
    assert results["credit"] is expected["credit"]

def test_load_and_validate():
    text = "+919876543210"
    results = load_and_validate(text)
    assert results["phone"] is True