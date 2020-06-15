---
title: "US expat taxes made less painful with expat-fatcat"
published: true
---

Today marks the last day for US expats to file taxes without an additional extension beyond our freebie two months. Only the United States and Eritrea subject its expats to [lifelong double taxation](https://www.taxesforexpats.com/expat-tax-advice/Citizenship-Based-Taxation-International-Comparison.html). Throw in [FATCA](https://www.irs.gov/businesses/corporations/foreign-account-tax-compliance-act-fatca), and that's a lot of expats filling out their f1040s, and f2555s and f116s and Schedule 3s ...

For me the biggest pain point used to be looking up dozens of historical FX rates for each of my salary payments and other relevant expenses (income tax in Germany, rental payments). Add to this the usual Excel accounting madness, and somehow filing taxes lost its fun. Human intelligence is a wonder, and should not be used to sort through Bank of England or ECB reports hoping to find an exchange rate to copy-paste into a spreadsheet.

Three years ago I started a small project [expact-fatcat](https://github.com/munichpavel/expat-fatcat) to automate historical FX-rate look-ups for filling out my IRS forms. This year, I put it on [PyPI](https://pypi.org/project/expat-fatcat/) to ease others' expat-FX-historical-lookup-Excel pain.

## Quick start

After doing `pip install expat-fatcat`, the core functionality is historical FX rate lookup (with some smoothing).

```python
from expat_fatcat import QuandlRateConverterToUSD, FatcatCalculator
converter = QuandlRateConverterToUSD()
# Single historical rate lookup
converter.get_rate('EUR', datetime(2019, 4, 18))
# 1.125
```

The typical use case is a series of salary or divident payments that need to be converted to USD with a rate valid on the date of payment.

```python
payments = [dict(date='2018-01-15', amount=100), dict(date='2018-02-15', amount=150)]
calculator = FatcatCalculator(converter)
calculator(payments, 'EUR', '%Y-%m-%d')
# 310.165
```

See also [notebooks/example-usage.ipynb](https://github.com/munichpavel/expat-fatcat/blob/master/notebooks/example-usage.ipynb).

To make more than 50 API calls / day, get a Quandl API key and store it in the environment variable `QUANDL_KEY`, and it will be used upon initialization of `QuandlRateConverterToUSA`.

Here's wishing you many happy tax returns!
