---
title: "fake-data-for-learning on PyPI"
published: true
---

My [package-in-the-making](2020-02-20-risk-ai-workshop) [fake-data-for-learning](https://github.com/munichpavel/fake-data-for-learning) to create interesting fake data for machine and human learning is 'in-the-making' no more! Now you can start using it from [PyPI](https://pypi.org/project/fake-data-for-learning/) with `pip install fake-data-for-learning`.

## The Easy Part

I developed the package with `setup.py` from the beginning, via the `-e .` line in the `requirements.txt`. The actual packaging worked exactly as documented in [the official tutorial](https://packaging.python.org/tutorials/packaging-projects/).

## The Tweaks

The modifications to my previous code for [PyPI](https://pypi.org/) fell into two categories, first how to make the PyPI landing page look decent, and second, topics I uncovered or finally got around to while preparing for packaging.

### Cosmetic

To make the PyPI landing page for my project look decent, I started by using the `setup.py` boilerplate from [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage), including parsing of your README, which is then assigned to `long_description`.

When rendered on [PyPI](https://pypi.org/), however, all relative links were broken. I tried making them absolute to my GitHub repo, but then decided to violate [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) and just copy-paste a short description into `setup.py`.

### The new and the procrastinated

While reading packaging documentation, I noticed that [pytest-runner](https://pypi.org/project/pytest-runner/) has been deprecated due to security vulnerabilities. The recomendation is to use something else, like [tox](https://tox.readthedocs.io/en/latest/).

I first head of tox a few years back when starting with [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage), but had put off doing more than reading the welcome page.

When using tox, I quickly discovered I was guilty of all sorts of [PEP](https://www.python.org/dev/peps/) sins. I had been using [pylint](https://www.pylint.org/) in [Visual Studio Code](https://code.visualstudio.com/), but somehow didn't catch as much as tox did (or maybe I was just better at ignoring it). I also installed the [cornflakes linter](https://marketplace.visualstudio.com/items?itemName=kevinglasson.cornflakes-linter), which made my style faux pas more obvious.

## Wrapup

Generating interesting fake data is now even easier with ```pip install fake-data-for-learning```.

If you like [fake-data-for-learning](https://github.com/munichpavel/fake-data-for-learning/), please star it on GitHub. Any issues, then just add an [issue](https://github.com/munichpavel/fake-data-for-learning/issues).
