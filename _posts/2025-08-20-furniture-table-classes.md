---
title: "GenAI brain-sneeze of the day: is a table of data really furniture?"
published: true
---

I was using Anthropic's Claude chat this morning to generate some utility code to evaluate how well different algorithms work for the task of extracting tabular data from semi-structured documents, like invoices, utility bills or financial reports.

One python code snippet caught my eye. The context is about converting the native output of a deep learning model (Microsoft's `table-transformer`) into a data format for which evaluation implementations already exist (the `COCO` format).

Do you see what's wrong with this code snippet?

```python
categories = [
    {"id": 1, "name": "table", "supercategory": "furniture"},
    {"id": 2, "name": "table column", "supercategory": "table"},
    {"id": 3, "name": "table row", "supercategory": "table"},
    {"id": 4, "name": "table column header", "supercategory": "table"},
    {"id": 5, "name": "table projected row header", "supercategory": "table"},
    {"id": 6, "name": "table spanning cell", "supercategory": "table"}
]
```

If you didn't spot it, look carefully at the `"supercategory"` value in the first entry: do we really want to consider a **data** table as belonging to the category of furniture???

Remember: GenAI hallucinations aren't a bug, they're a feature. Without the fuzzy-wuzzy powers of GenAI, it wouldn't be able to handle so many tasks so well.

The trick is to get the power while managing the flakiness. This is what AI and ML engineers have been doing for decades. Prompt trial-and-error (aka prompt engineering) won't get you there.

*************************************************

Does this post get your pulse going with excitement or hit a nerve that needs expert attention? Then reach out to me on [LinkedIn](https://www.linkedin.com/in/paul-larsen/) or email at paul.larsen.sp@gmail.com, and let's see how I can help you and your business.
