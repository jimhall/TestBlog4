---
layout: default
title: Categories
---

<!-- Begin code @ categories/index.md -->

# Category listing

<div class="catcloud">
{%- for category in site.categories -%}
  <a href="#{{ category[0] }}"><h3 style="display:inline;">{{ category[0] }}</h3></a>
{% endfor %}
</div>

<p></p>

<div class="catcloud">
{%- for category in site.categories -%}
  <a name="{{ category[0] }}"><h3>{{ category[0] }}</h3></a>
  <ul>
    {%- for post in category[1] -%}
      <li><a href="{{ post.url| relative_url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
<div>

<!-- End code @ categories/index.md -->
