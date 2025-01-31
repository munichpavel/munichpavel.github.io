---
layout: archive
title: "Paul's blog posts"
permalink: /posts/
entries_layout: list
---

{% for post in site.posts %}
  - [{{ post.title }}]({{ post.url }}) ({{ post.date | date: "%Y-%m-%d"}})
{% endfor %}