from __future__ import annotations

SITE_NAME = 'Cessnock Motor Cycle Club'
SITE_DESCRIPTION = (
    'A family-friendly off road motorcycle club in the Hunter Valley, '
    'focused on safe, welcoming enduro-style events for riders of all ages.'
)
NAV_ITEMS = [
    {'label': 'Home', 'slug': ''},
    {'label': 'About', 'slug': 'about'},
    {'label': 'News', 'slug': 'news'},
    {'label': 'Events', 'slug': 'events'},
    {'label': 'Get involved', 'slug': 'get-involved'},
    {'label': 'Membership', 'slug': 'membership'},
    {'label': 'Gallery', 'slug': 'gallery'},
    {'label': 'Sponsors', 'slug': 'sponsors'},
    {'label': 'Archive', 'slug': 'archive'},
    {'label': 'Contact', 'slug': 'contact'},
]

FOOTER_LINKS = [
    {'label': 'Club officials', 'href': 'officials', 'external': False},
    {'label': 'Meetings', 'href': 'meetings', 'external': False},
    {'label': 'Remembrance', 'href': 'remembrance', 'external': False},
    {'label': 'Facebook', 'href': 'https://www.facebook.com/cessnockmotorcycleclub/', 'external': True},
    {'label': 'YouTube', 'href': 'https://www.youtube.com/user/cessnockmcc/', 'external': True},
    {'label': 'Email us', 'href': 'mailto:info@cessnockmcc.com.au', 'external': True},
]

PAGES = [
    {
        'slug': '',
        'title': 'Welcome to Cessnock Motor Cycle Club',
        'eyebrow': 'Hunter Valley off road motorcycle club',
        'intro': 'Family-friendly riding, volunteer-led events, and a strong enduro culture for juniors, social riders, and serious racers alike.',
        'description': SITE_DESCRIPTION,
        'body_class': 'hero-home',
        'content': '''
<section class="grid two-up">
  <article class="card media-card">
    <img class="media-image media-tall" src="/assets/media/home-hero.jpg" alt="Cessnock Motor Cycle Club homepage slide from the legacy site">
  </article>
  <article class="card media-card">
    <div class="video-frame">
      <iframe src="https://www.youtube.com/embed/d5CjbK55g7A?rel=0" title="Cessnock Motor Cycle Club video" loading="lazy" allowfullscreen></iframe>
    </div>
  </article>
</section>
<section class="grid two-up">
  <article class="card card-feature">
    <h2>What the club is about</h2>
    <p>Cessnock Motor Cycle Club focuses on safe, enjoyable off road events for juniors from 85cc big wheels through to experienced riders in senior classes. The club culture is welcoming, community-minded, and built around helping riders improve while still keeping a competitive edge for those who want to race hard.</p>
    <p>Across the year the club hosts and supports enduro, enduro sprint, grass track, cross country, pony express, motocross, dirt track, trials, social rides, and junior coaching.</p>
  </article>
  <aside class="card card-accent">
    <h2>Quick links</h2>
    <ul class="link-list">
      <li><a href="membership/">Join the club via Ridernet</a></li>
      <li><a href="events/">Browse club events</a></li>
      <li><a href="news/">Read the latest news</a></li>
      <li><a href="get-involved/">Volunteer at working bees and race days</a></li>
    </ul>
  </aside>
</section>
<section class="grid thirds">
  <article class="card media-card">
    <img class="media-image" src="/assets/media/home-membership.jpg" alt="Membership tile from the legacy site">
    <h2>Membership</h2>
    <p>Membership gives riders access to club events, inclusion in the club championship, and the ability to obtain an MNSW race licence through an affiliated club.</p>
    <p><a class="button" href="membership/">Membership details</a></p>
  </article>
  <article class="card media-card">
    <img class="media-image" src="/assets/media/home-events.jpg" alt="Events tile from the legacy site">
    <h2>Meetings</h2>
    <p>General meetings are held at 7pm on the first Tuesday of every other month (Feb, Apr, Jun, Aug, Oct, Dec) at the Khartoum Hotel in Kitchener. New faces are always welcome.</p>
    <p><a class="button button-secondary" href="meetings/">Meeting info</a></p>
  </article>
  <article class="card media-card">
    <img class="media-image" src="/assets/media/home-contact.jpg" alt="Contact tile from the legacy site">
    <h2>Follow the club</h2>
    <p>For current updates, race announcements, and community news, the club's Facebook page remains the best public channel.</p>
    <p><a class="button button-secondary" href="https://www.facebook.com/cessnockmotorcycleclub/">Visit Facebook</a></p>
  </article>
</section>
'''.strip(),
    },
    {
        'slug': 'about',
        'title': 'About the club',
        'eyebrow': 'About Cessnock MCC',
        'intro': 'A welcoming club with deep local roots, volunteer energy, and a strong off road racing tradition.',
        'description': 'About the history, purpose, and supporting information for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card prose">
  <p>The existing club website describes Cessnock Motor Cycle Club as a place where knowledge, history, and community all come together. The club has long balanced family-friendly participation with serious racing, and it continues to rely on passionate members and volunteers to keep events running.</p>
  <p>This rebuild keeps the public information that matters most and makes it easier to maintain. For detailed committee, meeting, and memorial information, use the links below.</p>
</section>
<section class="card media-card">
  <img class="media-image" src="/assets/media/gallery-general.jpg" alt="General club photo from the legacy photo gallery">
</section>
<section class="grid thirds">
  <article class="card">
    <h2>Club officials</h2>
    <p>Meet the committee roles carried over from the current public site.</p>
    <p><a class="button button-secondary" href="../officials/">View officials</a></p>
  </article>
  <article class="card">
    <h2>Club constitution</h2>
    <p>A plain-language summary of the constitution content published on the existing site.</p>
    <p><a class="button button-secondary" href="../constitution/">Read summary</a></p>
  </article>
  <article class="card">
    <h2>Remembrance</h2>
    <p>A tribute to John Hall and his impact on the club and the wider riding community.</p>
    <p><a class="button button-secondary" href="../remembrance/">Read tribute</a></p>
  </article>
</section>
'''.strip(),
    },
    {
        'slug': 'officials',
        'title': 'Club officials',
        'eyebrow': 'Executive committee',
        'intro': "Committee roles published on the club's existing public website.",
        'description': 'Executive committee listing for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card">
  <div class="split-list">
    <div>
      <h2>Office bearers</h2>
      <ul class="detail-list">
        <li><strong>President:</strong> David Blake</li>
        <li><strong>Vice President:</strong> Jason Chapman</li>
        <li><strong>Race Secretary:</strong> Matthew Vogt</li>
        <li><strong>Treasurer:</strong> Glen Toner</li>
        <li><strong>Equipment Steward:</strong> Dave Cocking</li>
        <li><strong>Public Officer:</strong> David Blake</li>
        <li><strong>Publicity Officer:</strong> Steven Parish</li>
      </ul>
    </div>
    <div>
      <h2>Need the latest contacts?</h2>
      <p>Committee roles can change over time. If you are making an enquiry about events, volunteering, sponsorship, or membership, the safest contact point is the club email.</p>
      <p><a class="button" href="mailto:info@cessnockmcc.com.au">Email the club</a></p>
    </div>
  </div>
</section>
'''.strip(),
    },
    {
        'slug': 'constitution',
        'title': 'Club constitution summary',
        'eyebrow': 'Governance and membership',
        'intro': 'A concise summary of the constitution text published on the legacy website.',
        'description': 'Summary of the constitution content published for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card prose">
  <p>The current website publishes a full incorporated association constitution covering membership, committee responsibilities, meetings, voting, disputes, insurance, funds, and record keeping. Rather than reproducing a long block of legacy legal text here, this version keeps the core points easy to scan.</p>
  <p><a class="button" href="../assets/docs/club-constitution.pdf">Download constitution PDF</a></p>
  <h2>Highlights from the published constitution</h2>
  <ul>
    <li>Membership is approved by the committee after nomination and payment of applicable fees.</li>
    <li>Members may resign, be suspended, or be expelled under the rules set out in the constitution.</li>
    <li>The committee manages the affairs of the association and includes the president, vice-president, treasurer, secretary, and ordinary committee members.</li>
    <li>Annual general meetings and special general meetings are governed by notice, quorum, voting, and adjournment requirements.</li>
    <li>The constitution also covers disputes, insurance, the management of funds, the custody of books, and the service of notices.</li>
  </ul>
  <p>If you need the official current version of the constitution for governance or compliance purposes, please request it directly from the club committee.</p>
  <p><a class="button" href="mailto:info@cessnockmcc.com.au?subject=Constitution%20request">Request the constitution</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'gallery',
        'title': 'Gallery',
        'eyebrow': 'Photo archive',
        'intro': 'A preserved set of public club images copied from the legacy site photo gallery and related public pages.',
        'description': 'Historic public photo gallery preserved from the legacy Cessnock Motor Cycle Club website.',
        'content': '''
<section class="card prose">
  <p>This gallery preserves the public photo images exposed on the legacy site during the migration. It gives the new static build a place to retain that visual history even without the original dynamic gallery system.</p>
</section>
<section class="gallery-grid">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-01.jpg" alt="Historic club gallery image 1">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-02.jpg" alt="Historic club gallery image 2">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-03.jpg" alt="Historic club gallery image 3">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-04.jpg" alt="Historic club gallery image 4">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-05.jpg" alt="Historic club gallery image 5">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-06.jpg" alt="Historic club gallery image 6">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-07.jpg" alt="Historic club gallery image 7">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-08.jpg" alt="Historic club gallery image 8">
</section>
<section class="card prose">
  <h2>Other preserved files</h2>
  <ul>
    <li><a href="../assets/docs/club-constitution.pdf">Club constitution PDF</a></li>
    <li><a href="../assets/legacy-sweep/postie-gp-2015.jpg">Postie GP 2015 image</a></li>
    <li><a href="../assets/legacy-sweep/aus-gp-postie-tile.jpg">Aus GP Postie tile image</a></li>
  </ul>
</section>
'''.strip(),
    },
    {
        'slug': 'meetings',
        'title': 'Club meetings',
        'eyebrow': 'Bi-monthly catch-up',
        'intro': 'The club welcomes members and interested locals to attend and help shape the season ahead.',
        'description': 'Meeting time and location for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card prose">
  <p>Cessnock Motor Cycle Club holds general meetings at <strong>7:00pm on the first Tuesday of every other month (Feb, Apr, Jun, Aug, Oct, Dec)</strong> at the <strong>Khartoum Hotel, Kitchener</strong>.</p>
  <p>The club's annual general meeting is held in December. Anyone interested in the club is welcome to attend, contribute ideas, and help support the future of local off road riding.</p>
  <p>Memberships are available online, and meetings are a great place to learn how to get involved with events, volunteering, and club life.</p>
  <p><a class="button" href="../membership/">View membership information</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'remembrance',
        'title': 'Remembrance',
        'eyebrow': 'In memory of John Hall',
        'intro': "A tribute carried over from the legacy site, reflecting on John Hall's leadership, generosity, and influence.",
        'description': 'Memorial tribute to John Hall from the Cessnock Motor Cycle Club community.',
        'content': '''
<section class="card prose">
  <p>The original club website includes a moving tribute written by life member Glenn "Crasha" Toner about John Hall. Rather than listing dates and achievements alone, the piece speaks about how John carried himself: calm under pressure, deeply knowledgeable, generous with his time, and respected by everyone around him.</p>
  <p>It remembers the energy around the 1992 International Six Days Enduro campaign in Cessnock, the Monday night planning meetings at the fire station, and the way John brought clarity and confidence whenever questions arose. The tribute also captures the personal side of his legacy: the race stories, the practical advice, and the sense that he was always willing to help riders and events be better.</p>
  <p>For those who knew him, the page remains a reminder of a rider, organiser, mentor, and friend whose influence went well beyond one event or one club role.</p>
</section>
'''.strip(),
    },
    {
        'slug': 'get-involved',
        'title': 'Get involved',
        'eyebrow': 'The club runs on volunteers',
        'intro': 'From working bees to race-day jobs, members and families keep the calendar alive.',
        'description': 'Ways to join, volunteer, and support events at Cessnock Motor Cycle Club.',
        'content': '''
<section class="grid two-up">
  <article class="card prose">
    <h2>Why get involved?</h2>
    <p>The club encourages prospective members and their families to join in and support one of the Hunter Valley's leading off road motorcycle communities. The environment is designed to help junior members and novice riders build skills safely, while still giving competitive riders a full calendar of events to enjoy.</p>
    <p>The strength of the club comes from a passionate member base. Meetings, working bees, track prep, race administration, scoring, marshalling, catering, and scrutineering all depend on volunteers giving some of their time.</p>
  </article>
  <article class="card">
    <h2>Ways to help</h2>
    <ul class="detail-list">
      <li>Attend bi-monthly meetings and contribute ideas.</li>
      <li>Help at working bees before club events.</li>
      <li>Volunteer on race day as a marshal, scorer, or support crew member.</li>
      <li>Work toward becoming an official for club-level and higher events.</li>
    </ul>
  </article>
</section>
<section class="card prose">
  <h2>Officials and accreditation</h2>
  <p>The legacy site highlights the importance of qualified officials such as race secretaries, race stewards, scrutineers, and clerks of course. Without these roles, events do not run. If you are interested in becoming an official, the first step is normally completing the general seminar and then progressing through the relevant accreditation pathway with Motorcycling NSW.</p>
  <p><a class="button" href="mailto:info@cessnockmcc.com.au?subject=I%20want%20to%20help">Volunteer with the club</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'membership',
        'title': 'Membership',
        'eyebrow': 'Join the club',
        'intro': 'Simple pricing, affiliated racing access, and a welcoming local club community.',
        'description': 'Membership information and pricing for Cessnock Motor Cycle Club.',
        'content': '''
<section class="grid two-up">
  <article class="card prose">
    <h2>What membership gives you</h2>
    <ul>
      <li>Access to club events including race days, social rides, and inter-club events.</li>
      <li>Inclusion in the annual club championship.</li>
      <li>The ability to obtain an MNSW race licence through an affiliated club.</li>
    </ul>
  </article>
  <article class="card card-accent">
    <h2>Published prices</h2>
    <ul class="detail-list">
      <li><strong>Single membership:</strong> $30.00 per year</li>
      <li><strong>Family membership:</strong> $50.00 per year for up to 6 family members</li>
    </ul>
  </article>
</section>
<section class="card prose">
  <h2>How to join</h2>
  <p>The legacy site directs new members to the Motorcycling NSW Ridernet system. When completing the form, choose <strong>Cessnock Motor Cycle Club</strong> from the club list.</p>
  <p><a class="button" href="https://ridernet.com.au/member/index.cfm?p=register">Join via Ridernet</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'sponsors',
        'title': 'Sponsors',
        'eyebrow': 'Support the businesses that support the club',
        'intro': 'Community events are made possible by sponsors who back local riding and local volunteers.',
        'description': 'Sponsor acknowledgement page for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card prose">
  <p>Cessnock Motor Cycle Club thanks all of the sponsors who have supported the club over the years. The original site encourages members and visitors to support those businesses in return and recognise the role they play in keeping grassroots motorcycle sport strong in the region.</p>
  <h2>Featured sponsor from the legacy site</h2>
  <div class="media-inline">
    <img class="media-logo" src="/assets/media/sponsor-greenslipcalculator.jpg" alt="GreenSlipCalculator.com.au logo">
    <p><strong>GreenSlipCalculator.com.au</strong> was highlighted as a club sponsor, helping Australians compare greenslip prices, products, services, and insurers online.</p>
  </div>
  <p><a class="button button-secondary" href="http://greenslipcalculator.com.au/">Visit sponsor website</a></p>
</section>
<section class="card media-card">
  <img class="media-image" src="/assets/media/sponsor-khartoum-hotel.jpeg" alt="Khartoum Hotel sponsor image from the legacy site">
</section>
<section class="card prose">
  <h2>Interested in sponsoring the club?</h2>
  <p>If you would like to support the club, its events, or junior and community participation in off road motorcycling, get in touch with the committee.</p>
  <p><a class="button" href="mailto:info@cessnockmcc.com.au?subject=Sponsorship%20enquiry">Sponsorship enquiry</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'archive',
        'title': 'Archive',
        'eyebrow': 'Public highlights from the legacy site',
        'intro': 'A simplified archive for notable public events and historical content worth keeping.',
        'description': 'Archive of notable public content from the legacy Cessnock Motor Cycle Club website.',
        'content': '''
<section class="grid two-up">
  <article class="card media-card">
    <img class="media-image" src="/assets/media/gallery-general.jpg" alt="General club gallery image">
    <h2>Australian Four Day Enduro 2018</h2>
    <p>The legacy event listing notes the 40th anniversary edition of the Australian 4 Day Enduro, returning to Cessnock where it all started.</p>
    <p><a class="button button-secondary" href="a4de-2018/">Open archive page</a></p>
  </article>
  <article class="card media-card">
    <img class="media-image" src="/assets/media/postie-gp-hero.jpg" alt="Australian Postie Bike GP 2019 event image">
    <h2>Australian Postie Bike GP 2019</h2>
    <p>A family-friendly street event in the Cessnock CBD featuring team racing on Honda CT110 Postie Bikes.</p>
    <p><a class="button button-secondary" href="postie-bike-gp-2019/">Open archive page</a></p>
  </article>
</section>
<section class="card prose">
  <h2>Looking for current event updates?</h2>
  <p>The old website used dynamic news and events modules. For a simplified static setup, it makes more sense to keep major historical items here and use social channels or a future editable content workflow for up-to-date event announcements.</p>
  <p><a class="button" href="https://www.facebook.com/cessnockmotorcycleclub/">Follow updates on Facebook</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'archive/a4de-2018',
        'title': 'Australian Four Day Enduro 2018',
        'eyebrow': 'Archive item',
        'intro': 'A preserved summary of the public event listing from the legacy site.',
        'description': 'Archive summary for the 2018 Australian Four Day Enduro listing.',
        'content': '''
<section class="card prose">
  <p>The legacy site records this event as the <strong>40th anniversary edition of the Australian 4 Day Enduro</strong>, returning to Cessnock where the event began.</p>
  <img class="media-image" src="/assets/media/gallery-general.jpg" alt="General club image used as an archive illustration">
  <ul>
    <li><strong>Dates:</strong> 3 April 2018 to 7 April 2018</li>
    <li><strong>Location:</strong> Cessnock Showground</li>
  </ul>
  <p>This page is kept as a historical reference within the simplified static rebuild.</p>
  <p><a class="button button-secondary" href="../">Back to archive</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'archive/postie-bike-gp-2019',
        'title': 'Australian Postie Bike GP 2019',
        'eyebrow': 'Archive item',
        'intro': "A preserved summary of one of the club's standout public event pages.",
        'description': 'Archive summary for the 2019 Australian Postie Bike GP.',
        'content': '''
<section class="card prose">
  <img class="media-image" src="/assets/media/postie-gp-hero.jpg" alt="Australian Postie Bike GP 2019 banner image">
  <p>The Australian Postie Bike GP was presented as a family-friendly team race held on closed streets around the Cessnock CBD. By 2019 the event was in its sixth year and had built a strong profile with local riders, first-timers, and well-known names from the motorcycle community.</p>
  <div class="media-inline">
    <img class="media-logo" src="/assets/media/postie-gp-mitsubishi-logo.png" alt="Cessnock Mitsubishi sponsor logo">
    <p>The original page prominently thanked Cessnock Mitsubishi as the major sponsor for the 2019 event, alongside the public race information and course details.</p>
  </div>
  <h2>Key details from the legacy page</h2>
  <ul>
    <li><strong>Sign on and scrutineering:</strong> Saturday 9 November 2019</li>
    <li><strong>Race day:</strong> Sunday 10 November 2019</li>
    <li><strong>Format:</strong> Two-rider teams on Honda CT110 Postie Bikes with pit crew support</li>
    <li><strong>Course:</strong> A street circuit through central Cessnock and the TAFE precinct</li>
  </ul>
  <img class="media-image" src="/assets/media/postie-gp-course-layout.png" alt="Australian Postie Bike GP course layout">
  <p>The original page also outlined qualifying, the Cessnock Cup, a women's race, the main endurance-format GP, and recognition for major sponsor Cessnock Mitsubishi.</p>
  <p><a class="button button-secondary" href="../">Back to archive</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'contact',
        'title': 'Contact the club',
        'eyebrow': 'Get in touch',
        'intro': 'For membership, events, sponsorship, or general enquiries, start with the club email.',
        'description': 'Contact details for Cessnock Motor Cycle Club.',
        'content': '''
<section class="grid two-up">
  <article class="card prose">
    <h2>Postal address</h2>
    <p>
      Cessnock Motorcycle Club<br>
      PO Box 287<br>
      Cessnock NSW 2325
    </p>
  </article>
  <article class="card prose">
    <h2>Email</h2>
    <p><a href="mailto:info@cessnockmcc.com.au">info@cessnockmcc.com.au</a></p>
    <p>The club is volunteer-run, so responses may not be instant. Thanks in advance for your patience.</p>
  </article>
</section>
<section class="card prose">
  <h2>Social channels</h2>
  <p>For general updates and public-facing club activity, you can also follow the club on Facebook or YouTube.</p>
  <ul class="detail-list">
    <li><a href="https://www.facebook.com/cessnockmotorcycleclub/">Facebook</a></li>
    <li><a href="https://www.youtube.com/user/cessnockmcc/">YouTube</a></li>
  </ul>
</section>
'''.strip(),
    },
]
