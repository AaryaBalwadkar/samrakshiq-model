# src/models/ner/ensemble.py
from typing import Dict, List
from .infer import NERInfer
# from src.rules.pipeline import apply_rules  # <- avoid this extra pass if possible

class EnsembleNER:
    def __init__(self):
        self.ner = NERInfer()

    def combine_predictions(self, ml_entities: Dict[str, List[str]]) -> Dict[str, List[str]]:
        # If entities were found, that's equivalent to rule_results[type] == True
        # (since your validators would return True if those substrings exist).
        return {
            "phone":  ml_entities["phone"]  if ml_entities["phone"]  else [],
            "email":  ml_entities["email"]  if ml_entities["email"]  else [],
            "id":     ml_entities["id"]     if ml_entities["id"]     else [],
            "credit": ml_entities["credit"] if ml_entities["credit"] else [],
        }

    def predict(self, text: str) -> Dict[str, List[str]]:
        ml_entities = self.ner.predict(text)
        return self.combine_predictions(ml_entities)

# If you want a single entry point:
def infer_entities(text: str) -> Dict[str, List[str]]:
    ensembler = EnsembleNER()
    return ensembler.predict(text)
