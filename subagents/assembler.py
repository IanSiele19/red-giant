class PageAssembler:
    def assemble(self, content, image, links):

        breadcrumb_html = " / ".join(
            [f'<a href="{b["url"]}" class="text-white text-decoration-none">{b["label"]}</a>' for b in links["breadcrumbs"]]
        )

        related_html = "".join(
            [
                f'<a class="list-group-item list-group-item-action" href="{r["slug"]}">{r["name"]}</a>'
                for r in links["related_links"]
            ]
        )

        return f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{content['seo']['title']}</title>

<meta name="description" content="{content['seo']['meta_description']}">

<link rel="canonical" href="{content['seo']['canonical_url']}">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">

<style>

body{{
    font-family:'Segoe UI',sans-serif;
    background:#f5f7fb;
    color:#1f2937;
}}

.navbar{{
    box-shadow:0 3px 15px rgba(0,0,0,.08);
}}

.hero{{
    background:linear-gradient(135deg,#2563eb,#1d4ed8,#4338ca);
    color:white;
    border-radius:20px;
    padding:70px 40px;
    text-align:center;
    margin:40px auto;
}}

.hero h1{{
    font-size:3rem;
    font-weight:700;
}}

.hero p{{
    font-size:1.2rem;
    opacity:.95;
}}

.hero img{{
    margin-top:30px;
    border-radius:18px;
    width:100%;
    max-height:500px;
    object-fit:cover;
    box-shadow:0 10px 30px rgba(0,0,0,.2);
}}

section{{
    background:white;
    padding:35px;
    margin:30px 0;
    border-radius:18px;
    box-shadow:0 5px 20px rgba(0,0,0,.08);
}}

section h2{{
    color:#2563eb;
    margin-bottom:20px;
}}

.list-group-item{{
    border:none;
    margin-bottom:10px;
    border-radius:10px!important;
}}

.list-group-item:hover{{
    background:#2563eb;
    color:white;
}}

footer{{
    background:#111827;
    color:white;
    text-align:center;
    padding:40px;
    margin-top:60px;
}}

footer a{{
    color:#93c5fd;
    text-decoration:none;
    margin:0 12px;
}}

@keyframes fadeUp{{
from{{
opacity:0;
transform:translateY(25px);
}}
to{{
opacity:1;
transform:translateY(0);
}}
}}

.hero,
section{{
animation:fadeUp .7s ease;
}}

</style>

</head>

<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">

<div class="container">

<a class="navbar-brand fw-bold" href="index.html">
Red Giant Events
</a>

<div class="ms-auto">

{breadcrumb_html}

</div>

</div>

</nav>

<div class="container">

<div class="hero">

<h1>{content['seo']['h1']}</h1>

<p class="lead">
{content['seo']['meta_description']}
</p>

<div class="mt-4 mb-4">

<a href="#registration" class="btn btn-light btn-lg px-5">

Register Now

</a>

</div>

<img
src="{image['selected_image']}"
alt="{image['alt_text']}"
class="img-fluid">

</div>

{content['html']}

<section id="related-events">

<h2>Related Events</h2>

<div class="list-group">

{related_html}

</div>

</section>

</div>

<footer>

<p class="mb-2">
© 2026 Event Pipeline Prototype
</p>

<p>

Generated using a multi-agent orchestration pipeline.

</p>

<div class="mt-3">

<a href="index.html">
Home
</a>

<a href="#">
Events
</a>

<a href="#">
Contact
</a>

</div>

</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>
"""