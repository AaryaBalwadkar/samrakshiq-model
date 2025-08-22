import pytest
from src.rules.pipeline import apply_rules, load_and_validate

real_messages = [
    ("Call me at +919876543210x or email support@xyzbank.com for your order ID-7890. Card: 4539-1234-5678-9012.", {"phone": True, "email": True, "id": True, "credit": True}),
    ("Hi, it’s John, and I need you to purchase $500 in gift cards as soon as possible for a client and send me the codes to john.doe@example.com or call 987-654-3210.", {"phone": True, "email": True, "id": False, "credit": False}),
    ("IRS Notice: You have an outstanding tax issue ref A12345. Immediate action is required. Pay using card 4012888888881881 or contact +441234567890.", {"phone": True, "email": False, "id": True, "credit": True}),
    ("Your bank account is locked. Verify at security@bank.com with ID B4567 or call 1-800-123-4567.", {"phone": True, "email": True, "id": True, "credit": False}),
    ("Congratulations! You've won a prize. Claim by sending your credit card details to prize@contest.org or phone +123-456-7890.", {"phone": True, "email": True, "id": False, "credit": False}),
    ("E-Toll Alert: You have an outstanding balance. Pay immediately to avoid penalties: billing@etoll.com or ID: ET-123456.", {"phone": False, "email": True, "id": True, "credit": False}),
    ("Insiders say Bitcoin is about to explode in value. Buy now: invest@crypto.org with your card 5105105105105100 or call (123) 456-7890.", {"phone": True, "email": True, "id": False, "credit": True}),
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