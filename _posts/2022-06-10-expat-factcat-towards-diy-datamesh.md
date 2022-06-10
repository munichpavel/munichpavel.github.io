---
title: "expat-fatcat 2022: towards a DIY data mesh"
published: true
---

For us American expats, June 15th is when we have to file our annual tax returns (expats get a 2-month extension). This year, I decided to leave the python package [expat-fatcat](https://github.com/munichpavel/expat-fatcat) untouched, and instead spice up this year's tax filing process by starting a do-it-yourself (DIY) [data mesh](https://www.thoughtworks.com/what-we-do/data-and-ai/data-mesh).

OK, so a fully DIY data mesh isn't something I could reasonably manage in my free time on my 2019 MacBook Air, but my hope is to get as far as I can as a means to make sense of some data mesh principles and claims that sound great in theory, but for which I can't yet see a path to implementation.

The specific claim I am fleshing out with [expat-fatcat](https://github.com/munichpavel/expat-fatcat) (or rather, a [Django REST framework app](https://www.django-rest-framework.org/) around it) is from the *Principle of Data Ownership* chapter of [Zhamak Dehghani](https://www.linkedin.com/in/zhamak-dehghani/)'s book [Data Mesh: Delivering Data-Driven Value at Scale](https://www.oreilly.com/library/view/data-mesh/9781492092384/):

> Exposing analytical data directly from the operational database is an antipattern. This antipattern is observed in the implementation of ETLs and application of change data capture and data virtualization on top of the application’s database.

Thanks to [Emily Gorcenski](https://www.linkedin.com/in/emily-gorcenski-0a3830200/)'s support, I could get started with a prototype implementation in the spirit of data mesh (and avoiding the above antipattern), but there's still lots to do before having even a mini-MVP, both bits that I basically know how to implement, and even more where the effort so far has exposed white spots.
