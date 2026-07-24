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
    print(f"  API calls    : {api_calls}\n")


# ---------------------------------------------------
# Load rules
# ---------------------------------------------------
with open("agent-rules/layer0-rules.yaml", "r", encoding="utf-8") as f:
    rules = yaml.safe_load(f)


# ---------------------------------------------------
# Load events
# ---------------------------------------------------
with open("sample_events.json", "r", encoding="utf-8") as f:
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
Path("outputs").mkdir(exist_ok=True)

print("\n===== FULL MULTI-AGENT PIPELINE =====\n")


# ---------------------------------------------------
# Process every event
# ---------------------------------------------------
for event in events:

    print(f"Processing: {event['name']} ({event['subtype']})\n")

    # -----------------------------
    # Subagent 1
    # -----------------------------
    content = content_agent.generate(event)
    log_agent(
        "Subagent 1 - Content + SEO",
        event,
        content
    )

    # -----------------------------
    # Subagent 2
    # -----------------------------
    image = image_agent.generate(event)
    log_agent(
        "Subagent 2 - Image Sourcing",
        event,
        image,
        api_calls=1
    )

    # -----------------------------
    # Subagent 3
    # -----------------------------
    links = link_agent.generate(event, events)
    log_agent(
        "Subagent 3 - Interlinking / AIO SEO",
        event,
        links
    )

    # -----------------------------
    # Assemble final HTML
    # -----------------------------
    final_html = assembler.assemble(
        content,
        image,
        links
    )

    filename = f"outputs/{event['subtype']}-{event['keyword']}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Generated : {filename}")
    print(f"Slug      : {content['slug']}")
    print("-" * 60)


print("\n===== PIPELINE COMPLETE =====\n")


# ===================================================
# BUILD PROFESSIONAL INDEX PAGE
# ===================================================

cards = ""

for event in events:

    page = f"{event['subtype']}-{event['keyword']}.html"

    cards += f"""
<div class="col-lg-4 col-md-6 mb-4">

<div class="card shadow border-0 h-100">

<div class="card-body">

<span class="badge bg-primary mb-3">
{event['subtype'].title()}
</span>

<h4 class="card-title">
{event['name']}
</h4>

<p class="text-muted">
📍 {event['city']}
</p>

<p>
Explore this generated event landing page.
</p>

<a href="{page}" class="btn btn-primary">
Open Page →
</a>

</div>

</div>

</div>
"""


index_html = f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
name="viewport"
content="width=device-width, initial-scale=1">

<title>
Generated Event Pages
</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">

<style>

body{{
background:#f4f7fb;
font-family:Segoe UI,sans-serif;
}}

.hero{{
background:linear-gradient(135deg,#2563eb,#1d4ed8,#4338ca);
color:white;
padding:90px 20px;
text-align:center;
margin-bottom:60px;
}}

.hero h1{{
font-size:3rem;
font-weight:bold;
}}

.hero p{{
font-size:1.2rem;
opacity:.95;
}}

.card{{
transition:.3s;
border-radius:18px;
}}

.card:hover{{
transform:translateY(-8px);
box-shadow:0 20px 40px rgba(0,0,0,.15);
}}

footer{{
margin-top:80px;
background:#111827;
color:white;
padding:30px;
text-align:center;
}}

</style>

</head>

<body>

<section class="hero">

<div class="container">

<h1>

Multi-Agent Event Pipeline

</h1>

<p>

Automatically Generated Event Landing Pages

</p>

</div>

</section>

<div class="container">

<div class="row">

{cards}

</div>

</div>

<footer>

<p>

Generated using a Multi-Agent Architecture

</p>

<p>

Content Agent • Image Agent • Interlinking Agent • Assembler

</p>

</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>
"""


with open("outputs/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("✓ Professional Bootstrap index page generated.")