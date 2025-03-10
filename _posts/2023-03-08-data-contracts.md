---
title: "Data Contracts in AI solutions: assumptions should not be so expensive"
published: true
---

Complaining about data quality while developing AI solutions is a bit like complaining about politics. It feels good while you're doing it and often makes you feel smarter compared to others, but rarely results in concrete action. And this inaction leads to high costs, as, in our experience

> Data preparation is the most expensive part of an AI project.

To move beyond complaining about data quality into action (and code), [Manlio Grillo](https://www.linkedin.com/in/manliogrillo/), [Korbinian Breitrainer](https://www.linkedin.com/in/korbinian-breitrainer-1109b6bb/) and [Paul Larsen](https://munichpavel.github.io) of Allianz SE, and [Tsuyoshi Sugubuchi](https://www.linkedin.com/in/tsuyoshi-sugibuchi/) of Allianz France began developing and testing *data contracts* between data consumers (e.g. a team developing AI solutions) and producers (e.g. a data warehouse team or a business unit with domain data for the AI solution) to better manage data exchanges between teams.

At the risk of claiming too much, we present our experience with data contracts as a [design pattern](https://en.wikipedia.org/wiki/Design_Patterns), where a *design pattern*  "[describes] a problem which occurs over and over again in or environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice." (Source: [Christopher Alexander, cited in *Design Patterns*](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/).)

A design pattern typically consists of four parts: the pattern name ("data contracts"), the [problem space](#data-contract-problem-space) it relates to, the [solution elements](#data-contract-solution-elements), and the [consequences](#data-contract-consequences).

Historical note: The term "data contracts" is not new. It appears in the [.NET framework](https://learn.microsoft.com/en-us/dotnet/framework/wcf/feature-details/using-data-contracts) for server-client data exchanges, and more recently in the [substack post](https://dataproducts.substack.com/p/the-rise-of-data-contracts) in the context of data pipelines of [Chad Sanderson](https://substack.com/profile/12566999-chad-sanderson)  (and subsequent [Data Contract Battle Royale](https://www.youtube.com/watch?v=4BEpYAp3Qu4&t=1s) with [Ethan Aaron](https://www.linkedin.com/in/ethanaaron/)).

Disclaimer: the views expressed here are solely the authors', and do not represent the views of our employers.

## Data contract problem space

Mismatches of data expectations between data producer and consumer break AI solutions, and slow down development process.

Examples include:

* A production AI pipeline fails due to upstream changes in primary key logic
* Weeks required to train a first ML model with provided datasets due to slow, multiple iterations with data provider (missing target column, unexpected column value relationships, changes in fields delivered, changes in file format, ...)

Looking at the 2nd example of initial development work on an ML model for claims, we can break the status-quo process into the following steps:

1. *Agreeing on data expectations*: request data deliveries containing specified fields in a combination of emails and WebEx meetings

1. *Preparing the data deliveries*: the data producer (e.g. a business unit) performs custom queries from their source systems to produce one or more tables for the fields requested

1. *Transferring data deliveries*: the data producer sends the requested tables (typiclly as csv or Excel files in a first delivery, then parquet files for follow-up deliveries) to the data consumer (AI Team)

1. *Searching for data expectation failures*: Data consumer (AI team) explores data deliveries in Jupyter notebooks. Failures of data expectations are found by a combination of exploratory data analysis and running code on the (new) data delivery.

1. *Remediating data expectations failures*: Data consumer manually prepares evidence of data expectation failures for critical failures (like a missing target column) or adapts code for non-critical failures. For critical failures, evidence is typically gathered by exporting table extracts or plots from Jupyter notebooks to be incorporated into PowerPoint, Confluence or an email. In a WebEx session, these failures are discussed, and the data producer begins preparing a new delivery.

The status quo data delivery iterations take weeks of time, due to

* lack of clarity in agreeing upon data expectations
* manual work to find failed data expectations
* manual work to communicate critical data expectations failures for the next round, or modify AI solution code for non-critical data expectation failures

## Data contract solution elements

The pain-points of the status quo management of data deliveries can be combined to form the two components of a data contract:

A *data contract* is

* an agreement between parties about data expectations for each required data delivery
* a means of enforcing these data expectations, with a strong preference for automation

Note that the status quo process described above also involve these two components, but in an inefficient way. We can call the above painful data exchange and quality experience in projects as a specific type of data contract, but an anti-pattern, rather than pattern.

### Trojan horse data contract anti-pattern

The Trojan Horse anti-pattern is the most common in our experience as AI teams, and is characterized by upstream data producers sending us whatever data is most convenient for them to produce, which (at first) suits the data producer well, but not the downstream data scientist or engineer.

<p align="center">
  <img src="/assets/producer-happy-consumer-sad.png" />
</p>

Image source: author's own, as with other pencil drawings below.

Why Trojan Horse? Because the convenience of data producers sending data deliverables (e.g. CSV or Excel extracts) without any agreement about data expectations typically leads to unpleasant, costly surprises for the AI solution team.

<p align="center" title="Adam Jones from Kelowna, BC, Canada, CC BY-SA 2.0 &lt;https://creativecommons.org/licenses/by-sa/2.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Replica_of_Trojan_Horse_-_Canakkale_Waterfront_-_Dardanelles_-_Turkey_(5747677790).jpg">
  <img width="256" alt="Replica of Trojan Horse - Canakkale Waterfront - Dardanelles - Turkey (5747677790)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Replica_of_Trojan_Horse_-_Canakkale_Waterfront_-_Dardanelles_-_Turkey_%285747677790%29.jpg/256px-Replica_of_Trojan_Horse_-_Canakkale_Waterfront_-_Dardanelles_-_Turkey_%285747677790%29.jpg">
</p>

[Image source](https://commons.wikimedia.org/wiki/File:Replica_of_Trojan_Horse_-_Canakkale_Waterfront_-_Dardanelles_-_Turkey_(5747677790).jpg)


### Gandalf and the Balrog / "You Shall Not Pass" data contract anti-pattern

On the opposite end, the Gandalf and the Balrog anti-pattern leads to an initially happy downstream data consumer (data engineer or scientist) as she or he has set up an exhaustive and exhausting set of data expectations for the data producer upstream.

<p align="center">
  <img src="/assets/producer-sad-consumer-happy.png" />
</p>

For example, accepting only [highly normalized data deliveries](https://en.wikipedia.org/wiki/Database_normalization) will help the downstream data engineer ensure the integrity of all deliverables, but will likely wear down the data producers patience, sending both parties down into a fiery abyss.

<p align="center">
  <img width="256" src="https://i.pinimg.com/originals/27/9b/0c/279b0c676bda5bfaf783e6683e38651b.png">
</p>

[Image source](https://i.pinimg.com/originals/27/9b/0c/279b0c676bda5bfaf783e6683e38651b.png)

### Odd Couple / Groot and Drax data contract pattern

Our target picture for data contracts is to have [odd-couple](https://en.wikipedia.org/wiki/The_Odd_Couple_(1970_TV_series)) agreements that work for both parties. The parties may be different in their way of working and needs, like Groot and Drax from [Guardians of the Galaxy](https://en.wikipedia.org/wiki/Guardians_of_the_Galaxy_(film)), but thanks to a good data contract, they can work well together.

<p align="center">
  <img src="/assets/producer-happy-consumer-happy.png" />
</p>

<p align="center">
  <img width="512" src="https://screenrant.com/wp-content/uploads/2017/02/Guardians-of-the-Galaxy-Baby-Groot-and-Drax.jpg">
</p>

[Image source](https://screenrant.com/wp-content/uploads/2017/02/Guardians-of-the-Galaxy-Baby-Groot-and-Drax.jpg)

## Data contracts: agreeing on data expectations

Characteristics of an effective data expectation agreement process are

1. Recognition that the process is iterative changes can be managed but not completely eliminated
1. High level of transparency among stakeholders on data expectations

The first point is especially important for AI solutions, and present to a lesser degree--if not entirely missing--in other types of software. This difference arises from the highly exploratory nature of AI solutions in the early phases. Even in the more mature project phases the "learning" component of machine learning / AI means that iterating on data expectations never completely goes away.

The second point is made harder by the iterative and exploratory nature of early stage AI work, but, if done well, can cut down on the iterations required. A typical situation encountered is that the Data Scientists and Engineers request of the business colleague data deliveries from (often legacy) systems from another part of the organization for some model development. The data science and engineering team does not know the legacy sources on the data producer side, and the business colleagues (including business analysts who create data extracts from legacy databases plus IT colleagues responsible for these databases) do not typically understand required data expectations for machine learning models.

Put bluntly, transparency on data expectations among shareholders is typically very hard. Typically the data scientists and engineers get initial deliveries from their business partners based on schema concerns (delivery file format, required fields) but not on instance concerns (reference values, nulls) or change concerns. During initial exploratory analyses and modeling, the data scientists and engineers find required data expectations that are not met, and feed this back to the business by showing plots or data sample extracts. This process results in increased transparency, but slowly and with multiple iterations required.

One approach that has been effective in our experience is for the the data scientists and engineers to request key technical documentation from the business colleagues early in the project lifecycle, such as entity-relationship diagram extracts from the business-side legacy database. Note that such forms of documentation are relatively easy to produce from the business side, and do not require creating additional documentation for the data science / engineering team.

Some data expectations can be clarified immediately from this additional documentation, but even for remaining open data expectation that cannot be answered directly, having this additional documentation means that transparency is achieved faster with fewer administration iterations with the business stakeholders.

Multiple iterations with other stakeholders on defining and modifying data expectations cannot be avoided, but in our experience, there are ways to reduce the number of iterations and make the remaining feedback sessions more efficient. The keys to achieving more effective data expectation administration are high levels of transparency and high levels of automation.

For data scientists and engineers whose work depends on data deliveries from the business:

* Make explicit assumptions about required expectations, and feed these back to colleagues preparing the data early in the project to cut down on back-and-forth.
* Aim for a high level of automation in creating feedback (plots, sample tables) for business colleagues on data expectation to make iterations faster.
* Request targeted technical documentation of the data deliverer’s source system like entity-relation diagrams from a database to eliminate or make more efficient administration iterations.

## Data contracts: enforcing a data contract

Good data contract enforcement is

* highly automated
* transparent
* robust, and
* easy to change

Before discussing what tooling and practices enable achieving these goals, we give a based-on-a-true story example that fails each of these points.

### Enforcement anti-pattern: data expectations and enforcement miles apart

For example, the data expectations are codified in an Excel or confluence table for communicating between the data consumers and producers, which is then used as loose inspiration for writing custom python code to enforce these expectations.

This anti-pattern fails two of our criteria

* not transparent, as the table-version of the data expectations may be transparent, but the conversion into enforcement is opaque
* not easy to change, as changes to data expectations involve (re-)writing custom code.

### Enforcement anti-pattern: data expectation failure only found by luck, communicated by hard work

This situation arises often within the larger [Trojan horse data contract anti-pattern](#trojan-horse-data-contract-anti-pattern), where data errors show up downstream in the model creation pipeline indirectly, e.g. learning that a (possibly implicit) data expectation failed

* model performance drops because categorical labels change, resulting in the categorical encoder trained on the old deliveries mapping all new values to the "unknown" category.
* date formats switch from one delivery to the next. One change was noticed immediately by a data pipeline error, but subsequent data format changes were only picked up a week later when a data scientist spotted events from the future in the course of another analysis.

When they are detected, then communicating to the data producers typically involve exporting tables and graphics from Jupyter notebooks into PowerPoint that is shared via email, often followed up by a WebEx meeting to discuss the data bug and how to fix it for the next delivery.

## Data contract implementation

We implemented a demo data contract implementation using [Great Expectations](https://greatexpectations.io/) to give an example of data contract enforcement that satisfies our desiderata for enforcing a data contract (and this in early 2022 before Great Expectations trumpeted data contracts on their landing page :grinning:), as well as a lightweight python version using [pydantic](https://docs.pydantic.dev) plus a DIY declarative data expectation schema and enforcement mechanism.

[Great Expectations](https://greatexpectations.io/) has potential to meet all desiderata of a good data contract enforcement as

1. High automation is achieved by embedding data validation into checkpoints along your data pipeline, which can be configured to trigger actions such as alerts.
1. Transparency is achieved by the Data Docs, which feature a user-friendly presentation of data expectations and validation reports for all validation actions.
1. Robustness is achieved by configuring the data contract expectations in a consistently formatted plain-text file (JSON) placed under version control.
1. Ease of change is achieved by Great Expectation utilities, such as automatically generated (and hence disposable) Jupyter notebooks for editing expectations. An interface to edit expectations for non-developers (e.g. business analysts) is not provided out-of-the-box.

BUT, as with an open-source tooling, there is important DIY ("do-it-yourself") work remaining, such as

* configure to your pipeline framework
* integrate checkpoints into your pipeline
* write tests
* integrate into model execution framework (e.g. FastAPI on AI Core)

## Data contract consequences

* (Benefit) Avoid painful and expensive data expectation failures in productive systems
* (Benefit) Fewer data iterations via more transparent and precise agreement on data expectations
* (Benefit) Faster, more detailed feedback loops between data producer and consumer via automated data contract enforcement
* (Cost) Upfront implementation investment, either learning and applying an existing framework or creating your own

## Lessons from experience

In our collective experience, there *were* data expectations and they *were* enforced somehow, but all too often the enforcement of data expectations is done implicitly, vaguely lumped together under the label “data quality.” The lack of explicit enforcement of data expectations is one main factor in the unpleasant and costly data quality surprises that we aim to avoid.

Data contracts, by combining both the human and technical concerns, provide the transparency and automation required for AI solution teams and their business data providing counterparts to get past complaining about one another and find a dynamic equilibrium with which both sides can be reasonably happy and significantly more efficient in delivery.
