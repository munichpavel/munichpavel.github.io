---
title: How GenAI has (and hasn't) changed the way Allianz, ThoughtWorks and Outbrain lead data and AI teams
published: false
---

> This blog post was originally published at [mkdev.me/]().

If you take the vendor and media hype at face value, GenAI is a game changer for how data and AI teams work. What does GenAI mean in practice for those of us leading data or AI teams? On one extreme, there [won't be any more data or AI teams](https://x.com/klarnaseb/status/1876093526280171699), as they will be replaced by non-technical managers (human or otherwise) orchestrating a swarm of GenAI code-bots.

The other extreme view is that GenAI is mostly a distraction, as

* very little code written by GenAI [gets used as is](https://www.blueoptima.com/the-4-reality-what-genai-really-means-for-software-development-productivity/)
* only a small fraction of existing AI use cases are suited for GenAI
* GenAI won't replace the main function of data + AI teams, namely delivering the interface between business or product needs, and technical development.

The above points are about the team functioning, not necessarily what it means to lead a data or AI team. It's also important to consider GenAI's impact on getting new projects for your team, optimizing productivity and developing talent, to name a few.

To better splice what GenAI means in practice for data + AI teams, we asked three leaders teams or divisions how GenAI has, or hasn't, changed what it means to lead.

**[Andraž Tori](https://www.linkedin.com/in/andraz/)** is the Chief Product Officer of Outbrain. He co-founded the machine learning-based ad-tech company, Zemanta (now Outbrain Demand-Side-Platform), in 2007, and is a co-founder of the Slovenia-based investment fund [Silicon Gardens](https://silicongardens.com).

**[Pinar Karabulut-Leblebici](https://www.linkedin.com/in/npinark/)** is a Lead Data Scientist with Allianz Services in Munich. She's also worked for PricewaterhouseCoopers and a Legal-Tech Startup.

**[Emily Gorcenski](https://www.thoughtworks.com/profiles/service-line-leads/emily-gorcenski)** is Vice President of Data and AI for ThoughtWorks, where she oversees data and AI engagements for the German market. She is also heavily involved in data journalism and data justice initiatives.

We'll structure their insights into two categories. First, we look at their experience with GenAI for while turning ideas and business opportunities into deployed, scaled AI and data products (what we call the "[AI Value Funnel](https://mkdev.me/posts/ai-strategy-guide-how-to-scale-ai-across-your-business)"). How does, or doesn't, GenAI change the way they ideate new solutions with the business, deploy into production and then scale across the business?

The second focus area is team productivity and development. How has (or hasn't) GenAI changed the daily work of their team? What does GenAI mean for current and future talent development?


## GenAI and managing the AI value funnel

At the wide end of the [AI value funnel]((https://mkdev.me/posts/ai-strategy-guide-how-to-scale-ai-across-your-business)) is the initial ideation and scoping work with the business to come up with new products. We've already written about [how GenAI has made it easier than ever to develop prototypes](https://mkdev.me/posts/ai-strategy-guide-how-to-scale-ai-across-your-business), meaning it's faster and easier to quickly iterate on product-market fit. Pinar Karabulut-Leblebici confirms this view, with her team building initial prototypes often entirely from GenAI components. They even sometimes choose GenAI components though it's likely that classical AI components will replace GenAI as the project approaches go-live in production.

In areas where GenAI isn't just a quick means to an end, the team leaders we interviewed are embracing the project opportunities it affords. A key business opportunity with GenAI, specifically the Large Language Model subset, is text based reasoning and generation. In [Marketing and Lead-Generation](https://www.linkedin.com/posts/barbara-karuth-zelle_customerexperience-genai-riskassessment-activity-7197203809981337601-3oFW/) projects, it's rarely enough to give the business a blank recommendation, regardless of how amazing your AI's technical metrics are. The business partners (and often end-customers) want some understanding of **why** they are being offered a new product, why a new sales campaign is targeting a given demographic, or why reaching out to a specific customer profile will improve retention. These explanations often go under the heading "reason-to-believe." [Pinar sees value in GenAI](https://www.linkedin.com/posts/npinark_thrilled-to-share-that-our-team-emerged-victorious-activity-7133736097490120704-f2j6?utm_source=share&utm_medium=member_desktop) not only to provide human-readable versions of technical explainability approaches like [Shapely values](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html), but also in exposing to the customer real-world context that can get missed by technical approaches. In one example, where additional flood risk coverage is a recommended addition to a property insurance policy, the GenAI reason-to-believe module might cite that the property location is close to the Rhine River, hence the AI-recommendation for the extra protection.

Emily Gorcenski sees opportunities for her department not only in AI, but also with their whole approach to accessing and maintaining internal business knowledge.

> GenAI lays bare all the reality of knowledge management in most organizations: it's too hard to find and too inconsistent.

Yes, robust data pipelines and warehouses are still required, but not to the degree many assume, according to Emily. The wealth of business knowledge contained in un- or semi-structured documents that can be parsed, processed and interpreted by GenAI together with classical techniques means that

> GenAI has removed any excuses that remained regarding the cost and difficulty of leveraging internal unstructured data.

She sees GenAI unlocking a significant opportunity in data governance, e.g. with computational data governance of [Data Mesh](https://www.thoughtworks.com/insights/decoder/d/data-mesh), the data paradigm [Zhamak Dehghani](https://www.nextdata.com/company) created while at ThoughtWorks with contributions from Emily.

Both Emily and Pinar's teams both have overwhelmingly positive experiences with the GenAI technique Retrieval Augmented Generation, in which a Large Language Model isn't just given a task to complete, but also relevant background context as provided by a retrieval step, often from non-public data sources. Of GenAI techniques and patterns, Retrieval Augmented Generation is perhaps the most mature, having already moved to an "Adopt" recommendation in [ThoughtWork's April, 2024 Technology Radar](https://www.thoughtworks.com/radar/techniques/retrieval-augmented-generation-rag).

Despite these new opportunities and ways of workings, our experts don't see GenAI supplanting most of what they do. For example, GenAI will not replace the proprietary AI behind the ad-tech algorithms of Andraž Tori's teams at Outbrain any time soon. Why? Their content-recommendation algorithms have to run while a website such as [Handelsblatt](https://www.handelsblatt.com) or [CNN](https://edition.cnn.com) is loading, meaning their models have to give a prediction in a few milliseconds, something GenAI cannot at present manage. Heuristically, the current speed needs translate could only be met by a neural network that’s no deeper than 10 layers or so, otherwise response times are too slow. The full GPT-3 model from back in 2020 is approximately [10x this size](https://arxiv.org/pdf/2005.14165).

GenAI can even make important aspects of AI development harder, for example, evaluation of output quality. There are ways to coax GenAI to give outputs that can be exactly verified as correct or not, but the greatest strength and still most common usage of Large Language Models is to give free-form text as its output. Free form text is, by nature, more difficult to evaluate for correctness. If you don't believe me, just ask any teacher.

Pinar contrasted the evaluation challenge with the hype and vendor pressure to make everything GenAI:

> If you don't know how to measure and quantify impact, the model isn't enough. In the end, we're not working for Microsoft, we have to prove it works for the business.

Last but not least, there's also an internal marketing component to having your team engage with the latest hype, in this case GenAI. One Chief Data Officer, who preferred not to be named, said that he had to mention GenAI in every presentation to the Board of Management, otherwise they would lose interest.


## Team productivity and development in the age of GenAI

GenAI or not, I firmly believe that a data or AI team's greatest strength is the talent and work of its members. That's why it's essential to maximize your teams' productivity and make access to this valuable, hard-won knowledge as easy and complete as possible. GenAI and related technology has been a game-changer here.

These two team-management topics are followed insights from our experts on our final question: what does GenAI mean for the next generation of Data + AI experts?

While GitHub's initial Copilot coding assistant [boasted 55% productivity gains on a relatively standard website programming task](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/), [subsequent results](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566) on developer productivity gains are [more modest](https://www.blueoptima.com/the-4-reality-what-genai-really-means-for-software-development-productivity/), with anecdotal and [corelational (not causal) evidence that the effect can be negative](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality). BlueOptima, a service for measuring dev team's productivity and quality, found in their study involving more than 200k developers that [productivity gains were more like 4%](https://www.blueoptima.com/the-4-reality-what-genai-really-means-for-software-development-productivity/). I am not the only one skeptical about [quantitative-only measures](https://martinfowler.com/articles/measuring-developer-productivity-humans.html) of [developer productivity](https://martinfowler.com/bliki/CannotMeasureProductivity.html), but I value that 1. BlueOptima has an explicit methodology more complete than task-completion time of the GitHub Copilot study, and 2. their interest is in accurate, useful metrics for productivity and quality, not selling GenAI.

Our three data + AI experts split into two camps for copilot-like code generation usage. Pinar works in a heavily regulated financial services company, though Allianz has developed and internally deployed its own [AllianzGPT](https://www.linkedin.com/posts/allianz-technology_allianzgpt-iberolatam-innovation-activity-7219317967497400322-Ve0r?utm_source=share&utm_medium=member_desktop) [solution](https://www.allianz-trade.com/en_global/news-insights/expert-voices/how-to-transform-data-into-value.html). As Pinar further points out, modern coding tools already have nearly magical, non-GenAI productivity boosters, including auto-complete, mistake-flagging and refactoring tools.

Andraž and Emily's departments were early adopters of copilot-like code generation. Emily's experience is that the greatest gains aren't in code generation, but rather for accelerating with project management, story creation, requirements documentation and other code-peripheral tasks.

Among their customers, Emily sees reluctance to embrace GenAI code assistance due to their perceived "lack of accountability and difficulty with measuring quality," though Emily's department is actively working on filling in these gaps for their customers.

The second way the experts we interviewed are using GenAI to boost team effectiviness is by connecting their knowledge bases to semantic search tooling. We covered semantic search in our [blog series](https://mkdev.me/posts/which-database-when-for-ai-are-vector-databases-all-you-need) on [vector databases](https://mkdev.me/posts/which-database-when-for-ai-vector-and-relational-databases-in-practice), but the TL;DR version is that semantic search enables you to use natural language, rather than a programming language, to find answers and relevant sources to your questions. In this application, the search is over performed over internal wikis, code bases and other internal sources that are not public, and hence hidden from off-the-shelf GenAI models.

Andraž's dev-teams quickly implemented a semantic search on top of its internal knowledge base. Emily and ThoughtWorks have done the same. Both have considerable treasures in their wikis and code bases, meaning beginners and veterans alike have a single point of entry for their questions, especially if they don't already know where to look.

What about the next generation of data + AI experts? Copilot-like solutions and ever better access to expert knowledge via semantic-searchable knowledge stores mean that senior experts are more productive. This in turn means that much work that would previously be handed over to a junior never reaches them.

When I asked Andraž how juniors can develop into senior roles, his response was one word: "Bingo." This problem is a tough one.

## The significance of GenAI, real and hallucinated, for managing your data + AI teams

In our experts' experience, as well as ours at [mkdev](https://mkdev.me), GenAI does not change everything about leading data or AI teams. You should not be laying off your valuabe data and AI talent, since

1. Much of classical AI and data expertise is still needed to fulfill typical data + AI needs, and
2. Code assistants, when used smartly, are boosting productivity, but would require significant improvements on quality and reliability before being used without expert supervision

Behind the exuberance, maybe even hallucinations, of vendors and tech-hypers there are significant benefits to trialling and adopting new opportunities and ways-of-working that GenAI advances open up. Ignoring these mean your teams will get left behind.

If you'd like help reaping the benefits while avoiding the pitfalls of GenAI for your data or AI teams, please reach out to me at paul@mkdev.me or our sales team at team@mkdev.me.

### Acknowledgements

In addition to our amazing experts, I'd like to thank [Blaz Mramor](https://www.linkedin.com/in/blaz-mramor-93058967/) for technical background about real-time bidding.