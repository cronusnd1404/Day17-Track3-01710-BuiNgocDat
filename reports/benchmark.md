# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **4**
- Passed: **3/4**
- Evidence hit rate: **75.0%**
- Average retrieval latency: **3977.3 ms**
- Average token reduction vs full source context: **25.0%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E09 | long_term | FAIL | 5723.7 | 0 | 100.0% | BadRequestError: headers: {'date': 'Mon, 17 Aug 2026 10:01:19 GMT', 'content-type': 'application/json; charset=utf-8', 'content-length': '119', 'connection': 'keep-alive', 'vary': 'Origin', 'x-content-type-options': 'nosniff', 'x-ratelimit-increment': '1', 'x-ratelimit-limit': '300', 'x-ratelimit-remaining': '278', 'x-ratelimit-reset': '1786960920', 'strict-transport-security': 'max-age=2592000', 'cf-cache-status': 'DYNAMIC', 'server': 'cloudflare', 'cf-ray': 'a2c7d6361fe7dd57-HKG'}, status_code: 400, body: {'message': 'bad request: session with id eval-e09 already exists', 'request_id': '11c1a765-ada3-4130-9c8c-289c7109f34c'} |
| E02 | long_term | PASS | 2702.4 | 1270 | 0.0% |  |
| E03 | long_term | PASS | 4359.2 | 1265 | 0.0% |  |
| E08 | long_term | PASS | 3123.9 | 1290 | 0.0% |  |

## Evidence excerpts

### E09 - long_term

``

### E02 - long_term

`<USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 09:00:00     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name": "Nguyen",`

### E03 - long_term

`<USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 09:04:00     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name": "Nguyen",`

### E08 - long_term

`<USER_SUMMARY> The user works on a company project named BLUEBIRD-42, which requires using TypeScript with NestJS and prohibits Python. For personal demos, the user prefers Python for their project ORCHID-27.  The user prefers Python and dislikes Java. They prefer short examples when code is explained. They are learning async/await and sometimes confuse coroutines with Tasks. When this topic arises, they want it explained using a timeline. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-05 08:00:00     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name": "Nguyen",`
