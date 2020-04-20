---
layout: default
title: summer
---

<!-- Begin code @ tags/?/index.md -->

<h1>Posts Tagged with xxy {{ page.title }}</h1>

<div class="tagcloud">

{% capture title %}{{ page.title }}{% endcapture %}

{%- for tags in site.tags -%}
  {%- if tags[0] == title -%}
  <ul>
    {%- for post in tags[1] -%}
      <li><a href="{{ post.url| relative_url }}">{{ post.title }}</a></li>
      <time>{{ post.date | date: "%e %B %Y" }}</time>
    {% endfor %}
  </ul>
  {% endif %}
{%- endfor -%}
</div>

<!-- End code @ tags/?/index.md -->
