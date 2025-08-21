from typing import Dict
from time import time
from .phone.validate import validate_phone
from .email.validate import validate_email
from .ids.validate import validate_id
from .credit.validate import validate_credit
from ..api.config.yaml_loader import load_yaml_policy


def apply_rules(text: str) -> Dict[str, bool]:
    start = time()

    results = {}
    for name, validator in [
        ("phone", validate_phone),
        ("email", validate_email),
        ("id", validate_id),
        ("credit", validate_credit),
    ]:
        try:
            results[name] = validator(text)
        except Exception as e:
            print(f"[ERROR] {name} validator failed with: {e}")
            results[name] = False

    latency = time() - start
    print(f"Validation latency: {latency:.4f}s")
    return results



def load_and_validate(text: str, policy_file: str = "policies/rules.yaml") -> Dict[str, bool]:
    """Load policy and validate text."""
    policy = load_yaml_policy(policy_file)
    return apply_rules(text)
