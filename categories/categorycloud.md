---
layout: default
---
{%- for category in site.categories -%}
  {{ category[0] | strip_html }}
{% endfor %}
