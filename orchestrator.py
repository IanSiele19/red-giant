import json
import yaml
from pathlib import Path

from subagents.subagent_content_seo import ContentSEOAgent


# ---------------------------------------------------
# Validate generated output against rules file
# ---------------------------------------------------
def validate_rules(result, rules):
    required = rules['seo_fields']['required']

    # Check required SEO fields
    for field in required:
        if field not in result['seo']:
            raise ValueError(f'Missing SEO field: {field}')

    # Check sections exist
    if len(result['sections']) == 0:
        raise ValueError('No sections generated')


# ---------------------------------------------------
# Load rules
# ---------------------------------------------------
with open('agent-rules/layer0-rules.yaml', 'r') as f:
    rules = yaml.safe_load(f)


# ---------------------------------------------------
# Initialize Subagent 1 (Content + SEO)
# ---------------------------------------------------
agent = ContentSEOAgent(rules)


# ---------------------------------------------------
# Load sample events
# ---------------------------------------------------
with open('sample_events.json', 'r') as f:
    events = json.load(f)


# ---------------------------------------------------
# Ensure output directory exists
# ---------------------------------------------------
Path('outputs').mkdir(exist_ok=True)

print('\\n=== ORCHESTRATOR STARTED ===\\n')


# ---------------------------------------------------
# Process each event
# ---------------------------------------------------
for event in events:

    # Generate content + SEO
    result = agent.generate(event)

    # Validate against Layer 0 rules
    validate_rules(result, rules)

    # Output filename
    filename = f'outputs/{event["subtype"]}-{event["keyword"]}.html'

    # Write HTML file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(result['html'])

    # Console log
    print(f'Event: {event["name"]}')
    print(f'Subtype: {event["subtype"]}')
    print(f'Slug: {result["slug"]}')
    print(f'Sections: {", ".join(result["sections"])}')
    print(f'Output: {filename}\\n')


print('=== PIPELINE COMPLETE ===')