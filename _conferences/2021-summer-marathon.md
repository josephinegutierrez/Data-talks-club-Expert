---

title: DataTalks.Club Conference &ndash; 2021 Summer Marathon 
description:
  DataTalks.Club 2021 Summer Marathon &ndash; two weeks of awesomness.
image: images/other/conference-2021-feb-cover.jpg
layout: page

tracks:
  - name: Career in Data
    eventbrite: 153177531119
    youtube: NA
    talks:
      - speaker: svpino
        name: "Transitioning from Software Engineering to Machine Learning"
        date: 2021-06-14 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
      - speaker: dalianaliu
        name: "The Next Level of Your Data Science Career"
        date: 2021-06-15 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
      - speaker: andreaskretz
        name: "Build Your Own Data Pipeline"
        date: 2021-06-16 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
      - speaker: roksolanadiachuk
        name: Difference between big data engineer job and data science job
        date: 2021-06-17 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
      - speaker: elenasamuylova
        name: "I Want to Build a Machine Learning Startup!"
        date: 2021-06-18 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
  - name: Machine Learning in Production
    eventbrite: 153178006541
    youtube: NA
    talks:
      - speaker: janzawadzki
        name: "Something Awesome from Jan (TBA)"
        date: 2021-06-21 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
      - speaker: benwilson
        name: "Simplicity is the key to keeping your models running in production"
        date: 2021-06-22 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
      - speaker: linaweichbrodt
        name: "Something Awesome from Lina (TBA)"
        date: 2021-06-23 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
      - speaker: dougturnbull
        name: "Something Awesome from Doug (TBA)"
        date: 2021-06-24 17:00:00
        eventbrine: TBA
        abstract:
          TBA.
      - speaker: fabianaclemente
        name: "Something Awesome from Fabiana (TBA)"
        date: 2021-06-25 17:00:00
        eventbrine: TBA
        abstract:
          TBA.


partners:
  - name: O'Reilly Media
    link: https://www.oreilly.com/
    image: "/images/partners/oreilly.jpg"
  - name: MLOps.community
    link: https://mlops.community/
    image: "/images/partners/mlops-community.jpg"

---


### DataTalks.Club 2021 Summer Marathon

* Two weeks of awesomness
* It's online and entirely free!
* Time is in CET (UTC +1)
* Can't attend? Register anyways, we will send you the recordings.


<h2>Tracks</h2>

<ul>
{% for track in page.tracks %}
  <li>
    <a href="#{{ track.name | slugify }}">{{ track.name}}</a>
  </li>
{% endfor %}
</ul>

{% for track in page.tracks %}
<h2 id="{{ track.name | slugify }}">{{ track.name}}</h2>

<div class="conference-talks">
{% for talk in track.talks %}
  {% assign speaker = site.people | where: "short", talk.speaker | first %}
  <div class="talk-wrap d-flex">
    <div class="talk-speaker-img-container">
      <img class="talk-speaker-img" src="/{{speaker.picture}}" />
    </div>
    <div class="talk-details">
      <span class="datetime">{{ talk.date | date: "%A, %d %B at %H:%M" }} CET</span>
      <h2>{{talk.name}}</h2>
      <h3 class="speaker-name">— <a href="/people/{{talk.speaker}}.html" target="_blank">{{ speaker.title }}</a></h3>
      <span class="toggle-abscract"><a href="javascript:void();" onclick="toggle('{{ talk.name | slugify }}')">Show abstract</a></span>
      <div class="talk-absctract" id="{{ talk.name | slugify }}" style="display: none;">{{ talk.abstract }}</div>
    </div>
  </div>
{% endfor %}
</div>

<center class="my-3">
<button class="btn btn-secondary btn-lg" id="eventbrite-widget-modal-trigger-{{ track.eventbrite }}" type="button">
  <i class="fas fa-check"></i> Register
</button>
</center>

{% endfor %}



<script src="https://www.eventbrite.com/static/widgets/eb_widgets.js"></script>

<script type="text/javascript">
  var exampleCallback = function() {
      console.log('Order complete!');
  };

  {% for track in page.tracks %}
  window.EBWidgets.createWidget({
      widgetType: 'checkout',
      eventId: '{{ track.eventbrite }}',
      modal: true,
      modalTriggerElementId: 'eventbrite-widget-modal-trigger-{{ track.eventbrite }}',
      onOrderComplete: exampleCallback
  });
  {% endfor %}

  function toggle(name) {
    var x = document.getElementById(name);
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }
</script>