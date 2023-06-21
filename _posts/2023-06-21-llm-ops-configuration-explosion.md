---
title: "LMOps: Prompts just blew up your configuration space (and what to do about it)"
published: true
---

The first time I saw a software engineer with no data or statistics background demo a GPT-3 powered text classification use case, my reaction was "This is both super exciting and super scary." It seems clear that the excitement around ChatGPT and the GPT-3+ family is more than just hype. What has changed and what has not given the performance jump of large language models (LLMs) is a question for all of us in the field to actively answer.

What has clearly changed is that tasks such as question answering that would have required a number of different components, each of which would have required separate development followed by integration work to perform well, can now be largely off-loaded to a single API call to a single service.

So yes, it is [different this time](https://nadh.in/blog/this-time-it-feels-different/), but there is still [no free lunch](https://en.wikipedia.org/wiki/No_free_lunch_theorem). With the increased range of tasks you can off-load to an LLM, there are also new sources of volatility with LLMs compared to other ML applications, including

1. choice of language syntax in your prompt
2. probabilistic, rather than deterministic, outputs

The first point is specific to language models, while the second applies to any generative model, as the output is probabilistic, and not deterministic.

## Natural language syntax is now part of your configuration space

If we look at prompt syntax as part of your model configuration, then the good news is that the machine learning community has developed mature tooling to manage configuration, as the process of model selection amounts to trying out different configurations of model family, architectures and (hyper- )parameterizations in experiments and choosing the configuration with best performance. As with LLMs, the models from more traditional ML are also black boxes of sorts, where intuition is possible but getting robust root-cause explanations is difficult if not impossible.

In this post, we use [Hydra](https://hydra.cc/docs/intro/), a Python framework to manage both configuration specification and the outputs of your runs with different configurations (aka experiments). In non-LLM ML tasks, the types of configuration data can be divided into

* categorical configuration, such as model-family implementation name (e.g. `sklearn.linear_model.LogisticRegression`, `lightgbm`)
* graph or network configuration, such as neural network architectures
* numerical configuration, such as learning-rate, number-of-trees, number-of-clusters

There are already significant theoretical and computational considerations to evaluating across these three types of configuration.

The good news is that numerical configuration of the LLM we consider here (`gpt-3.5-turbo-0301`) is a single parameter, the `temperature`, which roughly calibrates how strict (temperature close to 0) or imaginative (temperature close to 1) of a response you wish. For this post, we ignore the small number of other parameters; see the [Open AI create completion API documentation](https://platform.openai.com/docs/api-reference/completions/create) for more.

The bad news is that LLMs add a 4th type of configuration, namely **natural language syntax configuration** in how prompts are written. Any change to your prompt syntax–be it a re-wording, a typo, an extra line, a punctuation change–can change the performance of the LLM. If you want to do LLMOps, natural language syntax just blew up your configuration space.

To bring some order to this potential chaos, we break the prompt configuration for generative-question answering into different parts, each of which we will manage with Hydra.

1. Prompt template structure (e.g. Jinja or python string) and its syntax.
1. Prompt component syntax (e.g. context-component, answer-format component, question-component)

And for each of these we have perhaps less obvious configuration dimensions such as

* Punctuation, tabs vs spaces, treatment of non-ascii characters (e.g. "Männer" vs "Maenner")
* For non-English domains, when to use the domain-native language and when to use English in each of the above components.

There is plenty of guidance ("best-practices’) on writing prompts, but what I have seen is on the level of writing a single prompt well to solve your problem (e.g. from [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api) and [DeepLearning.AI’s prompt-engineering course](https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/1/introduction)), and not
how to manage prompt variants (and that over time).

For even if you have optimized a prompt for your use case today, if you want to are calling a model that is [updated continuously](https://platform.openai.com/docs/models/continuous-model-upgrades) (and without any version tags), such as `gpt-3.5-turbo` and the `gpt-4` family, you have no guarantee that the prompt that was good enough yesterday still works. On the flip side, with model, an updated model might need less guidance on answer-format, meaning you have more tokens for giving additional context.
## Generative question answering example: Querying top-times in German masters swimming

I swim in a master’s club, and enjoy tracking how my times stack up in my age group and main events on the website [https://www.dsv.de/schwimmen/wettkampf-national/bestenlisten/](https://www.dsv.de/schwimmen/wettkampf-national/bestenlisten/). Here’s the main question I want to answer, formulated in English:

> What were the top 5 times in Germany between 2018 and 2020 for men in the 100m butterfly for the age group 40-44?

I’ve chosen for this blog post that a response is only correct if it semantically returns the expected best times and the response meets a specified JSON schema with data types (i.e. the service satisfied a [data contract](https://munichpavel.github.io/2023/03/08/data-contracts/)). Insisting that the correct response have a fixed schema means that we can test correctness automatically in a straightforward way. Of course, with some postprocessing I could have relaxed some of the data type requirements, but first, this goes against the philosophy of off-loading as much as possible to the LLM, and second, the stricter requirements mean we have more occasion to examine failure examples.

Sources of complexity that arise from this example use case include

* context must be provided, otherwise the LLM returns the usual "As an AI model, I do not have access ..."
* the context data is non-English (German)
* the need for a response schema means that the prompt must include answer-format instructions

The template syntax I use (with variations) is the Python string

```python
template = """Context: {context}

Question: {question}

Answer format: {answer_format}

Answer: """
```

which beomes the prompt for values of `context`, `question` and `answer_format` via

```python
prompt = template.format(context=context, question=question, answer_format=answer_format)
```

The expected response for the question given above as a json-document is

```json
[
    {
        "Platz": 1,
        "Schwimmer": "Thomas Ehrhardt",
        "JG": 1977,
        "Verein": "SSKC Poseidon Aschaffenburg",
        "Zeit": "1:01,64",
        "Punkte": 465,
        "Ort": "Gwangju",
        "Datum": "8/2019"
    },
   {
       "Platz": 2,
        "Schwimmer": "Jochen Kaminski",
        "JG": 1974,
        "Verein": "SSF Bonn 05",
        "Zeit": "1:03,91",
        "Punkte": 417,
        "Ort": "Karlsruhe",
        "Datum": "6/2019"
   },
   {
       "Platz": 3,
        "Schwimmer": "Paul Larsen",
        "JG": 1977,
        "Verein": "TSV Haar",
        "Zeit": "1:05,01",
        "Punkte": 397,
        "Ort": "Kranj",
        "Datum": "9/2018"
   },
   {
       "Platz": 4,
        "Schwimmer": "Sebastian Kratzenstein",
        "JG": 1978,
        "Verein": "BSC Robben",
        "Zeit": "1:05,21",
        "Punkte": 393,
        "Ort": "Karlsruhe",
        "Datum": "6/2019"
   },
   {
       "Platz": 5,
       "Schwimmer": "Torben Kritzer",
       "JG": 1977,
       "Verein": "Bad Homburger SC 1927",
       "Zeit": "1:05,64",
       "Punkte": 385,
       "Ort": "Karlsruhe",
       "Datum": "6/2019"}
]
```

## Prompt syntax configuration in practice: successes and failures

In this section, we highlight which syntax variants of the template, context, question and answer-format yield the expected result, and---what’s more interesting---which fail to give the expected result.

### Successful prompt syntax example

As mentioned, by success I mean the LLM-service returns records and data types as in the above json-document. Of the combinations created from variants [https://github.com/munichpavel/munichpavel.github.io/generative-question-answering/prompt_variants.json](https://github.com/munichpavel/munichpavel.github.io/blob/517be3ddc1346669886dd8102242888193431f58/generative-question-answering/prompt_variants.json), the only one that results in the expected response has context template as above, with context consisting of the copy-pasted relevant results from [https://www.dsv.de/schwimmen/wettkampf-national/bestenlisten/](https://www.dsv.de/schwimmen/wettkampf-national/bestenlisten/), and question and answer-format as follows:

* `question`: "Was waren die top 5 Zeiten Deutschlands der Saison zwischen 2018 und 2020 der Männer auf 100m Schmetterling im Altersklasse 40-44?"
* `answer_format`: "Return only a json document as a list entries with keys `Platz, Schwimmer, JG, Verein, Zeit, Punkte, Ort, Datum`."

Note that the question is in German, and uses the umlaut `ä`, not the latin transliteration `ae`. Turning to the answer-format, is requests that only a json-document be returned e.g. no additional text. (As an aside, `gpt-3.5-turbo-0301` returned json-format only without [having to threaten violence for non-compliance](https://twitter.com/goodside/status/1657396491676164096).) Moreoever, it gives instructions on the schema and expected keys.

I did not need to give one or more example responses as is recommended in some prompt-engineering guidance. There can be a trade-off between more explicit answer format instructions and additional context due to token limits. If your context text grows longer, it’s useful to have the option of (re-) checking shorter answer format instructions, as changes to the LLM (either the same or a sucessor) could mean the detailed answer format of before is no longer needed.
We now examine the question-answering failures.

### Failure due to insufficient context

Not surprisingly, just asking gpt-3.5-turbo-0301 the obscure best swimming time question above without providing any relevant context yields the usual "Sorry, as an AI language model, I don’t have access to the latest sports data
..." messages.

### Failure due to insufficiently specified answer-format

Again, no surprise that if we aren’t specific enough in the required response format, `gpt-3.5-turbo-0301` will guess for us. If we set

```python
answer_format="Return a json document with keys `Platz, Schwimmer, JG, Verein, Zeit, Punkte, Ort, Datum`.
```

then the LLM returns something like

```json
{
"1": {
        "Platz": "Thomas Ehrhardt",
        "JG": "1977",
        "Verein": "SSKC Poseidon Aschaffenburg",
        "Zeit": "1:01,64",
        "Punkte": "465",
        "Ort": "Gwangju",
        "Datum": "8/2019"
    }, "2": {
        "Platz": "Jochen Kaminski",
        "JG": "1974",
        "Verein": "SSF Bonn 05",
        ...
    }
}
```

Note that it not only gets the schema structure wrong, but also gets drops the required Schwimmer key (filling in the name instead under place, or `Platz`) and furthermore gives the year-of-birth (`JG`) and points (`Punkte`) as strings, not integers.

The remaining prompt-syntax failure modes are more subtle.

### Failure due to context format: spaces sometimes matter

Just adding two additional spaces in the prompt template above after the word Context: and the actual context text results in the LLM picking up wrong results from the provided context, namely the two results from the 2019-2020 Corona-shortened season, both of which were slower than the top five times from 2018-2019.

Interestingly, when trying the same variation of spacing in a different generative question answering problem, the same sensitivity to spaces was not present, giving further evidence for the importance of managing your configuration space robustly.

It is natural to dream up reasons why the LLM might select wrong results due to these extra spaces. I have little doubt that tweaking a bit further (e.g. adding the [recommended section break characters for GPT models](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)) could result in the expected result. And that is precisely the point of this blog post–there are so many tweaks we could (and should) try, we need a robust way to manage them.

### Failures due to non-English prompt components

If we use the English question as above but keep all else equal from the successful prompt, the only mistake in the response is that–as with insufficient answer- format guidance–the year-of-birth and point values (`JG`, `Punkte`) are strings, while we expected integers.

The same occurs if we use the German question, but write "men" (`Männer`) with latin letters as `Maenner`.

Maybe, however, these explanations are not root cause analyses, but rather a combination of the inscrutability of LLMs and the probabilistic–rather than determinstic–nature of its outputs. After all, with LLMs ...

### You are still flipping a coin

Even if you robustly test out different prompt and model configurations and set your temperature to 0 (GPT), you are still calling a generative model, which means that you can and will get different answers for the same input.

I tested out the probabilistic nature of `gpt-3.5-turbo-0301` with temperature 0 on the failures linked to mixing an English question with German context and the latinized ä above on 100 runs each:

* expected response counts using `ae` instead of `ä` in the question: 7 of 100 runs
* expected response counts with question in English: 0 of 100 runs

With only 100 trials, these may not be statistically meaningful results, but they do give evidence that the probabilistic nature of generative question answering must be managed with care. It’s tempting to say that you should always pose your question in the same language as any given context, but a more thorough study is needed, plus there may be some principled reason involving how LLMs are trained. If you have one, please let me know and I will add it with an attribution to you :grinning:.

## Conclusion

It is beyond me why exactly the question-answering fails when

* there is an extra space before the context section of the prompt template
* the question is in English while the context is in German
* the question uses `ae` rather than `ä` in the word "Männer".

Moreover, each of the failure modes is different, with the 3rd failure type occuring occasionally.

And that's likely OK, as the appeal of LLMs is that you can off-load much of what your use case needs to the LLM without understanding in full detail why or how it gives the results it does.

What these examples show, however, is that it pays to manage the natural-language-syntax-as-configuration robustly, which in this post we’ve shown by taking approaches from ML–experiment and configuration management using Hydra plus some DIY code on top. As the interest and user base has grown for LLM-based services, so has the tooling, though I expect the two sources of volatility we consider here,

1. choice of language syntax in your prompt
2. probabilistic, rather than deterministic, outputs,

will be the attention of intense activity in the coming months, both theoretical and tooling-related.

Yes, things are different this time, but not so different that "old" practices like configuration and experiment management can be neglected without consequence. So keep getting the super exciting benefits of LLMs while managing the technical scariness of an exploded configuration space.

## Appendix: Failure explanation caveats

The section headings describing failure modes use the language "Failure due to . . . ". This word choice is wrong, as it implies that I have a root cause understanding of input variants and output success or failure. I do not, both due to the complexity of the LLM and due to the probabilistic nature of its outputs. A more robust but less lyrical phrasing would be "Failure linked to ...".

## Appendix: Serializing and managing prompt variants

Ever since a project with Matthias Ossadnik a few years back, followed by work with the data validation framework Great Expectations, I have been a fan of generating config using Jupyter notebooks. I used the notebook [https://github.com/munichpavel/munichpavel.github.io/generative-question-answering/notebooks/generate-prompt-variants.ipynb](https://github.com/munichpavel/munichpavel.github.io/blob/dd8c014a5ea9d5928c659db6039ee3f9ef953315/generative-question-answering/notebooks/generate-prompt-variants.ipynb) to generate the prompt variant components analyzed here.

You may be wondering why I chose JSON over YAML for the prompt variants. JSON is a data format with a relatively simple specification. So while it’s not as human-readable as YAML, you are unlikely to get nasty surprises, and when it comes to natural language syntax configuration, there is enough potential for unexpected behavior that you shouldn’t have to wonder how data serialization might contribute.

I chose to version-control the json prompt variants, which is not a bad choice for initial collaboration, but will likely need to be replaced with a proper data store as your prompt variants increase in size and complexity, if only to keep your git commit history from getting cluttered with prompt tweaking. Some git-features you will want to preserve if moving away from git are

1. audit trail: this can be accomplished in your pipline on the left (version control) or on the right (persisting experiment artifacts)
2. diffs: recognizing an added space or removed " around text is not something you want to have to catch by eye, so be sure you have some diff tooling to recognize changes.

On the 2nd point, I use the standard library difflib in the notebook [https://github.com/munichpavel/munichpavel.github.io/generative-question-answering/notebooks/evaluate.ipynb](https://github.com/munichpavel/munichpavel.github.io/blob/dd8c014a5ea9d5928c659db6039ee3f9ef953315/generative-question-answering/notebooks/evaluate.ipynb) for making explicit what differs between prompt variations.
