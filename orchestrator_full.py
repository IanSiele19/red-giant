import json
import yaml
from pathlib import Path

from subagents.subagent_content_seo import ContentSEOAgent
from subagents.subagent_image_sourcing import ImageSourcingAgent
from subagents.subagent_interlinking import InterlinkingAgent
from subagents.assembler import PageAssembler


# ---------------------------------------------------
# Token/API logging helper
# ---------------------------------------------------
def log_agent(name, input_data, output_data, api_calls=0):
    input_tokens = len(str(input_data).split())
    output_tokens = len(str(output_data).split())

    print(f"[{name}]")
    print(f"  Input tokens : {input_tokens}")
    print(f"  Output tokens: {output_tokens}")
    print(f"  API calls    : {api_calls}\\n")


# ---------------------------------------------------
# Load rules
# ---------------------------------------------------
with open('agent-rules/layer0-rules.yaml', 'r') as f:
    rules = yaml.safe_load(f)


# ---------------------------------------------------
# Load events
# ---------------------------------------------------
with open('sample_events.json', 'r') as f:
    events = json.load(f)


# ---------------------------------------------------
# Initialize agents
# ---------------------------------------------------
content_agent = ContentSEOAgent(rules)
image_agent = ImageSourcingAgent(rules)
link_agent = InterlinkingAgent(rules)
assembler = PageAssembler()


# ---------------------------------------------------
# Ensure output folder exists
# ---------------------------------------------------
Path('outputs').mkdir(exist_ok=True)

print('\\n===== FULL MULTI-AGENT PIPELINE =====\\n')


# ---------------------------------------------------
# Process events
# ---------------------------------------------------
for event in events:

    print(f"Processing: {event['name']} ({event['subtype']})\\n")

    # Subagent 1 — Content + SEO
    content = content_agent.generate(event)
    log_agent('Subagent 1 - Content+SEO', event, content)

    # Subagent 2 — Image sourcing
    image = image_agent.generate(event)
    log_agent('Subagent 2 - Image Sourcing', event, image, api_calls=1)

    # Subagent 3 — Interlinking / AIO SEO
    links = link_agent.generate(event, events)
    log_agent('Subagent 3 - Interlinking/AIO', event, links)

    # Assemble final page
    final_html = assembler.assemble(content, image, links)

    filename = f"outputs/{event['subtype']}-{event['keyword']}.html"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Generated: {filename}")
    print(f"Slug     : {content['slug']}")
    print('-' * 60)


print('\\n===== PIPELINE COMPLETE =====')