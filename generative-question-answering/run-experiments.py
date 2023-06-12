"""Script for running llm experiments over configuration variants"""

from pathlib import Path
import json
import subprocess
from itertools import product

from pyrate_limiter import Limiter, RequestRate, Duration


with open(Path('.') / 'prompt_variants.json', 'r') as fp:
    prompt_variants = json.load(fp)

prompt_combinations = list(product(
    prompt_variants['contexts'],
    prompt_variants['questions'],
    prompt_variants['answer_formats'],
    prompt_variants['templates']
))

def run_experiment(context, question, answer_format, template) -> None:
    subprocess.run([
        'python', 'main.py',
        f'+context="{context}"',
        f'+question="{question}"',
        f'+answer_format="{answer_format}"',
        f'+template="{template}"',
        "hydra.job.chdir=True"
    ])

# Rate limiter for free gpt-3.5-turbo-0301. TODO make less hard-coded while avoiding RY
rate_limiter = Limiter(RequestRate(3, 59 * Duration.SECOND))

rep_idx = 1
n_reps = 1
n_combinations = len(prompt_combinations)
for context, question, answer_format, template in prompt_combinations:
    print(f'Running experiment {rep_idx} of {n_combinations}')
    rep_idx += 1
    for n_rep in range(n_reps):
        print(f'Running repeat {n_rep + 1} of {n_reps}')
        with rate_limiter.ratelimit('identity', delay=True):
            run_experiment(context, question, answer_format, template)
