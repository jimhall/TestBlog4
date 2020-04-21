---
layout: default
title: Tags
---

<!-- Begin code @ tags/index.md -->

# Category listing

<div class="catcloud">
{%- for tag in site.tags -%}
<!--  <a href="#{{ tag[0] }}"><h3 style="display:inline;">{{ tag[0] }}</h3></a> -->
  <a href="{{ tag[0] | prepend: 'tags/' | relative_url }}"><h3 style="display:inline;">{{ tag[0] }}</h3></a>
{% endfor %}
</div>

<p></p>

<div class="catcloud">
{%- for tag in site.tags -%}
<!--  <a name="{{ tag[0] }}"><h3>{{ tag[0] }}</h3></a> -->
  <a href="{{ tag[0] | prepend: 'tags/' | relative_url }}"><h3>{{ tag[0] }}</h3></a>
  <ul>
    {%- for post in tag[1] -%}
      <li><a href="{{ post.url| relative_url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
<div>

<!-- End code @ tags/index.md -->
