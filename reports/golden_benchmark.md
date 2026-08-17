# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **19/20**
- Evidence hit rate: **95.0%**
- Average retrieval latency: **1039.5 ms**
- Average token reduction vs full source context: **4.2%**
- Golden bonus: **0/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1333.6 | 896 | 0.0% |  |
| G09 | semantic | PASS | 205.5 | 418 | 8.9% |  |
| G10 | semantic | PASS | 222.7 | 270 | 41.2% |  |
| G14 | mixed | PASS | 1507.5 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1494.1 | 1589 | 0.0% |  |
| G04 | long_term | PASS | 1543.6 | 1728 | 0.0% |  |
| G07 | episodic | PASS | 241.5 | 564 | 0.0% |  |
| G08 | episodic | PASS | 217.6 | 578 | 0.0% |  |
| G11 | mixed | PASS | 1687.8 | 581 | 0.0% |  |
| G13 | mixed | PASS | 423.9 | 500 | 11.5% |  |
| G15 | mixed | PASS | 1768.3 | 831 | 0.0% |  |
| G16 | mixed | FAIL | 1731.5 | 581 | 0.0% | missing=LAB-REPORT-1600 |
| G17 | mixed | PASS | 1665.7 | 581 | 0.0% |  |
| G18 | mixed | PASS | 415.8 | 500 | 11.5% |  |
| G19 | mixed | PASS | 1887.5 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1358.2 | 1704 | 0.0% |  |
| G12 | mixed | PASS | 1544.1 | 560 | 11.4% |  |
| G20 | mixed | PASS | 1540.7 | 756 | 0.0% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`EPISODE: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. EPISODE: Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. EPISODE: Lan uu tien stack backend nao cho LOTUS-88?  FACT: Lan Tran does not use Python in backend examples. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: LOTUS-88 uses Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T`

### G09 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G10 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G14 - mixed

`<LONG_TERM> FACT: LOTUS-88 uses Java. [valid_at=2026-08-01T11:00:20Z, invalid_at=None]  <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend development, as indicated by the Vietnamese phrase 'Java + Spring Boot cho backend examples'.  Lan prefers using Java and Spring Boot and explicitly avoids Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 12:22:33     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?`

### G03 - long_term

`EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong EPISODE: Sep hoi chu`

### G04 - long_term

`EPISODE: Minh con open loop hay deadline nao chua hoan thanh? EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang timeout. Scope Minh, dung tron Lan. EPISODE: Minh sap giai thich coro`

### G07 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nha`

### G08 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurr`

### G11 - mixed

`<LONG_TERM> FACT: Lab Assistant checks the connection pool. [valid_at=2026-08-03T10:01:00Z, invalid_at=None]  <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 12:22:52     Sou`

### G13 - mixed

`<EPISODIC> EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh EPISODE: Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay styl EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn,`

### G15 - mixed

`<LONG_TERM> EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong FACT: Minh Nguyen identifies connection churn as the main issue. [valid_at=2026-08-03T10:03:00Z, invalid_at=None]  <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning a`

### G16 - mixed

`<LONG_TERM> FACT: Minh Nguyen's personal project is ORCHID-27. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z]  <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-`

### G17 - mixed

`<LONG_TERM> FACT: Connection churn is not the timeout threshold. [valid_at=2026-08-03T10:03:00Z, invalid_at=None]  <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 12:23:02   `

### G18 - mixed

`<EPISODIC> EPISODE: Cong ty yeu cau chinh context window cho agent tren dung backend du an cong ty. Minh can biet stack bat buoc cua BLUEBIRD va ty le budget bon tang nho trong lab de cau hinh cho dun EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. G EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE`

### G19 - mixed

`<LONG_TERM> FACT: Da hieu has a personal demo ORCHID-27. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:20Z]  <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 12:`

### G05 - long_term

`EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam`

### G12 - mixed

`<LONG_TERM> EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. FACT: Minh Nguyen identifies connection churn as the main issue. [valid_at=2026-08-03T10:03:00Z, invalid_at=None]  <USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks.`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
