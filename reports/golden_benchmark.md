# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **17/20**
- Evidence hit rate: **85.0%**
- Average retrieval latency: **5147.0 ms**
- Average token reduction vs full source context: **9.2%**
- Golden bonus: **0/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | FAIL | 18876.8 | 0 | 100.0% | BadRequestError: headers: {'date': 'Mon, 17 Aug 2026 10:47:03 GMT', 'content-type': 'application/json; charset=utf-8', 'content-length': '122', 'connection': 'keep-alive', 'vary': 'Origin', 'x-content-type-options': 'nosniff', 'x-ratelimit-increment': '1', 'x-ratelimit-limit': '300', 'x-ratelimit-remaining': '296', 'x-ratelimit-reset': '1786963680', 'strict-transport-security': 'max-age=2592000', 'cf-cache-status': 'DYNAMIC', 'server': 'cloudflare', 'cf-ray': 'a2c81936ad5cdd9e-HKG'}, status_code: 400, body: {'message': 'bad request: session with id eval-g06-v3 already exists', 'request_id': '93464f7b-2914-45c4-957a-cbea5162d87c'} |
| G09 | semantic | PASS | 276.6 | 418 | 8.9% |  |
| G10 | semantic | PASS | 326.0 | 270 | 41.2% |  |
| G14 | mixed | PASS | 2477.9 | 581 | 0.0% |  |
| G03 | long_term | PASS | 2070.1 | 1286 | 0.0% |  |
| G04 | long_term | PASS | 10124.0 | 1279 | 0.0% |  |
| G07 | episodic | PASS | 283.4 | 564 | 0.0% |  |
| G08 | episodic | PASS | 654.6 | 578 | 0.0% |  |
| G11 | mixed | PASS | 3246.5 | 581 | 0.0% |  |
| G13 | mixed | PASS | 21519.9 | 500 | 11.5% |  |
| G15 | mixed | PASS | 2939.6 | 831 | 0.0% |  |
| G16 | mixed | FAIL | 10466.1 | 581 | 0.0% | missing=LAB-REPORT-1600 |
| G17 | mixed | PASS | 13218.5 | 581 | 0.0% |  |
| G18 | mixed | FAIL | 761.4 | 500 | 11.5% | missing=BUDGET-10-4-3-3 |
| G19 | mixed | PASS | 7954.5 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1995.4 | 1308 | 0.0% |  |
| G12 | mixed | PASS | 3503.1 | 560 | 11.4% |  |
| G20 | mixed | PASS | 2245.0 | 756 | 0.0% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

``

### G09 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G10 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend development, as indicated by the Vietnamese phrase 'Java + Spring Boot cho backend examples'.  Lan prefers using Java and Spring Boot and explicitly avoids Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:45     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Minh la Lan, sap giai trinh doi tac ve lua chon backend. Nhac lai: san pham cua minh dung ngon ngu va framework nao? Ch`

### G03 - long_term

`<USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:30     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name": "Nguyen",`

### G04 - long_term

`<USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:44:00     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name": "Nguyen",`

### G07 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playboo`

### G08 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-2`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:57     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name`

### G13 - mixed

`<EPISODIC> EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. E`

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:44:06     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:44:03     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:34     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name`

### G18 - mixed

`<EPISODIC> EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout thresh`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:47:45     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name`

### G05 - long_term

`<USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-05 08:00:00     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name": "Nguyen",`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:40     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
