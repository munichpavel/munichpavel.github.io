---
title: "Data Engineering for and with GenAI: A Journey of Peaks and Potholes"
published: true
---

The utility of ChatGPT and its first cousins (e.g. Copilot like offerings) is relatively clear. Two examples are

1. [A BCG study together with the business schools of Harvard, MIT and the University of Pennsylvania found an average 40% productivity boost using GPT-4 on ideation and content creation tasks](https://www.bcg.com/publications/2023/how-people-create-and-destroy-value-with-gen-ai), and
2. [Github Copilot's claim of 55% productivity gains for 95 test developers on a Javascript task](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/).

Now a driving question is how else we can generate value with generative AI (GenAI)? Data engineering and especially data extraction is one area we will explore in a series of blog posts.

But first, let's take a step back and consider what a next step for GenAI could look like. When talking about the recent excitement around GenAI and especially large language models, relating it to the common experience of Google search seems to help.

Google search's goal is to give you a **selection of useful answers** per question or search task. ChatGPT's goal is to give you a **single useful answer** per question or task. The next step in AI---and our focus in this blog post---is to give you a **single useful action** per task. (Credits to [Ben Thompson of Stratechery](https://stratechery.com/2023/googles-true-moonshot/) for this basic progression.)

Getting from a ChatGPT or other-provided useful answer to a useful action involves

* removing the guard-rails of the human-in-the-loop user as quality-assurance (QA) agent
* removing the bottle-neck of the human-in-the-loop user as QA agent

In this series of blog posts we'll look at how GenAI is changing data engineering, and how data engineering needs to adapt to harness the benefits without exploding your data quality.

Let's take the main example of how I've used GenAI with customers over the past half year: extracting structured data from semi- or unstructured source data, such as PDF reports or invoices. My main take-away is

> GenAI-powered data extraction means higher dev velocity and higher data risk.

The (working) titles for these posts are

1. [LMOps: Prompts just blew up your configuration space (and what to do about it)](https://munichpavel.github.io/2023/06/21/llm-ops-configuration-explosion/) (caveat: more ML engineering than data engineering),
2. GenAI needs [data contracts](https://munichpavel.github.io/2023/03/08/data-contracts/), and
3. Relational databases can tame GenAI volatility

Underlying these recommendations is what can be called a *barbell strategy*. In the original context of financial investments, Nassim Taleb defines it as follows:

> If you know that you are vulnerable to prediction errors, and accept that most risk measures are flawed, then your strategy is to be as hyper-conservative and hyper-aggressive as you can be, instead of being mildly aggressive or conservative.

[Source: *The Black Swan*, Nassim Nicholas Taleb](https://www.penguinrandomhouse.com/books/176226/the-black-swan-second-edition-by-nassim-nicholas-taleb/)

Coming back to tech and GenAI the message is: Go wild technically with all that GenAI enables (going wild ethically is still a no-no), but clamp down the rest of your data pipelines.

Would you like to learn more? Do you have a project that needs data or AI expertise? Then message me on [LinkedIn](https://www.linkedin.com/in/paul-larsen/) or write to me at paul.larsen.sp@gmail.com.
