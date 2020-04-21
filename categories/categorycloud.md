---
layout: null
---

{{ site.categories | jsonify }}

{%- for category in site.categories -%}
  {{ category[0] | jsonify }}
{% endfor %}
