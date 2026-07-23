# Scaling Note (80,000 pages)

The prototype works for small batches, but several changes would be required to scale to 80,000 pages.

## Recommended changes

### Queue-based orchestration

Replace the sequential Python loop with a distributed queue such as RabbitMQ, Kafka, or AWS SQS.

### Persistent storage

Store events, generated metadata, image candidates, and link graphs in a database rather than JSON files.

### Cached prompt templates

Cache repeated prompts and shared context to reduce token usage and API costs.

### Parallel processing

Run subagents concurrently using worker pools or serverless functions.

### Centralized link graph

Maintain a shared internal-link graph to prevent orphan pages and improve crawl depth.

### Image pipeline

Download, deduplicate, and resize approved images, then serve them from object storage and a CDN.

### Monitoring

Add structured logging, retry handling, rate-limit protection, and QA dashboards.

## Production recommendation

Move the pipeline to a cloud environment with object storage, a managed PostgreSQL database, queue workers, containerized services, and centralized observability.
