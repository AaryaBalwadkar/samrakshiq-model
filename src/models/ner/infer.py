import onnxruntime as ort
import re
import numpy as np
from typing import Dict, List
from src.rules.phone.validate import validate_phone
from src.rules.email.validate import validate_email
from src.rules.ids.validate import validate_id
from src.rules.credit.validate import validate_credit

class NERInfer:
    def __init__(self, model_path: str = "models/ner_model.onnx"):
        try:
            self.session = ort.InferenceSession(model_path)
            self.input_name = self.session.get_inputs()[0].name
            self.output_name = self.session.get_outputs()[0].name
        except (FileNotFoundError, ort.capi.onnxruntime_pybind11_state.NoSuchFile):
            self.session = None

    def predict(self, text: str) -> Dict[str, List[str]]:
        if self.session is None:
            phone_candidates = re.findall(r'(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}', text)
            email_candidates = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
            id_candidates = re.findall(r'\b(?:(?:ID|ref)[- ]?[A-Za-z0-9]{2,20}|[A-Za-z]{2,5}[-]?\d{2,10})\b', text, re.IGNORECASE)
            credit_candidates = re.findall(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b|\b\d{13,16}\b', text)

            entities = {
                "phone": [e for e in phone_candidates if validate_phone(text) and any(re.sub(r'\D', '', m).isdigit() and 10 <= len(re.sub(r'\D', '', m)) <= 15 for m in re.findall(r'(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}', text))],
                "email": [e for e in email_candidates if validate_email(text) and any(re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', e.lower()) for e in email_candidates)],
                "id": [e for e in id_candidates if validate_id(text) and any(re.search(r'\b(?:(?:ID|ref)[- ]?[A-Za-z0-9]{2,20}|[A-Za-z]{2,5}[-]?\d{2,10})\b', e, re.IGNORECASE) for e in id_candidates)],
                "credit": [e for e in credit_candidates if validate_credit(text) and any(re.match(r'^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}$|\b\d{13,16}\b', re.sub(r'[\s-]', '', e)) for e in credit_candidates)]
            }
        else:
            input_data = np.array([[ord(c) for c in text]], dtype=np.float32)
            result = self.session.run([self.output_name], {self.input_name: input_data})[0]
            entities = {"phone": [], "email": [], "id": [], "credit": []}
            if len(result[0]) > 0:
                entities["phone"] = [e for e in re.findall(r'(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}', text) if validate_phone(text)]
        return entities

def infer_entities(text: str) -> Dict[str, List[str]]:
    ner = NERInfer()
    return ner.predict(text)
