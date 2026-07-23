class PageAssembler:
    def assemble(self, content, image, links):

        breadcrumb_html = ' / '.join(
            [f'<a href="{b["url"]}">{b["label"]}</a>' for b in links['breadcrumbs']]
        )

        related_html = ''.join(
            [f'<li><a href="{r["slug"]}">{r["name"]}</a></li>' for r in links['related_links']]
        )

        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{content['seo']['title']}</title>
  <meta name="description" content="{content['seo']['meta_description']}">
  <link rel="canonical" href="{content['seo']['canonical_url']}">

  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #f5f7fb;
      color: #1f2937;
      line-height: 1.7;
    }}

    .container {{
      width: 90%;
      max-width: 1100px;
      margin: auto;
      padding: 2rem 0;
    }}

    nav {{
      background: #ffffff;
      padding: 1rem 2rem;
      border-bottom: 1px solid #e5e7eb;
      font-size: 0.95rem;
    }}

    nav a {{
      color: #2563eb;
      text-decoration: none;
      font-weight: 500;
    }}

    .hero {{
      background: linear-gradient(135deg, #2563eb, #1e40af);
      color: white;
      padding: 4rem 2rem;
      border-radius: 20px;
      margin: 2rem 0;
      text-align: center;
      box-shadow: 0 10px 30px rgba(37, 99, 235, 0.25);
    }}

    .hero h1 {{
      font-size: 2.8rem;
      margin-bottom: 1rem;
    }}

    .hero p {{
      font-size: 1.1rem;
      opacity: 0.95;
    }}

    .hero img {{
      width: 100%;
      max-height: 500px;
      object-fit: cover;
      border-radius: 16px;
      margin-top: 2rem;
      border: 4px solid rgba(255,255,255,0.2);
    }}

    section {{
      background: #ffffff;
      margin: 1.5rem 0;
      padding: 2rem;
      border-radius: 18px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
      border: 1px solid #eef2f7;
    }}

    section h2 {{
      color: #111827;
      margin-bottom: 1rem;
      font-size: 1.5rem;
      border-left: 5px solid #2563eb;
      padding-left: 0.8rem;
    }}

    #related-events ul {{
      list-style: none;
      padding-left: 0;
    }}

    #related-events li {{
      margin: 0.7rem 0;
      padding: 0.8rem 1rem;
      background: #f8fafc;
      border-radius: 10px;
      border: 1px solid #e5e7eb;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}

    #related-events li:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    }}

    a {{
      color: #2563eb;
      text-decoration: none;
      font-weight: 500;
    }}

    a:hover {{
      text-decoration: underline;
    }}

    footer {{
      background: #0f172a;
      color: #e5e7eb;
      text-align: center;
      padding: 2rem;
      margin-top: 3rem;
    }}

    footer a {{
      color: #93c5fd;
      margin: 0 0.6rem;
    }}

    @media (max-width: 768px) {{
      .hero h1 {{
        font-size: 2rem;
      }}

      section {{
        padding: 1.4rem;
      }}
    }}
  </style>
</head>

<body>

  <nav>{breadcrumb_html}</nav>

  <div class="container">

    <div class="hero">
      <h1>{content['seo']['h1']}</h1>
      <p>{content['seo']['meta_description']}</p>

      <img src="{image['selected_image']}" alt="{image['alt_text']}">
    </div>

    {content['html']}

    <section id="related-events">
      <h2>Related Events</h2>
      <ul>{related_html}</ul>
    </section>

  </div>

  <footer>
    <p>&copy; 2026 Event Pipeline Prototype</p>
    <div style="margin-top: 0.5rem;">
      <a href="/events">All Events</a>
      <a href="/contact">Contact</a>
    </div>
  </footer>

</body>
</html>
'''