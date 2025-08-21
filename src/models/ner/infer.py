import onnxruntime as ort
import re
import numpy as np
from typing import Dict, List
from src.rules.phone.validate import validate_phone
from src.rules.email.validate import validate_email
from src.rules.ids.validate import validate_id
from src.rules.credit.validate import validate_credit

# Precompile once at module import:
PHONE_RE = re.compile(r'(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}')
EMAIL_RE = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
ID_RE    = re.compile(r'\b(?:(?:ID|ref)[- ]?[A-Za-z0-9]{2,20}|[A-Za-z]{2,5}[-]?\d{2,10})\b', re.IGNORECASE)
CREDIT_RE= re.compile(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b|\b\d{13,16}\b')
NON_DIGIT_RE = re.compile(r'\D')  # handy if needed

class NERInfer:
    def __init__(self, model_path: str = "models/ner_model.onnx"):
        try:
            self.session = ort.InferenceSession(model_path)
            self.input_name = self.session.get_inputs()[0].name
            self.output_name = self.session.get_outputs()[0].name
        except (FileNotFoundError, ort.capi.onnxruntime_pybind11_state.NoSuchFile):
            self.session = None

    def predict(self, text: str) -> Dict[str, List[str]]:
        # If you ever enable ONNX later, keep the fast path identical.
        if self.session is None:
            # IMPORTANT: extract ONCE and validate EACH candidate (no re.findall inside loops)
            credit_candidates = CREDIT_RE.findall(text)
            # remove credit-like strings from text before phone lookup to avoid misclassification
            text_wo_credit = text
            for c in credit_candidates:
                # Replace with spaces (preserve indices length-wise; also avoids merging tokens)
                text_wo_credit = text_wo_credit.replace(c, ' ' * len(c))

            phone_candidates = PHONE_RE.findall(text_wo_credit)
            email_candidates = EMAIL_RE.findall(text)
            id_candidates    = ID_RE.findall(text)

            entities = {
                "credit": [c for c in credit_candidates if validate_credit(c)],
                "phone" : [p for p in phone_candidates  if validate_phone(p)],
                "email" : [e for e in email_candidates  if validate_email(e)],
                "id"    : [i for i in id_candidates     if validate_id(i)],
            }
            return entities

        # Placeholder ONNX path (kept minimal and cheap)
        input_data = np.array([[ord(c) for c in text]], dtype=np.float32)
        _ = self.session.run([self.output_name], {self.input_name: input_data})[0]
        # You’ll likely map ONNX spans to strings here later.
        return {"phone": [], "email": [], "id": [], "credit": []}

def infer_entities(text: str) -> Dict[str, List[str]]:
    ner = NERInfer()
    return ner.predict(text)
