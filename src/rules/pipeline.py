from typing import Dict, List
from time import time
from .phone.validate import validate_phone
from .email.validate import validate_email
from .ids.validate import validate_id
from .credit.validate import validate_credit
from ..api.config.yaml_loader import load_yaml_policy

def apply_rules(text: str) -> Dict[str, bool]:
    """Apply validation rules to text and return results."""
    start = time()
    tokens = text.split()
    results = {
        "phone": any(validate_phone(token) for token in tokens),
        "email": any(validate_email(token) for token in tokens),
        "id": any(validate_id(token) for token in tokens),
        "credit": any(validate_credit(token) for token in tokens)
    }
    latency = time() - start
    print(f"Validation latency: {latency:.4f}s")
    return results

def load_and_validate(text: str, policy_file: str = "policies/rules.yaml") -> Dict[str, bool]:
    """Load policy and validate text."""
    policy = load_yaml_policy(policy_file)
    return apply_rules(text)