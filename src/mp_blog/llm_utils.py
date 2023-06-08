"""Utility methods and classes for LM demos"""
from dataclasses import dataclass
from typing import Dict, Callable
import importlib
import json

import pyarrow as pa


def make_prompt(prompt_str: str, parent_module: str, object_name: str) -> Dict:
    """TODO use https://github.com/microsoft/guidance or something less
    hacky and restrictive"""
    if parent_module == 'openai':
        if object_name == 'ChatCompletion':
            return dict(messages=[
                {'role': 'user', 'content': prompt_str},
            ])
        if object_name == "Completion":
            return dict(prompt=prompt_str)


def get_object_from_module(parent_module_name: str, object_name: str):
    '''Returns object from specified parent module'''
    parent_module = importlib.import_module(parent_module_name)
    an_object = getattr(parent_module, object_name)
    return an_object


def openai_chat_completion_parser(response) -> str:
    """
    TODO adapt for non-openai api and more complex responses, e.g. not just first choice
    """
    return response['choices'][0]['message']['content']


def llm_generate(
        model_version: str, method: Callable, model_params: Dict,
        text_input_dict: Dict, parser: Callable
) -> str:
    response = method(
        **text_input_dict,
        **model_params,
        model=model_version
    )
    res = parser(response)
    return res


EXPECTED_SCHEMA = pa.schema([
    pa.field('Platz', pa.int64()),
    pa.field('Schwimmer', pa.string()),
    pa.field('JG', pa.int64()),
    pa.field('Verein', pa.string()),
    pa.field('Zeit', pa.string()),
    pa.field('Punkte', pa.int64()),
    pa.field('Ort', pa.string()),
    pa.field('Datum', pa.string())
])

def enforce_data_contract(res: str, expected_schema: pa.schema) -> None:
    try:
        res_pylist = json.loads(res)
    except json.decoder.JSONDecodeError as _:
        msg = f"Syntax error when converting {res} to pylist."
        raise DataContractError(msg)

    try:
        res_table = pa.Table.from_pylist(res_pylist)
        if res_table.schema == expected_schema:
            return
        else:
            msg = f"Table of result has schema {res_table.schema}; expected{expected_schema}"
            raise DataContractError(msg)
    except (AttributeError, KeyError) as err:
        msg = f"Attribute error converting {res_pylist} to pyarrow table: {str(err)}"
        raise DataContractError(msg)

class DataContractError(Exception):
    pass
