from slugify import slugify


class ContentSEOAgent:

    def __init__(self, rules):
        self.rules = rules

    def generate(self, event):

        subtype = event["subtype"]

        sections = self.rules["page_sections"][subtype]

        slug = (
            f"/{slugify(event['city'])}"
            f"/{slugify(subtype)}"
            f"/{slugify(event['keyword'])}"
        )

        seo = {
            "title": f"{event['name']} | {event['city']} | Red Giant Events",
            "meta_description": (
                f"Discover everything about {event['name']} in "
                f"{event['city']}. View schedules, venue information, "
                f"registration details and event highlights."
            ),
            "h1": event["name"],
            "canonical_url": f"https://example.com{slug}"
        }

        html = ""

        for section in sections:

            if section == "hero":

                html += f"""
<section id="hero">

<h2>Welcome</h2>

<p>

Join us for <strong>{event['name']}</strong> taking place in
<strong>{event['city']}</strong>.

This page provides everything attendees need including venue
details, schedules, registration information and event highlights.

</p>

<div class="mt-4">

<a href="#registration" class="btn btn-primary me-2">
Register Now
</a>

<a href="#venue" class="btn btn-outline-primary">
View Venue
</a>

</div>

</section>
"""

            elif section == "agenda":

                html += f"""
<section id="agenda">

<h2>Agenda</h2>

<p>

The event agenda includes keynote presentations, breakout
sessions, networking opportunities and panel discussions
designed specifically for attendees.

</p>

</section>
"""

            elif section == "speakers":

                html += f"""
<section id="speakers">

<h2>Featured Speakers</h2>

<p>

Industry experts, innovators and guest speakers will share
their experiences, insights and practical knowledge throughout
the event.

</p>

</section>
"""

            elif section == "lineup":

                html += f"""
<section id="lineup">

<h2>Artist Line-up</h2>

<p>

Enjoy performances from headline artists together with exciting
support acts throughout the event.

</p>

</section>
"""

            elif section == "venue":

                html += f"""
<section id="venue">

<h2>Venue</h2>

<p>

This event will be hosted in {event['city']} at a venue selected
to provide an outstanding attendee experience with excellent
facilities and accessibility.

</p>

</section>
"""

            elif section == "registration":

                html += f"""
<section id="registration">

<h2>Registration</h2>

<p>

Secure your place early by completing your registration before
available slots are filled.

</p>

<a href="#" class="btn btn-success">
Complete Registration
</a>

</section>
"""

            elif section == "tickets":

                html += f"""
<section id="tickets">

<h2>Tickets</h2>

<p>

Purchase tickets online to guarantee entry. Early bird pricing
may be available for a limited period.

</p>

<a href="#" class="btn btn-warning">
Buy Tickets
</a>

</section>
"""

            elif section == "networking":

                html += f"""
<section id="networking">

<h2>Networking</h2>

<p>

Connect with professionals, business leaders and fellow attendees
during dedicated networking sessions.

</p>

</section>
"""

            elif section == "overview":

                html += f"""
<section id="overview">

<h2>Event Overview</h2>

<p>

This event brings together attendees from across the region for
learning, collaboration and memorable experiences.

</p>

</section>
"""

            elif section == "sponsors":

                html += f"""
<section id="sponsors">

<h2>Our Sponsors</h2>

<p>

The event is proudly supported by strategic partners and sponsors
who make the experience possible.

</p>

</section>
"""

            elif section == "parking":

                html += f"""
<section id="parking">

<h2>Parking Information</h2>

<p>

Parking is available near the venue. Guests are encouraged to
arrive early to secure convenient parking.

</p>

</section>
"""

            elif section == "couple_story":

                html += f"""
<section id="couple_story">

<h2>Our Story</h2>

<p>

Celebrate this special occasion by learning more about the couple
and their memorable journey together.

</p>

</section>
"""

            elif section == "schedule":

                html += f"""
<section id="schedule">

<h2>Wedding Schedule</h2>

<p>

The ceremony, reception and celebrations have been carefully
planned to create a memorable experience for everyone attending.

</p>

</section>
"""

            elif section == "accommodation":

                html += f"""
<section id="accommodation">

<h2>Accommodation</h2>

<p>

Recommended hotels and accommodation options are available nearby
for guests travelling from outside the city.

</p>

</section>
"""

            elif section == "rsvp":

                html += f"""
<section id="rsvp">

<h2>RSVP</h2>

<p>

Kindly confirm your attendance before the RSVP deadline.

</p>

<a href="#" class="btn btn-danger">
RSVP Now
</a>

</section>
"""

            elif section == "faqs":

                html += f"""
<section id="faqs">

<h2>Frequently Asked Questions</h2>

<p>

Answers to the most common questions about attendance, parking,
tickets, schedules and venue information.

</p>

</section>
"""

            else:

                html += f"""
<section>

<h2>{section.replace('_',' ').title()}</h2>

<p>

Content generated for the {section} section.

</p>

</section>
"""

        return {

            "slug": slug,

            "seo": seo,

            "html": html,

            "sections": sections

        }