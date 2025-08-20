import yaml
from typing import Dict, List
from pathlib import Path

def load_yaml_policy(file_path: str) -> Dict[str, List[str]]:
    """Load validation rules from YAML file."""
    path = Path(file_path)
    with path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}