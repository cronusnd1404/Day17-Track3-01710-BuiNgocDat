# Lab 17 Submission

## Phan tich memory

Trong bo practice nay, long-term la layer quan trong nhat vi E02, E03, E08, E09 va mot phan E07 phu thuoc vao Context Block, recency va user isolation. Neu layer nay sai, agent mat preference, deadline va fact cua user qua nhieu session; E09 con co nguy co leak cross-user.

Context Block cua Zep tien hon Redis + Qdrant khi can managed ingestion, relevance va context theo user/thread; code van ngan va co provenance. Redis + Qdrant re hon va kiem soat schema, TTL, ranking tot hon cho baseline, nhung phai tu lo ingestion, search, isolation, compaction va consistency.

Chong memory poisoning bang consent va user-scoped namespace, chi ghi durable facts khi co provenance, timestamp va confidence; khong tu dong ghi preference/task co tac dong cao neu chua co policy hoac human review. Can giu audit trail va cho phep forget theo user.

## Benchmark va ky thuat

Layer co hit rate thap nhat duoc ket luan tu `reports/benchmark.json`, bang cach nhom case theo `expected_layer` va dem PASS/total; khong suy doan tu latency. Case can nhieu token nhat la case co `retrieved_tokens` lon nhat trong report.

E07 la mixed case: router lay long-term cho `Python` va semantic graph cho `Idempotency-Key`, sau do `ContextBudgetManager` ghep theo thu tu short-term, long-term, episodic, semantic. Token reduction chi cho biet context ngan hon; no khong tu dong lam hit rate tang vi marker co the da bi cat boi budget.

E08 uu tien fact moi `TypeScript`/`NestJS` nhung van giu `BLUEBIRD-42` va provenance de giai thich conflict. E10 compaction giu durable constraint `REVIEW-DEADLINE-1600`, `Friday`, `16:00` va recent turns thay vi giu toan bo transcript.
