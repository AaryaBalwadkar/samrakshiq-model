import pytest
from sms import parse_sms
from src.rules.pipeline import apply_rules

adversarial_inputs = [
    "+91987654321x",  # Invalid phone
    "test@domain..in",  # Invalid email
    "4111-1111-1111-111g",  # Invalid credit card
    "91+9876543210",  # Obfuscated phone
    "user.name@domain.in\x00",  # Null byte in email
]

@pytest.mark.parametrize("text", adversarial_inputs)
def test_adversarial_validation(text):
    parsed = parse_sms(text)
    assert parsed is not None, f"Parser failed on {text}"
    results = apply_rules(parsed)
    assert all(not value for value in results.values()), f"Validation accepted invalid {text} with results {results}"
