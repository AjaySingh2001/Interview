Below are **commonly asked Redis interview questions** with **clear answers + simple examples**, ordered from **basic → advanced**.
Short, interview-ready, and practical ✅

---

## 1. What is Redis?

**Answer:**
Redis is an **in-memory, key–value data store** used as a **cache, database, and message broker**.

**Example:**

```bash
SET user:1 "Ajay"
GET user:1
```

---

## 2. Why is Redis so fast?

**Answer:**
Because it stores data **in RAM** and uses **simple data structures** with **single-threaded execution**.

---

## 3. Redis vs Traditional Database?

| Redis          | RDBMS          |
| -------------- | -------------- |
| In-memory      | Disk-based     |
| Key-value      | Tables         |
| Extremely fast | Slower         |
| No joins       | Supports joins |

---

## 4. Is Redis a database?

**Answer:**
Yes, Redis is a **NoSQL in-memory database**, but mostly used as a **cache**.

---

## 5. What data types does Redis support?

**Answer:**

* String
* List
* Set
* Sorted Set
* Hash
* Bitmap
* HyperLogLog
* Stream

---

## 6. What is a Redis String?

**Answer:**
A string stores text, integers, or binary data.

**Example:**

```bash
SET visits 10
INCR visits
```

---

## 7. What is a Redis Hash?

**Answer:**
Used to store **objects** (like a dictionary).

**Example:**

```bash
HSET user:1 name Ajay age 24
HGET user:1 name
```

---

## 8. What is a Redis List?

**Answer:**
A list is an **ordered collection**, useful for queues.

**Example:**

```bash
LPUSH tasks task1
RPUSH tasks task2
```

---

## 9. What is a Redis Set?

**Answer:**
An **unordered collection of unique values**.

**Example:**

```bash
SADD users Ajay Rahul
SMEMBERS users
```

---

## 10. What is a Sorted Set?

**Answer:**
A set where each value has a **score**, auto-sorted.

**Example:**

```bash
ZADD leaderboard 100 Ajay
ZRANGE leaderboard 0 -1 WITHSCORES
```

---

## 11. What is Redis used for?

**Answer:**

* Caching
* Session storage
* Rate limiting
* Pub/Sub
* Leaderboards
* Queues

---

## 12. What is Redis caching?

**Answer:**
Storing frequently used data in Redis to reduce database load.

**Example (Django idea):**

```text
Request → Redis Cache → DB (if cache miss)
```

---

## 13. What is TTL in Redis?

**Answer:**
TTL (Time To Live) sets auto-expiry for keys.

**Example:**

```bash
SET token abc123 EX 60
TTL token
```

---

## 14. What happens after TTL expires?

**Answer:**
Redis **automatically deletes the key** ⏳

---

## 15. What is Redis persistence?

**Answer:**
Saving in-memory data to disk.

**Types:**

* RDB (snapshot)
* AOF (append-only file)

---

## 16. RDB vs AOF?

| RDB                | AOF          |
| ------------------ | ------------ |
| Faster restart     | More durable |
| Less disk          | More disk    |
| Data loss possible | Minimal loss |

---

## 17. Can Redis lose data?

**Answer:**
Yes, if **persistence is disabled** or a crash happens before saving.

---

## 18. What is Redis Pub/Sub?

**Answer:**
A **message broadcasting system**.

**Example:**

```bash
SUBSCRIBE chat
PUBLISH chat "Hello"
```

---

## 19. Redis vs Memcached?

| Redis           | Memcached   |
| --------------- | ----------- |
| Data structures | Only string |
| Persistence     | No          |
| Pub/Sub         | No          |

---

## 20. What is Redis replication?

**Answer:**
Copying data from **master to replicas**.

---

## 21. Redis Master–Slave?

**Answer:**

* Master: write operations
* Slave: read-only copies

---

## 22. What is Redis Sentinel?

**Answer:**
Used for **automatic failover & monitoring**.

---

## 23. What is Redis Cluster?

**Answer:**
A way to **scale Redis horizontally** using shards.

---

## 24. What is Redis eviction policy?

**Answer:**
Controls what happens when memory is full.

**Examples:**

* LRU (Least Recently Used)
* LFU (Least Frequently Used)

---

## 25. What is LRU in Redis?

**Answer:**
Removes **least recently used keys** first.

---

## 26. What is rate limiting using Redis?

**Answer:**
Restricting requests per user/API.

**Example logic:**

```text
INCR user_ip
EXPIRE user_ip 60
```

---

## 27. Is Redis thread-safe?

**Answer:**
Yes ✅
Redis uses a **single-threaded event loop**, making it safe.

---

## 28. Can Redis handle high traffic?

**Answer:**
Yes, Redis can handle **millions of requests/sec**.

---

## 29. Does Redis support transactions?

**Answer:**
Yes, using `MULTI` and `EXEC`.

**Example:**

```bash
MULTI
SET a 1
SET b 2
EXEC
```

---

## 30. Redis vs Kafka?

| Redis         | Kafka            |
| ------------- | ---------------- |
| In-memory     | Disk-based       |
| Fast          | Durable          |
| Simple queues | Distributed logs |

---

## Quick Interview Summary ✅

* Redis = **in-memory NoSQL**
* Extremely **fast**
* Used for **cache, session, rate limiting**
* Supports **multiple data structures**
* TTL + persistence available

If you want:

* 🔹 Redis + Django examples
* 🔹 System design questions
* 🔹 Real production use cases

Just say the word 💡
