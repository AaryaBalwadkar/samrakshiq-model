from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.transform.redact.apply import redact_entities
from src.models.ner.infer import infer_entities
import random
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

indian_messages = [
    "SBI: Txn to +919876543210, ID: SBI-1234, card 4111-1111-1111-1111.",
    "HDFC: Alert on 4123-4567-8912-3456 via email hdfc@alert.in.",
    "ICICI: Update Aadhaar ID AA-789012, call +918765432109.",
    "Paytm: Rs 500 to +919223344556, Ref: PTM-3456.",
    "Jio: Recharge Rs 299, ID: JIO-2345, contact jio@care.in.",
]

@app.get("/api/messages")
async def get_messages():
    message = random.choice(indian_messages)
    entities = infer_entities(message)
    start = time.time()
    redacted = redact_entities(message)
    redact_time = (time.time() - start) * 1000

    start = time.time()
    hashed = message
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            hashed = hashed.replace(entity, f"[{entity_type.upper()}_HASH:{hash(entity)}]")
    hash_time = (time.time() - start) * 1000

    metrics = {"redactTime": redact_time, "hashTime": hash_time, "pseudoTime": 0.0, "fpeTime": 0.0, "aesTime": 0.0}
    return {"messages": [{"id": random.randint(1, 1000), "text": redacted}], "metrics": metrics}