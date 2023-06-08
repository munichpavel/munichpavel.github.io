---
title: "LMOps: Prompts just blew up your configuration space (and what to do about it)"
published: false
---

The first time I saw a software engineer with no data or statistics background demo a GPT-3-endpoint driven free-text classification use case, my reaction was "This is super exciting and super scary." It seems clear that the excitement around ChatGPT signals is more than just hype. What has changed and what has not given the performance jump of large language models (LLMs) is a question for all of us in the field to actively answer.

What has clearly changed is that tasks such as named-entity-recognition and question answering that would have required a number of different components, each of which would have required separate development followed by integration work to perform well, can now be largely off-loaded to a single API call to a single service. In a series of blog posts, I'll share thoughts and experience on what hasn't changed with this jump in LLM performance.

One area of software development (and one near and dear to those of us in machine learning) is configuration management. Put simply, which choice of dependencies and parameters will make your software perform best? For machine learning, this process focuses on model selection, which splits into finding the optimal family of algorithms and their implementation (e.g. linear regression, gradient boosted trees, neural network architecture) together with parametrization (i.e. optimizing algorithm hyperparameters).

Turning to LLMs, nearly all of the blog posts I have read regarding "best practices" focus on how to write a prompt that is most likely to yield good answers, such as how to order the text (e.g. if there's a question, put it at the end) and how to signal a section break.

* https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api

Of these best practices, the only one that has any theory-based aspect is the last, as choice of section break, as that

We have gone from the numerical (hyperparamter values) and categorical (e.g. model family, encoding method) configuration of traditional ML to numerical (e.g. temperature), categorical and syntactical configuration space of LLMs.

Furthermore, the prompt "architecture" that was optimal yesterday may cease to be if you are calling a model that is updated regularly (and without any version tags), such as ???.

Syntactical configuration dimensions

* If your domain data is in a non-English language, how is performance affected by problem-native vs English prompts? What about mixing prompt components (e.g. context section in problem native language, question format specification in English)?

## Generative question answering with Hydra


Prompt configuration elements

(maybe as tree structure)

1. Template structure (e.g. Jinja or python string) and its syntax.
1. Prompt component syntax (e.g. context-component, answer-format component, question-component)
1. Punctuation, tabs vs spaces, treatment of non-ascii characters (e.g. 'Männer' vs 'Maenner')
1. For non-English domains, when to use native and when to use English in each of the above.

The point is that even if you find a syntactical, numerical and categorical configuration what works well today, model updates, new models and further advances will mean that you had better automate the configuration performance evaluation.


## Highlighted examples

### Answer-format: data-only please!

How to get JSON (or csv etc) only response. Absurd example from BARD: tweet.

It can beome a be a trade-off due to token limits between more explicit answer format instructions and additional context. If your context text grows longer, it's useful to have the option of (re-) checking shorter answer format instructions, as changes to the LLM (either the same or a sucessor) could mean the detailed answer format of before is no longer needed.

### Context format: spaces sometimes matter

Interestingly, when trying the same variation of spacing in a distinct generative question answering problem, the same sensitivity to spaces was not present, giving further evidence for the importance of managing your configuration space robustly.

### You are still flipping a coin

Even if you robustly test out different prompt + model configurations and set your temperature to 0 (GPT), you are still calling a generative model, which means that you can and will get different answers for the same input.

## Appendix: Why JSON for prompt-config?

You may wonder why I chose JSON for the prompt configuration, rather than YAML. JSON is a data format with a relatively simple specification. So while it's not as human-readable as YAML, you are unlikely to get nasty surprises, and when it comes to "configurating" free text, there is enough potential for unexpected behavior--you shouldn't have to wonder how data serialization might contribute.

I chose to version-control the json prompt variants, which is not a bad choice for initial collaboration, but will likely need to be replaced with a proper data store as your prompt variants increase in size and complexity, if only to keep your git commit history from getting cluttered with prompt tweaking. Some git-features you will want to preserve if moving away from git are

1. audit trail: this can be accomplished in your pipline on the left (version control) or on the right (persisting experiment artifacts)
1. diffs: recognizing an added space or removed `` around text is not something you want to have to catch by eye, so be sure you have some diff tooling to recognize changes.

## Appendix: Why `dataclass` for prompt-configurations?

`dataclass`es occupy an often useful middle ground between standard library dicts (no typing or schema validation beyond missing key errors) and more restrictive Pydantic subclasses of `BaseModel`. As the application matures, the balance of validation would likely tip toward using Pydantic.

## Appendix: Prompt diffs across runs

https://docs.python.org/3/library/difflib.html
https://stackoverflow.com/questions/10451678/how-can-i-diff-and-patch-merge-strings-instead-of-files