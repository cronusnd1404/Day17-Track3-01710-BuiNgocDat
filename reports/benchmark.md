# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **2**
- Passed: **2/2**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **7794.4 ms**
- Average token reduction vs full source context: **69.2%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E06 | semantic | PASS | 15108.8 | 164 | 64.3% |  |
| E11 | semantic | PASS | 480.1 | 146 | 74.2% |  |

## Evidence excerpts

### E06 - semantic

`ENTITY: POST /payments -  ENTITY: Payment API Retry Policy - For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. ENTITY: max-3-retries -  ENTITY: PAYMENT-RULE-3 -  ENTITY: Idempotency-Key -  ENTITY: transient 5xx errors -  ENTITY: HTTP 429 -  ENTITY: timeout - When async HTTP calls time out, inspect connection pooling, downstream saturation, and concurrency before increasing the timeout. Reuse a long-lived client session where possible. The recommended first step is to inspect connection pooling.`

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`
