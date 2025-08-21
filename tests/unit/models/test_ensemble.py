import pytest
from src.models.ner.infer import infer_entities
import re

real_indian_messages = [
    "SBI Alert: Your UPI txn to +919876543210 is successful. Ref ID: UPI-123456. If not you, report to support@sbi.in.",
    "HDFC Bank: Suspicious activity on card 4111-1111-1111-1111. Verify at hdfc@alert.com or call 1-800-123-4567.",
    "ICICI: Update your Aadhaar details via ID AA-789012. Email icici@update.in or call +918765432109.",
    "Win Rs 1 Lakh lottery! Send credit card 5105 1051 0510 5100 to lottery@win.in. Ref: LOT-3456, phone +919223344556.",
    "TRAIPotential Spam: Toll due Rs 200. Pay with card 4000-1234-5678-9012 or call +917654321098. ID: TOLL-9012.",
    "PhonePe: Rs 500 transferred to UPI ID user@phonepe. If error, email phonepe@support.in or call 1800-456-7890.",
    "Axis Bank: Alert on 4500 1234 5678 9012. Contact axis@bank.in with ref AX-5678 or phone +919445566778.",
    "Paytm: Transaction ref PTM-9012 failed. Retry with card 4123-4567-8912-3456 or call +919556677889.",
    "Jio Recharge: Rs 299 successful. ID: JIO-2345. For queries, email jio@care.in or call +918934567890.",
    "Kotak: Rs 1000 withdrawn. Verify with ID KOT-6789 or card 4111 1111 1111 1111 at kotak@notify.com.",
    "IRCTC: PNR 1234567890 booked. Track with +919667788990 or email irctc@book.in. Ref: IRCTC-3456.",
    "BSNL: Bill Rs 350 due. Pay with card 5105-1051-0510-5100 or ID BSN-7890 at bsnl@bill.in.",
    "Vodafone: Recharge Rs 199. Call +918745632109 for support. Email vodafone@recharge.in. ID: VOD-9012.",
    "Reliance: Payment alert on 4012-8888-8888-1881. Ref: REL-2345. Contact +919778899001.",
    "Ola: Ride booked with ID OLA-5678. Pay using card 4500-1234-5678-9012 or call 1800-789-0123.",
    "MakeMyTrip: Booking MMT-9012 confirmed. Email mmt@trip.in or call +919889900112.",
    "BigBasket: Order BB-2345 delivered. Pay with 4123 4567 8912 3456 or ID BB-ID-4567.",
    "Zomato: Order ZOM-5678. Contact zomato@food.in with ref Z-7890 or phone +919990001122.",
    "Swiggy: Delivery with ID SWG-9012. Use card 4000 1234 5678 9012 or email swiggy@delivery.in.",
    "Amazon India: Order AMZ-2345 shipped. Track with +919001122334 or ID AMZ-ID-5678.",
] * 500  # Replicate to reach ~100 messages

@pytest.mark.parametrize("text", real_indian_messages)
def test_ensemble_detection(text):
    entities = infer_entities(text)
    phone_pattern = re.compile(r'(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,4}\d{2,4}')
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    id_pattern = re.compile(r'\b(?:(?:ID|ref|PNR)[- ]?[A-Za-z0-9]{2,20}|[A-Za-z]{2,5}[-]?\d{2,10})\b', re.IGNORECASE)
    credit_pattern = re.compile(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b|\b\d{13,16}\b')

    has_phone = any(phone_pattern.search(e) for e in entities["phone"]) if entities["phone"] else False
    has_email = any(email_pattern.search(e) for e in entities["email"]) if entities["email"] else False
    has_id = any(id_pattern.search(e) for e in entities["id"]) if entities["id"] else False
    has_credit = any(credit_pattern.search(e) for e in entities["credit"]) if entities["credit"] else False

    assert any([has_phone, has_email, has_id, has_credit]), f"No entities detected in {text}"