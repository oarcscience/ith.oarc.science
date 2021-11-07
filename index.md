---
layout: seclanding
title: "Intangible Textual Heritage Archive"
---
W**elcome to the largest freely available archive** of online books
about religion, mythology, folklore and the esoteric on the Internet.
The site is dedicated to religious tolerance and scholarship, and has
the largest readership of any similar site on the web.

<div class="row">

{% for elem in site.data.toplevellinks %} {% assign dataline =
site.data.nav \| where: "name", elem.name \| first %}

<div
class="col2 {% assign residue = forloop.index | modulo:6 %}{% if residue==0%}last{% endif%}">

<a href="%7B%7Bdataline.link%7D%7D" class="tile"><span class="tile-teaser"><em></em></span> <span class="tile-title">{{dataline.name}}</span></a>

</div>

{% endfor %}

</div>

<div class="row">

<div class="col4">

<a href="https://help.passbolt.com/faq/discover" class="tile"><span class="tile-teaser"><em></em></span> <span class="tile-title">Get started using passbolt</span> <span class="tile-description">Frequently asked questions during first time use.</span></a>

</div>

<div class="col4">

<a href="https://help.passbolt.com/faq/start/browser-extensions" class="tile"><span class="tile-teaser"><em></em></span> <span class="tile-title">Browser extension</span> <span class="tile-description">How to install and remove the browser extensions.</span></a>

</div>

<div class="col4 last">

<a href="https://help.passbolt.com/faq/start/create-edit-delete-password" class="tile"><span class="tile-teaser"><em></em></span> <span class="tile-title">Password basics</span> <span class="tile-description">Creating, editing, sharing and deleting passwords</span></a>

</div>

<div class="col4">

<a href="https://help.passbolt.com/faq/start/share-password" class="tile"><span class="tile-teaser"><em></em></span> <span class="tile-title">Sharing passwords</span> <span class="tile-description">Sharing is caring (but only if you really have to).</span></a>

</div>

<div class="col4">

<a href="https://community.passbolt.com" class="tile"><span class="tile-teaser"><em></em></span> <span class="tile-title">Forum</span> <span class="tile-description">When in doubt, you can also ask the community!</span></a>

</div>

</div>
