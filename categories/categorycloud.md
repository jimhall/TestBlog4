---
layout: null
---

{%- for category in site.categories -%}
  {{ category[0] | jsonify }}
{% endfor %}
