# Token and Cost Report

## Measured token usage

| Subagent           | Avg input tokens | Avg output tokens | Avg total |
| ------------------ | ---------------: | ----------------: | --------: |
| Content + SEO      |               11 |                62 |        73 |
| Image Sourcing     |               11 |                17 |        28 |
| Interlinking / AIO |               11 |                47 |        58 |
| **Total per page** |           **33** |           **126** |   **159** |

## Tokens per page

* **Average tokens per page:** 159

## Extrapolation formula

### Tokens per page

Total tokens per page = input tokens + output tokens

* Input = 33
* Output = 126
* Total = 159

### Tokens for 80,000 pages

Total tokens = 159 × 80,000 = **12,720,000**

### Cost formula

Estimated cost = (Input tokens ÷ 1,000,000 × input price) + (Output tokens ÷ 1,000,000 × output price)

Using a Claude Sonnet assumption:

* Input price = $3 / 1M tokens
* Output price = $15 / 1M tokens

Estimated cost = (2.64 × 3) + (10.08 × 15) = **$159.12 USD**

## Notes

* Actual costs depend on the Claude model selected.
* Caching repeated prompts could reduce costs significantly.
* Image scraping adds network overhead but not LLM token cost.
