---
layout: default
title: summer
---

<!-- Begin code @ tags/summer/index.md -->

<h1>Posts Tagged with {{ page.title }}</h1>

<div class="tagcloud">
{%- for tags in site.tags -%}
  {%- if tags[0] == 'summer' -%}
<!--  <a name="{{ tags[0] }}"><h3>{{ tags[0] }}</h3></a> -->
  <ul>
    {%- for post in tags[1] -%}
      <li><a href="{{ post.url| relative_url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
  {% endif %}
{% endfor %}
</div>

<!-- End code @ tags/summer/index.md -->
