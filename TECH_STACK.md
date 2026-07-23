# Implementation Stack

## Language

* Python 3.14

## Libraries

* PyYAML (rules-file parsing)
* python-slugify (slug generation)
* requests (HTTP requests)
* BeautifulSoup4 (HTML parsing / image scraping)

## Architecture

* Single orchestrator script (`orchestrator_full.py`)
* Three sequential subagents
* One assembler script (non-agent)
* Static HTML output

## Agent tooling

* Claude Agent SDK installed via npm (`@anthropic-ai/claude-code`)
* VS Code used as the development environment

## Output

* Static cross-linked HTML pages
* QA reports
* Token/cost reports
* ZIP delivery package
