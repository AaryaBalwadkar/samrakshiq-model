# SamrakshIQ Task Board

Privacy-first SMS anonymizer for global compliance (GDPR/HIPAA/DPDP).

## Day 0: Setup [Done]
- [x] Initialize Git repo with modular structure
- [x] Configure FastAPI backend (`src/api/`)
- [x] Set up Vite/React/TypeScript/Tailwind UI (`src/ui/`)
- [x] Add utils for logging, metrics, preprocessing
- [x] Verify API (`http://localhost:8000/health`)
- [x] Verify UI (`http://localhost:5173`)

## Day 1: I/O + Schema [Done]
- [x] Implement streaming parsers (`src/parsers/`)
- [x] Define Pydantic schema (`src/schema/message.py`)
- [x] Write unit tests (`tests/unit/parsers/`)
- [x] Test 3 sample files, log performance

## Day 2: Rule Engine & Validators
- [x] Add phone validator (`src/rules/phone/validate.py`)
- [x] Add email validator (`src/rules/email/validate.py`)
- [x] Add ID validator (`src/rules/ids/validate.py`)
- [x] Add credit card validator (`src/rules/credit/validate.py`)
- [x] Implement YAML policy loader (`src/api/config/yaml_loader.py`)
- [x] Integrate rules in pipeline, measure latency
- [x] Write unit tests (`tests/unit/rules/`)

## Day 3: ML Models
- [x] Implement ONNX NER inference (`src/models/ner/infer.py`)
- [x] Add obfuscation heuristics (`src/models/obfuscate/detect.py`)
- [x] Build ensemble model, test on 100 messages
- [x] Optimize for CPU performance
- [x] Write unit tests (`tests/unit/models/`)

## Day 4: Transformations + KeyStore
- [ ] Implement redaction (`src/transform/redact/apply.py`)
- [ ] Implement hashing (`src/transform/hash/apply.py`)
- [ ] Implement pseudonymization (`src/transform/pseudo/apply.py`)
- [ ] Implement FPE (`src/transform/fpe/apply.py`)
- [ ] Add AES-256 encryption (`src/keystore/crypto/aes.py`)
- [ ] Write roundtrip tests, measure encryption perf

## Day 5: UI Integration + Metrics
- [ ] Build UI components for review (`src/ui/src/components/`)
- [ ] Style with Tailwind (`src/ui/src/styles/`)
- [ ] Integrate API calls (`src/ui/src/hooks/useApi.ts`)
- [ ] Add metrics dashboard (`src/utils/metrics/`)
- [ ] Test end-to-end UI flow

## Day 6: Red-Team Testing
- [ ] Run adversarial tests for parsers/rules
- [ ] Generate compliance report (`docs/compliance.md`)
- [ ] Implement data deletion utils
- [ ] Fix edge cases from tests

## Day 7: Docs + Final Tests
- [ ] Write quickstart guide (`docs/quickstart.md`)
- [ ] Add compliance notes (`docs/compliance.md`)
- [ ] Run end-to-end tests (`tests/integration/`)
- [ ] Verify local run (API/UI)